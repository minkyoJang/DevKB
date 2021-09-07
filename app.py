# app.py

from flask import Flask, render_template, send_file
import save
import time


# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')

@app.route('/export') # 접속하는 url
def export():
    # from save import save_to_file 또는 from save import * 로 하고 기존에 작성한것처럼 함수를 save_to_file() 이렇게 해도 동작은 문제 없으나 코드 작성시 헷갈려서 실수 가능성이 있음. 그래서 "모듈.클래스" 이렇게 작성하는것이 편함. 실제로 아래 time도 from time import * 으로 사용하면 str(strftime...) 이런식으로 사용가능한데, 너무 길거나 반복이 많은경우에만 from을 사용하는것이 좋음(내피셜). 인터넷도 찾아보면 사람마다 from로 해서 줄인사람도 있고, import로 해서 모듈까지 다 쓴것 있는데, 모듈마다 특성들이 있어서 인터넷에 자주쓰는거로 하면됨. 공식 코드작성가이드 pep참고 https://cuorej.tistory.com/entry/pep8-import-%EC%8A%A4%ED%83%80%EC%9D%BC-%EA%B0%80%EC%9D%B4%EB%93%9C
    # 참고로 위의 글이 길어서 안보이면 vscode 단축키 Alz + Z 를 사용할것
    save.save_to_file()
    FN= str(time.strftime("%Y%m%d"))+".csv"
    return send_file(FN,mimetype='application/x-csv',attachment_filename = FN, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

    # host 등을 직접 지정하고 싶다면
    # app.run(host = "127.0.0.1", port = "5000", debug = True)