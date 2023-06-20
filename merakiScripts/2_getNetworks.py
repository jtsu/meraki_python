# Get Networks in Org
# Meraki API Reference:
# https://developer.cisco.com/meraki/api-latest/#!list-the-networks-that-the-user-has-privileges-on-in-an-organization

import tokens
import requests
import json

base_url = "https://api.meraki.com/api/v1"
resource_path = f"/organizations/{tokens.ORG_ID}/networks"
url = base_url + resource_path


payload = None

headers = {
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": tokens.API_KEY
}

response = requests.request('GET', url, headers=headers, data = payload)

#print(response.text.encode('utf8'))
json_data = response.json()
print(json.dumps(json_data, indent=2))

