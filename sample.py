 from google.cloud import storage
 from google.cloud.storage import Blob  
 storage_client = storage.Client()

 # get all the buckets
 buckets = storage_client.list_buckets()
 for bucket in buckets:
     print(bucket.name)
 # output  bucket_name

 # get all the blobs in a bucket
 bucket = client.get_bucket("bucket_name")
 blobs = list(bucket.list_blobs())
 for blob in blobs:
     print (blob)
 # print the blobs: blob_name

 #check if the blob exists
 assert isinstance(bucket.get_blob('blob_name'), Blob)

 #get the blob from path
 my_blob = Blob.from_string("gs://bucket_name/blob_name")

 # List the files in a folder 
 files = bucket.list_blobs(prefix='folder_name')
 for f in files:
     print(f.name)

   
   
def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))
    
    
    
    
# retry on connection fails     
from urllib3.exceptions import ProtocolError
from google.api_core import retry

predicate = retry.if_exception_type(
    ConnectionResetError, ProtocolError)
reset_retry = retry.Retry(predicate)

data = reset_retry(blob.download_as_string)()



https://dev.to/sethmlarson/python-data-streaming-to-google-cloud-storage-with-resumable-uploads-458h
 
 
 
# convert a ipynb file to py file
# https://stackoverflow.com/questions/59530429/how-to-convert-multiple-ipynb-files-which-are-in-gcp-to-py-files/59530544#59530544

from google.cloud import storage
from IPython.display import IFrame

client = storage.Client()
bucket = client.get_bucket('test-vladoi')
blob = bucket.get_blob('test.ipynb')
blob.download_to_filename('test.ipynb')

!jupyter nbconvert --to html test.ipynb
!jupyter nbconvert --to python test.ipynb

IFrame('test.html', 600, 200)
IFrame('test.py', 600, 200)
 

