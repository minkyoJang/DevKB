# app.py
import time
from flask import Flask, render_template, send_file, request

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST']) # 접속하는 url
def post():
    value1 = request.form['userInput1']
    value2 = request.form['userInput2']

    FN = str(value1)+"-"+str(value2) +".csv"
    
    with open(FN,mode = 'w') as f:
        f.write("Hellow-World")
    
    return send_file(FN,mimetype='application/x-csv',attachment_filename = FN, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

    # host 등을 직접 지정하고 싶다면
    # app.run(host = "127.0.0.1", port = "5000", debug = True)

