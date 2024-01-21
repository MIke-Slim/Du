import requests
from bs4 import BeautifulSoup
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
titles=requests.get('https://www.ugnx.net/wd',headers=headers)
print(titles.status_code)
soup=BeautifulSoup(titles.text,'html.parser')
titless=soup.findAll('h2',attr={'class':'title'})
for i in titless:
    print(i.string)