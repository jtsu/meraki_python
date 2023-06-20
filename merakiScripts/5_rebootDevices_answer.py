# Reboot Device by Serial numbers
# Meraki API Reference: 
# https://developer.cisco.com/meraki/api-latest/#!reboot-a-device


import json
import meraki
import requests
import tokens

# Define your variables
device_serial_number = ""
device_serial_numbers = []

# Function to reboot a single device using the request module
def reboot_device(device_serial):
   
    base_url = "https://api.meraki.com/api/v1"
    resource_path = f"/devices/{device_serial}/reboot"
    url = base_url + resource_path

    payload = None

    headers = {
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": tokens.API_KEY
    }

    response = requests.request('POST', url, headers=headers, data = payload)

    json_data = response.json()
    print(json.dumps(json_data, indent=2))


# Function to reboot a list of devices using the meraki sdk
def reboot_devices_in_list(device_serials):

    if len(device_serials) != 0:  # Reboot specific list of APs
        for item in device_serials:
            response = dashboard.devices.rebootDevice(item)
            print(response)


# Call the reboot functions
reboot_ap = reboot_device(device_serial_number)
reboot_aps = reboot_devices_in_list(device_serial_numbers)