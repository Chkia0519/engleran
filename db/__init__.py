#用於檢查單字是否已存在於單字本內
def word_indb(word):
    cursor = db.mydb.cursor()
    sql = "SELECT COUNT(*) FROM learnword WHERE en = %s"
    cursor.execute(sql, (word,))
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0