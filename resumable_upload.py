import io
import google.auth
import google.auth.transport.requests as tr_requests
from google.resumable_media.requests import ResumableUpload


bucket='resume_vladoi'
file_to_transfer='/Users/mihai/Desktop/file.mp4'
blob_name='file.mp4'

ro_scope = u'https://www.googleapis.com/auth/devstorage.read_only'
credentials, _ = google.auth.default(scopes=(ro_scope,))
transport = tr_requests.AuthorizedSession(credentials)



url_template = (u'https://www.googleapis.com/upload/storage/v1/b/{bucket}/o?'u'uploadType=resumable')
upload_url = url_template.format(bucket=bucket)
chunk_size = 1024 * 1024
upload = ResumableUpload(upload_url, chunk_size)
stream = io.FileIO(file_to_transfer)
metadata = {u'name': blob_name}

content_type = u'video/mp4'

response = upload.initiate(transport, stream, metadata, content_type)
print(response)

upload_id = response.headers[u'X-GUploader-UploadID']
upload.resumable_url == upload_url + u'&upload_id=' + upload_id
response0 = upload.transmit_next_chunk(transport)
print(response0)


while (upload.finished is False):
  upload.transmit_next_chunk(transport)
