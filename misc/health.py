#!/usr/bin/env python3
''' Check health status of KairosDB using REST API through requests module.
    
    Please, check out the documentation on the KairosDB website:
        http://kairosdb.github.io/docs/build/html/restapi/Health.html

    @author Fernando Paladini <fnpaladini@gmail.com>
'''

import requests
import json

kairosdb_server = "http://localhost:8080"

# Returns the status of each health check as JSON.
response = requests.get(kairosdb_server + "/api/v1/health/status")
print(response.json())

# Checks the status of each health check. 
# If all are healthy it returns status 204 otherwise it returns 500.
response = requests.get(kairosdb_server + "/api/v1/health/check")
print("Is everything okay with KairosDB? %s" % (response.status_code == 204))