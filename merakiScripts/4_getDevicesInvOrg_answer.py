# This python script should return the device inventory for an organization
# Check Meraki API Dashboard Docs for Resource Path
# https://developer.cisco.com/meraki/api-latest/

import tokens
import requests
import json

base_url = "https://api.meraki.com/api/v1"
resource_path = f"/organizations/{tokens.ORG_ID}/inventory/devices"
url = base_url + resource_path

payload = None

headers = {
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": tokens.API_KEY
}

response = requests.request('GET', url, headers=headers, data = payload)

json_data = response.json()
print(json.dumps(json_data, indent=2))

