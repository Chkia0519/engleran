import requests
from bs4 import BeautifulSoup
import db

cursor = db.mydb.cursor()

url = 'https://www.englishok.com.tw/category/learning/english-vocabulary'

header = {
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'cookie':'ApplicationGatewayAffinityCORS=48282c56c1ae4f832cf8984ca6ed81e0; ApplicationGatewayAffinity=48282c56c1ae4f832cf8984ca6ed81e0; _ga=GA1.3.894321893.1768134822; _gid=GA1.3.1608134897.1768134822; _ga_E18C7TBS4E=GS2.3.s1768134822$o1$g1$t1768135763$j54$l0$h0'                          
}

urls = requests.get(url,headers=header)
urls.encoding = 'utf-8'
urls=urls.text

soup = BeautifulSoup(urls,'html.parser')

words = soup.find_all('h2',class_='entry-title')
exps = soup.find_all(class_='entry-content')

for w,n in zip(words,exps):

    word = w.text
    cnword = word.split()[0]
    enword = word.split()[1]
    #print(cnword)
    #print(enword)

    exp = n.text
    sam = exp.split('\r\n')

    clean = [line.strip() for line in exp.split('\r\n') if line.strip() != '']

    #print(clean)
    typ = clean[0]
    lik = clean[1][4:]
    #print(typ,lik)


    #print(repr(exp))
    #print(sam)
    sql = "insert into nword(en,cn,typ,likeW) values('{}','{}','{}','{}')".format(enword,cnword,typ,lik)                   
    cursor.execute(sql)
    db.mydb.commit()

    
db.mydb.close()