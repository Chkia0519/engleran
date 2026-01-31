#bs4爬蟲
import requests
from bs4 import BeautifulSoup

def eveW():
    url = 'https://cdict.info/'

    header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        'cookie':'ApplicationGatewayAffinityCORS=48282c56c1ae4f832cf8984ca6ed81e0; ApplicationGatewayAffinity=48282c56c1ae4f832cf8984ca6ed81e0; _ga=GA1.3.894321893.1768134822; _gid=GA1.3.1608134897.1768134822; _ga_E18C7TBS4E=GS2.3.s1768134822$o1$g1$t1768135763$j54$l0$h0'                          
    }


    urls = requests.get(url,headers=header)
    urls.encoding = 'utf-8'
    urls=urls.text

    soup = BeautifulSoup(urls,'html.parser')

    en = soup.find('h5').text #英文

    exps = soup.find(class_='content-data').get_text(separator="\n",strip=True)
    #exps = exps.replace(en,'')

    return(en,exps)

    #print(exps)