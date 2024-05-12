import requests
from dotenv import load_dotenv
import os

load_dotenv()

endpointResPost = os.getenv('ENDPOINT_POST')
endpointResGet = os.getenv('ENDPOINT_GET')

resPost = requests.post(endpointResPost, params={
  "grant_type"    : os.getenv('GRANT_TYPE'),
  "client_id"     : os.getenv('CLIENT_ID'),
  "client_secret" : os.getenv('CLIENT_SECRET'),
  "refresh_token" : os.getenv('REFRESH_TOKEN')
})

if resPost:
  print(f"success! {resPost.status_code}")
else:
  raise Exception(f"not success status: {resPost.status_code}")

access_token = resPost.json()["access_token"]

resGet = requests.get(endpointResGet, headers={
  "Authorization"    : f"Bearer {access_token}"
})

print(resGet.json())