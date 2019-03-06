#coding:utf-8
import json
import urllib2
import subprocess
p = subprocess.Popen("/opt/check.sh",shell=True,stdout=subprocess.PIPE)
str = p.stdout.read()
url = "https://oapi.dingtalk.com/robot/send?access_token=e5f1e804439df65dd205c6a7fffd4e070e1925ab427823c7798967238722058f"
header = {
    "Content-Type":"application/json",
    "Charset":"utf-8"
    }


data = {
        "msgtype":"text",
        "text":{
            "content":"%s"%(str)
        },
        "at":{
                "atMobiles":[]
        }
    }
sendData = json.dumps(data)
request = urllib2.Request(url,data = sendData,headers = header)
opener= urllib2.urlopen(request)
print(opener.read())