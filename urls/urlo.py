import requests
from bs4 import BeautifulSoup

url = 'https://cuiqingcai.com/1319.html'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
data = requests.get(url,headers =headers)
html =data.content.decode('utf-8')

soup = BeautifulSoup(html,"html.parser")
print(soup)