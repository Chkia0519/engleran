from flask import Flask, request, session ,render_template
from db import db,word_indb
from datetime import datetime
from fire import eveW
from getentocn import getentocn
from read import *
<<<<<<< HEAD
=======

>>>>>>> c69262c4cae4eeceecd4cd627fa61ba9816fce5c
#import os

app = Flask(__name__)
app.secret_key = "learn-secret-key" 

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

            tips = (f'很棒!學習了一個新的單字! {learnW},{cnW}')

            today = datetime.today()
            tdtime = today.strftime('%Y-%m-%d')

            cursor = db.mydb.cursor()
            sql = "INSERT INTO learnword(en, cn, typ, likeW, pracTimes, correctTimes, lotime) VALUES (%s, %s, %s, 0, 0, 0, %s)"
            cursor.execute(sql, (learnW, cnW, word_type, tdtime))
            db.mydb.commit()
            cursor.close()

            return render_template('mylearnwords.html',tips=tips)
    else:
        tips = '請輸入單字！'
        return render_template('mylearnwords.html', tips=tips)

#英翻中
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
    
<<<<<<< HEAD
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
=======
#抽字卡練習
@app.route('/read', methods=['GET', 'POST'])
def readword():
    #第一次進去是GET
    if request.method == 'GET':
        session['total'] = 0
        session['correct'] = 0

        en, cn, _, _ = get_random_word()
        return render_template(
            "read.html",
            learnW=en,
            cnW=cn,
            last_correct=None,
            last_answer=None,
            total=session['total'],
            correct=session['correct'],
            show=False #不顯示答題正確及錯誤
        )
    
    #使用者輸入答案
    ans = request.form.get('Ans')
    en = request.form.get('en')
    cn = request.form.get('cn')

    result = practice_word(en, cn, ans)
>>>>>>> c69262c4cae4eeceecd4cd627fa61ba9816fce5c

    #使用 session 紀錄狀態 
    session['total'] += 1
    if result["correct"]:
        session['correct'] += 1

    # 如要繼續就抽下一題
    next_en, next_cn, _, _ = get_random_word()

    return render_template(
        "read.html",
        learnW=next_en,
        cnW=next_cn,
        last_correct=result["correct"],
        last_answer=result["en"],
        pracTimes=result["pracTimes"],
        total=session['total'],
        correct=session['correct'],
        show=True
    )

#結束練習
@app.route('/end_practice')
def end_practice():
    total = session.get('total', 0)
    correct = session.get('correct', 0)
    #正確率
    accuracy = round((correct / total) * 100, 2) if total > 0 else 0

    return render_template(
        "result.html",
        total=total,
        correct=correct,
        accuracy=accuracy
    )

#顯示全部資料
@app.route('/all_words')
def all_words():
    total = session.get('total', 0)
    correct = session.get('correct', 0)
    #正確率
    accuracy = round((correct / total) * 100, 2) if total > 0 else 0

    return render_template(
        "allwords.html",
        total=total,
        correct=correct,
        accuracy=accuracy
    )
if __name__ == "__main__":
    app.run(debug=True)