#bs4爬蟲
import requests
from bs4 import BeautifulSoup

def getentocn(word):
    url = 'https://cdict.info/query/'

    header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        'cookie':'ApplicationGatewayAffinityCORS=48282c56c1ae4f832cf8984ca6ed81e0; ApplicationGatewayAffinity=48282c56c1ae4f832cf8984ca6ed81e0; _ga=GA1.3.894321893.1768134822; _gid=GA1.3.1608134897.1768134822; _ga_E18C7TBS4E=GS2.3.s1768134822$o1$g1$t1768135763$j54$l0$h0'                          
    }

    #word = 'egg' #input('請輸入英文：')
    url += word
    print(url)
    urls = requests.get(url,headers=header)
    urls.encoding = 'utf-8'
    urls=urls.text

    soup = BeautifulSoup(urls,'html.parser')
    print(soup)
    cl = soup.find(class_='content-data')
    p=cl.find('p')
    text = p.get_text(separator="\n",strip=True)

    return text if text else "查無結果"



# text = getentocn('sop')
# print(text)