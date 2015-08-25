import time
import datetime
import json
import urlparse
import ast
import urllib2
from azure.storage import BlobService
from azure.storage import AccessPolicy
from azure.storage.sharedaccesssignature import SharedAccessPolicy, SharedAccessSignature

#-------------------------------------------------------------------------
# Constants for the share access signature
SIGNED_START = 'st'
SIGNED_EXPIRY = 'se'
SIGNED_RESOURCE = 'sr'
SIGNED_PERMISSION = 'sp'
SIGNED_IDENTIFIER = 'si'
SIGNED_SIGNATURE = 'sig'
RESOURCE_BLOB = 'b'
RESOURCE_CONTAINER = 'c'
SIGNED_RESOURCE_TYPE = 'resource'
SHARED_ACCESS_PERMISSION = 'permission'


#-------------------------------------------------------------------------------------------------------
def convert_query_string(query_string):
	''' Converts query string to str. The order of name, values is very import and can't be wrong.'''
	convert_str = ''
	if query_string.has_key(SIGNED_START):
		convert_str += SIGNED_START + '=' + str(query_string[SIGNED_START]) + '&'
	convert_str += SIGNED_EXPIRY + '=' + str(query_string[SIGNED_EXPIRY]) + '&'
	convert_str += SIGNED_PERMISSION + '=' + str(query_string[SIGNED_PERMISSION]) + '&'
	convert_str += SIGNED_RESOURCE + '=' + str(query_string[SIGNED_RESOURCE]) + '&'

	if query_string.has_key(SIGNED_IDENTIFIER):
		convert_str += SIGNED_IDENTIFIER + '=' + str(query_string[SIGNED_IDENTIFIER]) + '&'
	convert_str += SIGNED_SIGNATURE + '=' + urllib2.quote(str(query_string[SIGNED_SIGNATURE])) + '&'
	return convert_str
#------------------------------------------------------------------------------------------------------



DEV_STORAGE_ACCOUNT_NAME = "pinbanesco"
DEV_STORAGE_ACCOUNT_KEY = "z6Ufkrqf7Rp2ww1uieq3Z8fNSrPaY1vvPZOAOt8ggkTUxYAAtYsdMvj4W9s6l5QIJ/7Frtb/t6BZXNy0poedvg=="
CONTAINER_NAME='test-firmas'
STORAGE_URL = 'https://pinbanesco.blob.core.windows.net/'



def generate_signature_blob(dev_storage_account_name,dev_storage_account_key,container_name):
	query_string={}
 	date=datetime.datetime.now().strftime("%Y-%m-%d")
 	sas = SharedAccessSignature(account_name=dev_storage_account_name,account_key=dev_storage_account_key)
 	accss_plcy = AccessPolicy()
 	accss_plcy.expiry = date 
 	accss_plcy.permission = 'r'
 	sap = SharedAccessPolicy(accss_plcy)
 	string = ast.literal_eval(json.dumps(urlparse.parse_qs(sas.generate_signed_query_string(container_name,'test-firmas',sap))))
 	return convert_query_string(string).replace("test-firmas","c")

def put_blob(storage_url,container_name, blob_name,qry_string,x_ms_blob_type):
 	opener = urllib2.build_opener(urllib2.HTTPHandler)
 	request = urllib2.Request(storage_url+container_name + '/' + blob_name+'?'+qry_string, data='Hello World!!')
 	request.add_header('x-ms-blob-type', x_ms_blob_type)
 	print x_ms_blob_type
 	request.get_method = lambda: 'PUT'
 	opener.open(request)

sas_url = generate_signature_blob(DEV_STORAGE_ACCOUNT_NAME,DEV_STORAGE_ACCOUNT_KEY,CONTAINER_NAME)
put_blob(STORAGE_URL,CONTAINER_NAME,"prueba.txt",sas_url,"BlockBlob")
