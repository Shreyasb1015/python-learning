import requests
from bs4 import BeautifulSoup


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage=requests.get('https://www.lifewire.com/most-popular-sites-3483140',headers=headers).text


bs=BeautifulSoup(webpage,'html.parser')

urls=bs.find_all('a')

for url in urls:
    print(url.get('href'))
