#bs4爬蟲 暫不使用
import requests
from bs4 import BeautifulSoup

#def getentocn(word):
url = 'https://cdict.info/query/'

header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'cookie':'ApplicationGatewayAffinityCORS=48282c56c1ae4f832cf8984ca6ed81e0; ApplicationGatewayAffinity=48282c56c1ae4f832cf8984ca6ed81e0; _ga=GA1.3.894321893.1768134822; _gid=GA1.3.1608134897.1768134822; _ga_E18C7TBS4E=GS2.3.s1768134822$o1$g1$t1768135763$j54$l0$h0'                          
}

word = '安' #input('請輸入英文：')
url += word
print(url)
urls = requests.get(url,headers=header)
urls.encoding = 'utf-8'
urls=urls.text

soup = BeautifulSoup(urls,'html.parser')

print(soup)
cl = soup.find(class_='resultbox')

for unwanted in cl.find_all(class_=["bartop", "xbox"]):
    unwanted.decompose()

print(cl.get_text(strip=True))

# p=cl.find('p')
# if p :
#     text = p.get_text(separator="\n",strip=True)
#     print(text)
# else:
#     print('找不到相關資料')


