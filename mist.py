import requests
import json
import time
import os
import string
import schedule

### Set Variables
OrgID = '<Your OrgID from Mist Dashboard>'
AuthToken = '<Your AuthToken from Mist API>'
url = "https://api.mist.com/api/v1/orgs/%s/stats" % (OrgID)

payload = {}
headers = {
  'Authorization': 'Token {}'.format(AuthToken),
  'Content-Type': 'application/json'
}
### Define Function to get Mist API Information
def fetch_mist():
	print("Gathering Stats from Mist")
	response = requests.request("GET", url, headers=headers, data = payload)
### Print the Output to make sure the GET succeeded
	print(response.ok)
	print(response.status_code)
### Read the output from Mist
	data = response.text
### Parse this into JSON
	parsed = json.loads(data)
### Print the Output
# print(json.dumps(parsed, indent=4))
### Extract the Data
	Number_of_Sites = parsed["num_sites"]
	Number_of_Devices_in_Inventory = parsed["num_inventory"]
	Number_of_Devices_Connected = parsed["num_devices_connected"]
	Number_of_Devices_Disconnected = parsed["num_devices_disconnected"]
### Print the Output of each
	print("Number of Sites:" + str(Number_of_Sites))
	print("Number of Devices in Inventory:" + str(Number_of_Devices_in_Inventory))
	print("Number of Devices Connected:" + str(Number_of_Devices_Connected))
	print("Number of Devices Disconnected:" +str(Number_of_Devices_Disconnected))
### Schedule fetch_mist
schedule.every(10).seconds.do(fetch_mist)
while True:
	schedule.run_pending()
	time.sleep(1)