# Python Script to get Org ID

# Import Python Modules
import tokens
import requests

# Build the Endpoint API URL
base_url = "https://api.meraki.com/api/v1"
resource_path = "/organizations"
url = base_url + resource_path

payload = None

headers = {
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": tokens.API_KEY
}

# Make the API call
response = requests.request('GET', url, headers=headers, data = payload)

# Print the response to the console
print(response.text.encode('utf8'))



