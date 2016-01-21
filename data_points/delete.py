#!/usr/bin/env python3
''' Delete data points from KairosDB database using REST API through requests module.
  
    Please, check out the documentation on the KairosDB website:
      http://kairosdb.github.io/docs/build/html/restapi/DeleteDataPoints.html

    @author Fernando Paladini <fnpaladini@gmail.com>
'''

import requests
import json

kairosdb_server = "http://localhost:8080"

# Simple test
query = {
   "start_relative": {
        "value": "4",
        "unit": "years" 
   },
   "metrics": [
       {
           "name": "test",
           "limit": 10000
       }
   ]
}
response = requests.post(kairosdb_server + "/api/v1/datapoints/delete", data=json.dumps(query))
print("Status code (204 = Okay): %d" % response.status_code)
