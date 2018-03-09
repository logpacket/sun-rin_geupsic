from flask import Flask, request
import parser

app = Flask(__name__)
@app.route('/keyboard')
def keyboard():
    key = '{"type":"buttons", "buttons":["오늘의 급식", "내일의 급식"]}'
    return key
@app.route('/message')
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
    app.run()
