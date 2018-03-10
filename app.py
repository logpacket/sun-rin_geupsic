from flask import Flask, request
import parser

application = Flask(__name__)
@application.route('/keyboard')
def keyboard():
    key = '{"type":"buttons", "buttons":["오늘의 급식", "내일의 급식"]}'
    return key
@application.route('/message')
def message():
    if request.method == "POST":
        select = request.form["button"]
        if select == "오늘의 급식":
            menu = parser.today_menu()
            return menu
        elif select == "내일의 급식":
            menu = parser.tomorrow_menu()
            return menu
if __name__ == '__main__':
    application.run(host='0.0.0.0')
