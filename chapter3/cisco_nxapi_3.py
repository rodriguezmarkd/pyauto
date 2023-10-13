#!/usr/bin/env python3

import requests
import json
import pprint

url='http://10.32.1.205/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "hostname lax-cor-r1-new",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

#print(response['result']['body']['nxos_ver_str'])
