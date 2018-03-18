#-*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')

key = '"keyboard":{"type":"buttons", "buttons":["오늘의 급식", "내일의 급식"]}}'
output_date = []
def create_form(menu):
    menu = menu.replace('\n', '')
    menu = menu.replace('\r', '')
    menu = menu.replace('\t', '')
    menu = menu.replace(' ', '')
    menu = menu.replace(',', '\\n')
    menu = menu.replace('(', '\\n')
    menu = menu.replace(')', '')
    message = '{"message":{"text":' + '\"'+ menu + '\"' + '}' + ',' + key
    return message

def check_day():
    date = soup.select('dl > dd > p.date')
    to_day = datetime.today()
    to_day = str(to_day)
    to_day = to_day[8:10]
    date_list = []
    for day in date:
        output_date.append(day.text)
        date_list.append(day.text[8:10])
    if to_day in date_list :
        return 1;
    else :
        today.write('{"message":{"text":' + '\"' + '오늘 급식이 없습니다!' + '\"' + '}' + ',' + key)
        to_day = int(to_day)
        to_day += 1
        tomorrow_day = str(to_day)
        if tomorrow_day != date_list[0]:
            tomorrow.write('{"message":{"text":' + '\"' + '내일 급식이 없습니다!' + '\"' + '}' + ',' + key)
            sys.exit()
        else :
            tomorrow.write(create_form(output_date[0] +'\\n\\n'+ menu[0].text))
            sys.exit()            

today = open("/home/packet/sun-rin_geupsic/today", "w")
tomorrow = open("/home/packet/sun-rin_geupsic/tomorrow", "w")
req = requests.get('http://www.sunrint.hs.kr/index.do')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
menu = soup.select(' dl > dd > p.menu')

check_day()
today.write(create_form(output_date[0] + '\\n\\nn' + menu[0].text))
tomorrow.write(create_form(output_date[1] + '\\n\\n' + menu[1].text))
