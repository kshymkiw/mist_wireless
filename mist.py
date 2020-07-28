import requests
import json
import time
import os
import string
# Set Parameters you need to gather data from the Mist REST API
OrgID = '<Your ORG ID>'
AuthToken = '<Your Auth Token>'
URL = "https://api.mist.com/api/v1/orgs/%s/stats" % (OrgID)
# Define the Headers for Token Auth
headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Token {}'.format(AuthToken)
}
# Make a GET Request and get HTTP Response Code
response = requests.get(URL, headers=headers)
data = response.json()
# Print Data Response
print(data["num_sites"], data["num_devices"], data["num_inventory"], data["num_devices_connected"], data["num_devices_disconnected"])
