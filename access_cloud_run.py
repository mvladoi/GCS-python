from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

service_url = 'example.com'
key_file = 'key.json'

credentials = service_account.IDTokenCredentials.from_service_account_file(
    key_file, target_audience=service_url)
authed_session = AuthorizedSession(credentials)
response = authed_session.get(service_url)
