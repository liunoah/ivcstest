import requests
import json
import time
from threading import Thread

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
Authorization = ""

url = "https://192.168.31.32:3000/v1/"
def Authenticationurl():
    url = "http://192.168.31.204:3131"
    server = "643d357f92dcc10832e47697"
    key = "k2Fzbv7MSasLeElWEY5XxAM1ZEpliUsNrwgOlK9obqNgvGRqamgw7ClzqEE/CP4sK6lrpBaeArSGPK43dMbojDfey8Hk6a5cN4zqGj6vQjtQxcSbCjoliQskLJJ7b47QSShcRhRiS56JxaUcQfOgZopz4Zp/Tpu8nsc0o96P8f8="
    payload=json.dumps({
        "server":server,
        "key":key
    })
    # payload="server="+server+"&key="+key
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    Authorization = response.text
    print(response.text)
# Authenticationurl()
Authorization = "MAuth realm=http://marte3.dit.upm.es,mauth_signature_method=HMAC_SHA256,mauth_serviceid=643d357f92dcc10832e47697,mauth_cnonce=f2f127e8a4b92f63,mauth_timestamp=1681733731643,mauth_signature=M2EwY2FmZGU1NDBhYThiNmE5OTkxY2I5NDc4ZWJmNTU5ZDZiMjhmOWFmMzUyNDNiZDFjZTQ5ZWJhMWFjODJlNA=="
headers = {
    'Authorization': Authorization,
    'Content-Type': 'application/json'
    }
def create_room(num):
    url = "https://192.168.31.32:3000/v1/rooms/"

    payload = json.dumps({
    "name": num,
    "options": {
        "views": [],
        "sip": {
        "sipServer": "192.168.31.204",
        "username": "1001",
        "password": "123456"
        }
    }
    })
    
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    # print(response.text)
    print(num,response.json()['_id'])
    

    

def delete_room():
    payload={}

    response = requests.request("DELETE", url+"rooms"+roomid, headers=headers, data=payload)

def delete_all_room():
    payload={}
    response = requests.request("GET", url+"rooms", headers=headers, data=payload)
    response = response.json()
    print()

for i in range(100,500):
    time.sleep(1)
    create_room(str(i))