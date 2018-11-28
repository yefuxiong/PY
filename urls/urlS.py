
import requests
import re

#设置下载网络的页面url
url = 'http://jandan.net/pic/page-369#comments'
#设置请求头数据
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
#发送请求
response = requests.get(url,headers = headers)
#解析数据
html = response.content.decode("utf8")

#通过正则表达式获取我们需要的数据
reStr = '<img src="(.*?)" '
data = re.findall(reStr,html)
for item in data:
    if not item.startswith("http"):
        item = "http:"+item
    print(item)

    response = requests.get(item)
    data = response.content
    nameList = item.split("/")
    imageName = nameList[len(nameList) - 1]
    with open(imageName,"wb") as f:
        f.write(data)