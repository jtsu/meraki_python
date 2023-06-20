# Reboot Device by Serial numbers
# Meraki API Reference:
# https://developer.cisco.com/meraki/api-latest/#!return-a-ping-device-job

import time
import json
import meraki
import tokens

# Define your variables
device_serial_number = ""

dashboard = meraki.DashboardAPI(tokens.API_KEY, suppress_logging=True)


# Enqueue a job to check connectivity status to the device
def queue_ping_job(device_serial):
    response = dashboard.devices.createDeviceLiveToolsPingDevice(
        device_serial,
        count=3
    )

    ##### LAB: Parse response to get ping ID and return value #####
    return response


# Return ping results from ping device job
def get_ping_job(device_serial, ping_id):
    response = dashboard.devices.getDeviceLiveToolsPingDevice(
        device_serial, ping_id
    )
    print(response)


#Call function and assign return value
ping_id = queue_ping_job(device_serial_number)

# Timer to wait for job queue to complete
print("Waiting 10 seconds for job to complete.")
for i in range(1, 10 + 1):
    print(i)
    time.sleep(1)
print("")

#Call function to get ping job results
##### LAB: Add arguments needed by function #####
get_ping_job()
