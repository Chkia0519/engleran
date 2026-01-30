from db import db
import random

#顯示全部字卡
def loadwd():
    cursor = db.mydb.cursor()
    cursor.execute("SELECT en, cn ,typ ,pracTimes ,correctTimes ,lotime FROM learnword")
    rows = cursor.fetchall()
    cursor.close()

    return(rows)

#use eg.
# for en, cn ,typ ,pts ,cts ,tim in loadwd():
#     print(en, cn, typ ,pts ,cts ,tim)

#隨機挑數個字卡
def random_words(n=5):
    cursor = db.mydb.cursor()
    cursor.execute("SELECT en, cn ,typ FROM learnword")
    rows = cursor.fetchall()
    cursor.close()
    return random.sample(rows, n)

#use eg.
# for en, cn ,typ in random_words(3):
#     print(en, cn, typ)


#隨機挑1個字卡及顯示他的練習次數 直接從SQL裡面下RAND會比較快(原本是用先全抓下來再random.choice)
def get_random_word():
    cursor = db.mydb.cursor()
    cursor.execute("""
            SELECT en, cn, pracTimes, correctTimes
            FROM learnword
            ORDER BY RAND()
            LIMIT 1
             """)
    word = cursor.fetchone()
    cursor.close()
    return word

#use eg.
# en, cn, pts, cts = get_random_word()
# print(en, cn, pts, cts)


#更新練習次數並顯示已經練習幾次
def update_prac_times(enword):
    cursor = db.mydb.cursor()
    cursor.execute("UPDATE learnword SET pracTimes = pracTimes + 1 WHERE en = %s", (enword,))
    db.mydb.commit()

    cursor.execute("SELECT pracTimes FROM learnword WHERE en = %s", (enword,))
    tims = cursor.fetchone()[0]  # 取出第一列的第一個欄位值

    cursor.close()

    return(tims)

#use eg.
# tims = update_prac_times('none')
# print(tims)


#答案正確就正確+1
def update_correct_times(enword):
    cursor = db.mydb.cursor()
    cursor.execute("UPDATE learnword SET correctTimes = correctTimes + 1 WHERE en = %s",(enword,))
    db.mydb.commit()
    cursor.close()

#已經答對的次數
def get_correct_times(enword):
    cursor = db.mydb.cursor()
    cursor.execute("SELECT correctTimes FROM learnword WHERE en = %s", (enword,))
    tims = cursor.fetchone()[0]  # 取出第一列的第一個欄位值
    db.mydb.commit()
    cursor.close()
    return(tims)

#use eg.
# tims = get_correct_times('none')
# print(tims)


#整合抽字卡和更新次數 -還沒改好-
def practice_word(en, cn, ans):
<<<<<<< HEAD
    # #使用get_random_word()來抽一張字卡
    # en, cn, pts, cts = get_random_word() 放裡面會再次重抽 邏輯錯誤
=======
    
    # 使用get_random_word()來抽一張字卡 會重複抽導致答案和題目錯亂，寫在函式外會更好
    # en, cn, pts, cts = get_random_word()

    # print("請輸入英文單字：")
    # print(f"中文：{cn}")
>>>>>>> c69262c4cae4eeceecd4cd627fa61ba9816fce5c

    #只要有練習就在練習次數+1
    prac_add = update_prac_times(en)
    

    #答案正確就在正確+1
    correct = ans.strip().lower() == en.strip().lower() #大小寫跟空白忽略

    if correct:
<<<<<<< HEAD
        update_correct_times(en)
        #print('恭喜答對!')
=======
        now_cts = update_correct_times(en) #now_cts->抓取最新的正確次數
        print('恭喜答對!')
    else:
        now_cts = update_correct_times(en) #now_cts->抓取最新的正確次數
>>>>>>> c69262c4cae4eeceecd4cd627fa61ba9816fce5c

    # else:
        #print(f'正確答案是：{en}')

<<<<<<< HEAD
    #print(f"這個單字已練習 {prac_add} 次")

=======
    #改字典比較好維護
>>>>>>> c69262c4cae4eeceecd4cd627fa61ba9816fce5c
    return {
        "en": en,
        "cn": cn,
        "answer": ans,
        "correct": correct,
        "pracTimes": prac_add
    }


# en, cn, _, _ = get_random_word()
# print(f"中文：{cn}")
# answer = input("請輸入英文單字：")

# practice_word(en, cn, answer)