import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.sunrint.hs.kr/index.do')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
menu = soup.select(' dl > dd > p.menu')
sort = []
for txt in menu:
    sort.append(txt.text)
def today_menu():
    today = sort[0].split()
    today = today[0].split(',')
    return today

def tomorrow_menu():
    tomorrow = sort[1].split()
    tomorrow = tomorrow[0].split(',')
    return tomorrow