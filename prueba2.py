import time
import datetime
from azure.storage import AccessPolicy, SharedAccessPolicy
from azure.storage.blob import BlobService, BlobSharedAccessPermissions


dateExpHou=int(datetime.datetime.now().strftime("%H"))
dateExpMin=int(datetime.datetime.now().strftime("%M"))

if dateExpMin >= 30:
	dateExpHou+=5
else:
	dateExpHou+=5
	dateExpMin+=30

dateExp=datetime.datetime.now().strftime("%Y-%m-%dT#:*:%S.0000000Z")
dateExp=dateExp.replace("#",str(dateExpHou))
dateExp=dateExp.replace("*",str(dateExpMin))
#dateExp=dateExp.replace("/","%3A")
	
#dateNow=datetime.datetime.now().strftime("%Y-%m-%dT%H/%M/%S")
#dateMod=dateNow.replace("/","%3A")
print dateExp


blob_service = BlobService(account_name='pinbanesco', account_key='z6Ufkrqf7Rp2ww1uieq3Z8fNSrPaY1vvPZOAOt8ggkTUxYAAtYsdMvj4W9s6l5QIJ/7Frtb/t6BZXNy0poedvg==')

ap = AccessPolicy(
    expiry=dateExp,
    permission=BlobSharedAccessPermissions.READ,
)
sas_token = blob_service.generate_shared_access_signature(
    container_name='test-firmas',
    blob_name='prueba.jpg',
    shared_access_policy=SharedAccessPolicy(ap),
)
url = blob_service.make_blob_url(
    container_name='test-firmas',
    blob_name='prueba.jpg',
    sas_token=sas_token,
)
print url

#Create Blob from path file
#blob_service.put_block_blob_from_path('test-firmas', 'prueba3.jpg', 'formato2.jpg')

#Delete Blob
#blob_service.delete_blob('test-firmas', 'prueba.txt')

#List all Blobs in Container
"""
blobs = []
marker = None
while True:
    batch = blob_service.list_blobs('test-firmas', marker=marker)
    blobs.extend(batch)
    if not batch.next_marker:
        break
    marker = batch.next_marker
for blob in blobs:
    print(blob.name)
"""