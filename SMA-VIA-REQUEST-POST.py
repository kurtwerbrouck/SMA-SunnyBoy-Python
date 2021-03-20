import json
import requests
import time
import threading

def readingoutsma():
    url = 'http://192.168.0.164/dyn/getValues.json?sid=' + sid
    payload = ('{"destDev":[],"keys":["6400_00260100","6400_00262200","6100_40263F00"]}')
    headers = {"Content-Type": "application/json", "Accept-Charset": "UTF-8"}
    r = requests.post(url, data=payload, headers=headers)
    print("Request reply:")
    print(r)
    j = json.loads(r.text)
    print("Json reply:")
    print(j)
    Total = j["result"]["012F-730B7309"]["6400_00260100"]["1"][0]["val"]
    Today = j["result"]["012F-730B7309"]["6400_00262200"]["1"][0]["val"]
    Current = j["result"]["012F-730B7309"]["6100_40263F00"]["1"][0]["val"]
    print("Returned values: ")
    print(Total,Today,Current)
    d = {}
    d["Total"] = Total
    d["Today"] = Today
    d["Current"] = Current
    print("Received Data from SMA")
    print(json.dumps(d, ensure_ascii=False))
    t = threading.Timer(0.5,readingoutsma)
    t.start()
    
url = 'http://192.168.0.164/dyn/login.json'
payload = ('{"pass" : "xxx", "right" : "yyy"}')
#headers = {"Content-Type": "application/json"}#, "Accept-Charset : "UTF-8"}
headers = {"Content-Type":"application/json" , "Connection" : "Keep-Alive","Keep-Alive": "timeout=5, max=1000"}
r = requests.post(url, data=payload, headers=headers)
print("Request reply:")
print(r)
j = json.loads(r.text)
print("Json reply:")
print(j)
sid = j['result']['sid']
print("Sid reply:")
print(sid)

t = threading.Timer(0.5,readingoutsma)
t.start()