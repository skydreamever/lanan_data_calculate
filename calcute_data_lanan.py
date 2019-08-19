import requests

#用户资料
USERNAME = ""
PASSWORD = ""


#请求头
HEADER = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) lanan-mac/2.0.0 Chrome/59.0.3071.115 Electron/1.8.7 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate'
}

POSTDATA = {
    'username': USERNAME,
    'password': PASSWORD
}

HOSTURL = 'https://v2ray.api.lanan.xyz/client/api.php'

#登录POST请求
AUTHURL = HOSTURL + '?s=user.auth'
response = requests.post(url=AUTHURL, data=POSTDATA, headers=HEADER, timeout=10)
CONTENT = eval(response.content.decode("utf-8"))
TOKEN = CONTENT["data"]

#选择package
PACKAGEINFO = HOSTURL + '?s=whmcs.hosting&token=' + TOKEN;
response = requests.get(url=PACKAGEINFO, headers=HEADER, timeout=10)
CONTENT = eval(response.content.decode("utf-8"))

count = 0;
for index in CONTENT['data']:
    print("%d:%s" % (count, index['name']))
    count += 1
index = input("选择查询套餐序号：")

PACKAGEID = CONTENT['data'][eval(index)]['packageId']
SERVERID = CONTENT['data'][eval(index)]['serverId']

#请求用量
DATAINFO = "%s%s%s%s%s%s%s" % (HOSTURL, '?s=v2ray.userInfo&token=', TOKEN, "&serverId=", SERVERID, "&packageId=", PACKAGEID)
response = requests.get(url=DATAINFO, headers=HEADER, timeout=10)
CONTENT = eval(response.content.decode("utf-8"))

u = CONTENT['data']['u']
d = CONTENT['data']['d']
transfer_enable = CONTENT['data']['transfer_enable']

print("总量：%sG" % (transfer_enable/1024/1024/1024))
print("使用：%sG" % ((u+d)/1024/1024/1024))
