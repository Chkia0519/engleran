from flask import Flask, request, jsonify ,render_template
from db import db,word_indb
from datetime import datetime
from fire import eveW
from getentocn import getentocn
from read import *
#import os

app = Flask(__name__)

#首頁
@app.route('/')
def index():
    #每日一詞
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
            learnW = learnW.lower()
            cnW = request.form.get('cnW')
            word_type = request.form.get('word_type')

            today = datetime.today()
            tdtime = today.strftime('%Y-%m-%d')

            cursor = db.mydb.cursor()
            sql = "INSERT INTO learnword(en, cn, typ, likeW, pracTimes, correctTimes, lotime) VALUES (%s, %s, %s, 0, 0, 0, %s)"
            cursor.execute(sql, (learnW, cnW, word_type, tdtime))
            db.mydb.commit()
            cursor.close()

            return render_template('addwords.html',learnW=learnW,cnW=cnW)
    else:
        tips = '請輸入單字！'
        return render_template('mylearnwords.html', tips=tips)

#中翻英
@app.route('/entocn',methods=['GET','POST'])
def etc():
    enW = request.form.get('enW')
    
    if enW and enW.strip():  # 確保不是 None 或空字串
        word = getentocn(enW)
        print(word,enW)
        return render_template('entocn.html', word=word ,enW=enW)
    
    else:
        tips = '請輸入單字！'
        return render_template('entocn.html',tips=tips)
    
#還沒好
@app.route('/read',methods=['GET','POST'])
def readword():
    #第一次get
    if request.method == 'GET':
        en, cn, _, _ = get_random_word()
        return render_template(
            "addwords.html",
            learnW=en,
            cnW=cn,
            correct=None
        )
    #使用者post
    ans = request.form.get('Ans')
    en = request.form.get('en')
    cn = request.form.get('cn')

    result = practice_word(en, cn, ans)

    return render_template(
        "addwords.html",
        learnW=result["en"],
        cnW=result["cn"],
        correct=result["correct"],
        pracTimes=result["pracTimes"]
    )

if __name__ == "__main__":
    app.run(debug=True)