import google.auth
import google.auth.transport.requests

creds, projects = google.auth.default()
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

print(creds.token)
#'ya29.IpgBtweYBBqA6-j0s8dz_tZdspe1m0vyhf2KemSlFLoM6syDfNRtRW62yNUhNkf5fb_fbrOM5Gxl6ePYvmJX_MUTHcZQHwvxc_oFZcXk8ZE7QAXdUQ1H3P1SYjupWhvZSKx5uv7zCbt5NePwIpWLs0fda3NLNqo2EO-4YfClEGJpfywR2LpPsOA801HikCQuXztDUOW6jihta2E'

bucket = 'test'
file = 'file'

url = 'https://www.googleapis.com/storage/v1/b/{}/o/{}?alt=media'.format(bucket, file)
headers={'Authorization': 'Bearer {}'.format(creds.token), 'Accept': 'application/json'}

r = requests.get(url, headers=headers)

print(r.text)
#The content of your file
