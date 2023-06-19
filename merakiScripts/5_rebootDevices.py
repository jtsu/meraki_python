
import json
import meraki
import tokens

dashboard = meraki.DashboardAPI(tokens.API_KEY, suppress_logging=True)
delay = 2


def getDeviceName(deviceSerialNumbers):

    deviceName = []

    for serial in deviceSerialNumbers:
        try:
            response = dashboard.devices.getDevice(serial)
            print(f"{response['lanIp']}")

            deviceName.append(response['name'])
        except:
            print(response)
            continue
    deviceName.sort()
    print(deviceName)

    return(deviceName)


def rebootDevice(deviceSerialNumbers):
    rebootStatus = []

    if len(deviceSerialNumbers) != 0:  # Reboot specific list of APs
        for item in deviceSerialNumbers:
            try:
                reboot = dashboard.devices.rebootDevice(serial=item)
                rebootStatus.append({"serial": item, "status": reboot})
                time.sleep(delay)
            except:
                print(f"Exception error: {item} -Check SDK Logs. Continuing.")
                continue
    return(rebootStatus)



def rebootStatus(rebootResults):
    passCount = 0
    failCount = 0
    results = []
    apFailList = []

    for item in rebootResults:
        if item["status"]["success"] is True:
            passCount += 1
        else:
            failCount += 1
            apFailList.append(item["serial"])

    results.append({"apRebooted": passCount, "apNotRebooted": failCount, "apFailList": apFailList})
    print(results)
    return (results)


if __name__ == '__main__':


    deviceSerialNumbers = []

    print("Starting reboot script.  It may take several minutes to complete.")
    rebootAP = rebootDevice(deviceSerialNumbers)
    status = rebootStatus(rebootAP)
