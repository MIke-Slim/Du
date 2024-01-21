import requests
from bs4 import BeautifulSoup
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

for i in range(0,250,25):
    response=requests.get(f'https://movie.douban.com/top250?start={i}',headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    titles=soup.findAll('span',attrs={'class':'title'})
    for title in titles:
        
        if '/' not  in title.string:
            print(title.string)
            

