#!/usr/bin/env python3
''' List tag names from KairosDB database using REST API through requests module.
    
    Please, check out the documentation on the KairosDB website:
        http://kairosdb.github.io/docs/build/html/restapi/ListTagNames.html

    @author Fernando Paladini <fnpaladini@gmail.com>
'''

import requests

kairosdb_server = "http://localhost:8080"

# Making the request to KairosDB
response = requests.get(kairosdb_server + "/api/v1/tagnames")

# Printing the response
print(response.json())