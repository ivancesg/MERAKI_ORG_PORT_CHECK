import requests
import json
import pandas as pd
from datetime import datetime
import os

path = ".\\REPORTS"

isExist = os.path.exists(path)

if not isExist:
    os.makedirs(path)

now = datetime.now()
excel_name = "Report-" + str(now.date()) + "_" + str(now.strftime("%H-%M-%S")) + ".xlsx"
excel_path = ".\\REPORTS\\" + excel_name
writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
writer.save()

df = pd.read_excel(excel_path)
df = pd.DataFrame([],index=[], columns=['Switch S/N', 'Errors', 'Port with Errors', 'Warnings', 'Port with Warnings', 'Half Duplex', 'Port with Half Duplex'])

base_url = "https://n149.meraki.com" #modify this with your base URL

organizations_array = []
number_to_select = 1
switches_array = []
networks_array = []
ports_array = []
fila = 1

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "4ab0c0f91eeb3e48c8d47d892ef64b7954147464" #modify this with your API key
}

print("#######################################################################")
print("############################CREATED BY#################################")
print("########################IVÁN CES GÁNDARA###############################")
print("############# " + "https://www.linkedin.com/in/ivances/" + " ####################")
print("#######################################################################")
print("")

url_getOrganizations = base_url + "/api/v1/organizations"
response_getOrganizations = requests.request('GET', url_getOrganizations, headers=headers, data=payload)
allOrganizations = json.loads(response_getOrganizations.text)
for organization in allOrganizations:
    print(str(number_to_select) + " -> " + organization["name"])
    number_to_select = number_to_select + 1
    organizations_array += [organization["id"]]
number_selected = input("Select the Organization that u want to check (insert the number and press Enter): ")
number_selected_final = int(number_selected) - 1
organization_ID = organizations_array[number_selected_final]

url_getNetworks = base_url + "/api/v1/organizations/" + organization_ID + "/networks"
response_getNetworks = requests.request('GET', url_getNetworks, headers=headers, data=payload)
allNetworks = json.loads(response_getNetworks.text)

for network in allNetworks:
    networks_array += [network["id"]]

for network in networks_array:
    url_getNetworkDevices = base_url + "/api/v1/networks/" + network + "/devices"
    response_devices_network = requests.request('GET', url_getNetworkDevices, headers=headers, data = payload)
    allDevices = json.loads(response_devices_network.text)
    for device in allDevices:
        if "MS" in device["model"]:
            switches_array += [device["serial"]]

for switch in switches_array:
    df.loc[fila, 'Switch S/N'] = switch
    url_getDeviceSwitchPorts = base_url + "/api/v1/devices/" + switch + "/switch/ports/statuses"
    response_getDeviceSwitchPorts = requests.request('GET', url_getDeviceSwitchPorts, headers=headers, data=payload)
    allPorts = json.loads(response_getDeviceSwitchPorts.text)
    for port in allPorts:
        if "Port disconnected" in port["errors"]:
            df.loc[fila, 'Errors'] = "OK"
            df.loc[fila, 'Port with Errors'] = "OK"
        else:
            df.loc[fila, 'Errors'] = port["errors"]
            df.loc[fila, 'Port with Errors'] = port["portId"]

        if not port["warnings"]:
            df.loc[fila, 'Warnings'] = "OK"
            df.loc[fila, 'Port with Warnings'] = "OK"
        else:
            df.loc[fila, 'Warnings'] = port["warnings"]
            df.loc[fila, 'Port with Warnings'] = port["portId"]

        if port["duplex"] == "":
            df.loc[fila, 'Half Duplex'] = "OK"
            df.loc[fila, 'Port with Half Duplex'] = "OK"
        else:
            df.loc[fila, 'Half Duplex'] = port["duplex"]
            df.loc[fila, 'Port with Half Duplex'] = port["portId"]
    fila = fila + 1


df.to_excel(excel_path, index = False)