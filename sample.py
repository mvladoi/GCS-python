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
