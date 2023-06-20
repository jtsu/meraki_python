# Reboot Device by Serial numbers
# Meraki API Reference:
# https://developer.cisco.com/meraki/api-latest/#!reboot-a-device

import time
import json
import meraki
import requests
import tokens

# Define your variables
device_serial_number = ""
device_serial_numbers = []

dashboard = meraki.DashboardAPI(tokens.API_KEY, suppress_logging=True)


# Enqueue a job to check connectivity status to the device
def queue_ping_job(device_serial):
    response = dashboard.devices.createDeviceLiveToolsPingDevice(
        device_serial,
        count=3
    )

    return response["pingId"]


# Return ping results from ping device job
def get_ping_job(device_serial, ping_id):
    response = dashboard.devices.getDeviceLiveToolsPingDevice(
        device_serial, ping_id
    )

    print(response)



ping_id = queue_ping_job(device_serial_number)
print("Waiting 10 seconds for job to complete.")
for i in range(1, 10 + 1):
    print(i)
    time.sleep(1)
print("")
get_ping_job(device_serial_number, ping_id)
