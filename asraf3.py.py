import requests
import urllib.parse as parse
import re
import json
# keyname = "女装"
goods_id = "118885061601"
token = "IVI735SIJPZFVJZPZWAZEIXUBXMVRAS6Q367NLKI2RU7CWHSBKEQ113b592"
#url = "http://mobile.yangkeduo.com/search_catgoods.html?search_key="+parse.quote(keyname)+"&search_type=goods&source=search"
url = "http://mobile.yangkeduo.com/goods_comments.html?goods_id="+goods_id
headers = {
    "Cookie": "PDDAccessToken="+token+"; ua=Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ===  iOS/12.5.1 Model/iPhone7,2 BundleID/com.xunmeng.pinduoduo AppVersion/5.59.0 AppBuild/202104192233 pversion/1667",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ===  iOS/12.5.1 Model/iPhone7,2 BundleID/com.xunmeng.pinduoduo AppVersion/5.59.0 AppBuild/202104192233 pversion/1667",
    "AccessToken": token,
    "Referer": "http://mobile.yangkeduo.com/goods.html?goods_id="+goods_id
}
res = requests.get(url,headers=headers)

resp = re.search('window.rawData=(.+);',res.text)
resp = resp.group(1)
print(resp)
resp_json=json.loads(resp)
commentsList = resp_json["store"]["commentsList"]
for i in commentsList:
    print(i['comment'])
    for k in i['pictures']:
        print(k["url"])
