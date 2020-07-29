# mist_wireless
This is a python script which pulls Org Level Stats from the Mist REST API, and puts them into InfluxDB.

### Configuration

You will need the following from your Mist Account
1. Org ID - This is accessible from https://manage.mist.com Then click on Organization and Settings.  You can copy your Org ID directly from here.
2. Your API Token - If you haven't created one, make sure you're logged into your Mist Dashboard, and go to https://api.mist.com/api/v1/self/apitokens and hit POST

Drop your OrgID and Token in lines 56 and 57

This script assumes you have already created an InfluxDB with the name mistwireless.  If you want to change any of the DB parameters you will need to edit lines 12-17 and 29.

### How to use the script

Downlaod the script in a location on your machine, and the rest is simple

    python3 mist.py
  
You would then see the following output letting you know it is working:

    Wrote {data} to influx, Sleeping
    Wrote {data} to influx, Sleeping
    
The script will self run every 10 seconds.  If you want to change this, just change the scheduler.


### Special Thanks 

Special thanks to OMGKitteh who massively helped me on this.
