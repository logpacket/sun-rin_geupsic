import requests
from bs4 import BeautifulSoup

key = '"keyboard":{"type":"buttons", "buttons":["오늘의 급식", "내일의 급식"]}}'
def create_form(menu):
    menu = menu.replace('\n', '')
    menu = menu.replace('\r', '')
    menu = menu.replace('\t', '')
    menu = menu.replace(' ', '')
    menu = menu.replace(',', '\\n')
    menu = menu.replace('(', '\\n')
    menu = menu.replace(')', '')
    message = '{"message":{"text":' + '\"' + menu + '\"' + '}' + ',' + key
    return message
today = open("./today", "w")
tomorrow = open("./tomorrow", "w")
req = requests.get('http://www.sunrint.hs.kr/index.do')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
menu = soup.select(' dl > dd > p.menu')

print(create_form(menu[0].text))
today.write(create_form(menu[0].text))
tomorrow.write(create_form(menu[1].text))
