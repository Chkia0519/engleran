from flask import Flask, request, jsonify ,render_template
from db import db
from datetime import datetime
#import os

app = Flask(__name__)



#輸入單字卡
@app.route('/mylearnwords',methods=['GET','POST'])
def index():

    learnW = request.form.get('lenW')
    cnW = request.form.get('cnW')
    word_type = request.form.get('word_type')

    today = datetime.today()
    tdtime = today.strftime('%Y-%m-%d')

    print(learnW,cnW,word_type,tdtime)
    
    cursor = db.mydb.cursor()
    sql = "insert into learnword(en,cn,typ,likeW,pracTimes,lotime) values('{}','{}','{}', 0 ,0,'{}')".format(learnW,cnW,word_type,tdtime)                   
    cursor.execute(sql)
    db.mydb.commit()
    cursor.close()

    return render_template('mylearnwords.html')


@app.route('/mywords',methods=['GET','POST'])
def learnWord():
    # 預設值，避免缺值或 UnboundLocalError
    learnW = ""
    cnW = ""
    word_type = ""

    if request.method == 'GET':
        learnW = request.args.get('lenW')
        cnW = request.args.get('cnW')
        word_type = request.args.get('word_type')

    else:
        data = request.get_json(silent=True)
        learnW = (data.get('lenW') if data else request.form.get('lenW') or "").strip()
        cnW = (data.get('cnW') if data else request.form.get('cnW') or "").strip()
        word_type = (data.get('word_type') if data else request.form.get('word_type') or "").strip()

    if not learnW:
        # 後端回傳錯誤，前端可顯示「尚未輸入文字」
        return jsonify({"error": "尚未輸入文字"}), 400

    return jsonify({"lenW": learnW,'cnW':cnW,'word_type':word_type}), 200
# ...existing code...    

if __name__ == "__main__":
    app.run(debug=True)