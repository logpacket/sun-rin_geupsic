#-*- coding: utf-8 -*-
from flask import Flask, request
import requests
from bs4 import BeautifulSoup
def parse():
    req = requests.get('http://www.sunrint.hs.kr/index.do')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    menu = soup.select(' dl > dd > p.menu')
    return menu
def today_menu():
    menu = parse()
    today = menu[0].text
    return today
def tomorrow_menu():
    menu = parse()
    tomorrow = menu[1].text
    return tomorrow

application = Flask(__name__)
@application.route('/keyboard')
def keyboard():
    key = '{"type":"buttons", "buttons":["오늘의 급식", "내일의 급식"]}'
    return key
@application.route('/message',methods=['POST'])
def message():
    if request.method == "POST":
        select = request.get_json()
        key = '"keyboard":{"type":"buttons", "buttons":["오늘의 급식", "내일의 급식"]}}'
        if select['content'] == '오늘의 급식':
            menu = today_menu()
            menu = menu.replace('\n', '')
            menu = menu.replace('\r', '')
            menu = menu.replace('\t', '')
            menu = menu.replace(' ', '')
            menu = menu.replace(',', '\\n')
            menu = menu.replace('(', '\\n')
            menu = menu.replace(')', '')
            message = '{"message":{"text":' + '\"' + menu + '\"'+'}' + ',' + key
            return message
        elif select['content'] == '내일의 급식':
            menu = tomorrow_menu()
            menu = menu.replace('\n', '')
            menu = menu.replace('\r', '')
            menu = menu.replace('\t', '')
            menu = menu.replace(' ', '')
            menu = menu.replace(',', '\\n')
            menu = menu.replace('(', '\\n')
            menu = menu.replace(')', '')
            message = '{"message":{"text":' + '\"' + menu + '\"'+'}' + ',' + key
            return message
if __name__ == '__main__':
    application.run(host='0.0.0.0')



