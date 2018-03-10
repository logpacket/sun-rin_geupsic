#-*- coding: utf-8 -*-
from flask import Flask, request
import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.sunrint.hs.kr/index.do')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
menu = soup.select(' dl > dd > p.menu')
def today_menu():
    today = menu[0].text
    print(today)
    return today
def tomorrow_menu():
    tomorrow = menu[1].text
    return tomorrow

application = Flask(__name__)
@application.route('/keyboard')
def keyboard():
    key = '{"type":"buttons", "buttons":["오늘의 급식", "내일의 급식"]}'
    return key
@application.route('/message',methods=['POST','GET'])
def message():
    if request.method == "POST":
        select = request.get_json()
        if select.content == '오늘의 급식':
            menu = today_menu()
            return menu
        elif select.content == '내일의 급식':
            menu = tomorrow_menu()
            return menu
if __name__ == '__main__':
    application.run(host='0.0.0.0')