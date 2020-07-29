import requests
import json
import time
import os
import string
import schedule
from influxdb import InfluxDBClient
 
 
def fetchInfluxClient() -> InfluxDBClient:
    # The database we created
    dbname = "mistwireless"
    hostname = "localhost"
    port = 8086
    #user = "username"
    #password = "password"
    client = InfluxDBClient(hostname, port, dbname)
    return client
 
 
def writeToInflux(c: InfluxDBClient, d: dict) -> bool:
    iso = time.ctime()
    # Cant remember what session is...
    session = "env"
    json_body = [
        {"measurement": session, "tags": {"run": 1,}, "time": iso, "fields": d}
    ]
    try:
        ret = c.write_points(json_body, database='mistwireless')
        return True
    except Exception as e:
        print(f"Shits fucky: {e}")
        return False
 
 
def fetch_mist(org: str, headers: dict, payload: dict) -> dict:
    """Function to snag data from mist
    Returns:
        r.json: a dict containing the results from Mist API
    """
    mist_url = f"https://api.mist.com/api/v1/orgs/{org}/stats"
    r = requests.get(mist_url, headers=headers, json=payload)
    if r.status_code != requests.status_codes.codes.ALL_OK:
        print("Got unexpected status code, exiting")
        print("%s - %s" % (r.status, r.text))
        exit(1)
    try:
        return r.json()
    except Exception as e:
        print(f"Got unexpected data from mist API{e}. Exiting. Data:\n{r.text}")
        exit(1)
 
 
def main():
    ### Set Variables
    OrgID = "<Your OrgID>"
    AuthToken = "<Your AuthToken>"
    # Get influx client
    iclient = fetchInfluxClient()
 
    payload = {}
    headers = {
        "Authorization": "Token {}".format(AuthToken),
        "Content-Type": "application/json",
    }
    mist_data = fetch_mist(OrgID, headers, payload)
    data = dict()
    data["num_sites"] = mist_data["num_sites"]
    data["num_inventory"] = mist_data["num_inventory"]
    data["num_devices_connected"] = mist_data["num_devices_connected"]
    data["num_devices_disconnected"] = mist_data["num_devices_disconnected"]
 
    while True:
        mist_data = fetch_mist(OrgID, headers, payload)
        data = dict()
        data["num_sites"] = mist_data["num_sites"]
        data["num_inventory"] = mist_data["num_inventory"]
        data["num_devices_connected"] = mist_data["num_devices_connected"]
        data["num_devices_disconnected"] = mist_data["num_devices_disconnected"]
 
        if writeToInflux(iclient, data):
            print("Wrote {data} to influx. Sleeping")
        else:
            print("Wrote {data} to influx. Sleeping")
        time.sleep(10)
 
 
if __name__ == "__main__":
    main()
 