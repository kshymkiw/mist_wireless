# mist_wireless
This is a python script which pulls Org Level Stats from the Mist REST API, and puts them into InfluxDB.

### Configuration

You will need the following from your Mist Account
1. Org ID - This is accessible from https://manage.mist.com Then click on Organization and Settings.  You can copy your Org ID directly from here.
2. Your API Token - If you haven't created one, make sure you're logged into your Mist Dashboard, and go to https://api.mist.com/api/v1/self/apitokens and hit POST

Drop your OrgID and Token in lines 72 and 73

This script assumes you have already created an InfluxDB with the name mistwireless.  If you want to change any of the DB parameters you will need to edit lines 12-17 and 29.

### How to use the script

Downlaod the script in a location on your machine, and the rest is simple

    python3 mist.py
  
You would then see the following output letting you know it is working:

    Wrote {data} to influx, Sleeping
    Wrote {data} to influx, Sleeping
    
The script will self run every 10 seconds.  If you want to change this, just change the scheduler.

### InfluxDB Data

The data will be stored in <database>, env, $variables:
    
    > select * from env
    name: env
    time                 num_devices_connected num_devices_disconnected num_inventory num_sites run total
    ----                 --------------------- ------------------------ ------------- --------- --- -----
    2020-08-04T17:20:45Z 1                     1                        2             1         1   5
    2020-08-04T17:20:56Z 1                     1                        2             1         1   5
    2020-08-04T17:21:07Z 1                     1                        2             1         1   5
    2020-08-04T17:21:18Z 1                     1                        2             1         1   5




### Special Thanks 

Special thanks to OMGKitteh who massively helped me on this.
