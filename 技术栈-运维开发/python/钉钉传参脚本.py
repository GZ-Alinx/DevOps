#coding:utf-8
import json
import urllib2
import sys

if len(sys.argv) < 2:
    exit(1)
print sys.argv[1]
url = "这里填webhook地址"
header = {
    "Content-Type":"application/json",
    "Charset":"utf-8"
    }

data = {
        "msgtype":"text",
        "text":{
            "content":sys.argv[1]
        },
        "at":{
                "atMobiles":[]
        }
    }
sendData = json.dumps(data)
request = urllib2.Request(url,data = sendData,headers = header)
opener= urllib2.urlopen(request)
print(opener.read())