from azure.storage import BlobService

blob_service = BlobService(account_name='pinbanesco', account_key='z6Ufkrqf7Rp2ww1uieq3Z8fNSrPaY1vvPZOAOt8ggkTUxYAAtYsdMvj4W9s6l5QIJ/7Frtb/t6BZXNy0poedvg==')


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