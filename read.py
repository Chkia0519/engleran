from db import db
import random

#顯示全部字卡
def loadwd():
    cursor = db.mydb.cursor()
    cursor.execute("SELECT en, cn ,typ FROM learnword")
    rows = cursor.fetchall()
    cursor.close()

    return(rows)

#use eg.
# for en, cn ,typ in loadwd():
#     print(en, cn, typ)

#隨機挑字卡
def random_words(n=5):
    cursor = db.mydb.cursor()
    cursor.execute("SELECT en, cn ,typ FROM learnword")
    rows = cursor.fetchall()
    cursor.close()
    return random.sample(rows, n)

#use eg.
# for en, cn ,typ in random_words(3):
#     print(en, cn, typ)


import pymysql
import random

db = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_db",
    charset="utf8mb4"
)

def get_random_word():
    cursor = db.cursor()
    cursor.execute("SELECT id, en, cn, pracTimes FROM learnword")
    rows = cursor.fetchall()
    cursor.close()
    return random.choice(rows)

def update_prac_times(word_id):
    cursor = db.cursor()
    cursor.execute("UPDATE learnword SET pracTimes = pracTimes + 1 WHERE id = %s", (word_id,))
    db.commit()
    cursor.close()

