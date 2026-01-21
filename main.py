from flask import Flask, request, jsonify ,render_template
from db import db,word_indb
from datetime import datetime
from fire import eveW

#import os

app = Flask(__name__)

@app.route('/')
def index():
    en,exps = eveW()
    return render_template('index.html',en=en,exps=exps)

#輸入單字卡
@app.route('/mylearnwords',methods=['GET','POST'])
def mylearnwords():

    learnW = request.form.get('lenW')

    if learnW and learnW.strip():  # 確保不是 None 或空字串

        if word_indb(learnW):
            tips = '這個單字已經存過囉!'
            return render_template('mylearnwords.html', tips=tips)
        else:
            cnW = request.form.get('cnW')
            word_type = request.form.get('word_type')

            today = datetime.today()
            tdtime = today.strftime('%Y-%m-%d')

            cursor = db.mydb.cursor()
            sql = "INSERT INTO learnword(en, cn, typ, likeW, pracTimes, lotime) VALUES (%s, %s, %s, 0, 0, %s)"
            cursor.execute(sql, (learnW, cnW, word_type, tdtime))
            db.mydb.commit()
            cursor.close()

            return render_template('mylearnwords.html')
    else:
        tips = '請輸入單字！'
        return render_template('mylearnwords.html', tips=tips)


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