from flask import Flask
from flask import request
#建立Application 物件

app = Flask(
    __name__,
    static_folder='static',#設定靜態檔案資料夾名稱
    static_url_path='/abc' #設定靜態檔案網址路徑,也可設定為'/'
      ) 

#所有在static資料夾底下的檔案，網址會對應到/abc/檔案名稱

#建立網站首頁
@app.route('/')
#用來回應網站首頁連線的函式
def index():
    
    #print('請求方法',request.method) #物件屬性
    #print('通訊協定',request.scheme)
    #print('主機名稱',request.host)
    #print('路徑',request.path)
    #print('完整的網址',request.url)

    #print('瀏覽器和作業系統',request.headers.get('user-agent'))
    #print('語言偏好',request.headers.get('accept-language'))
    #print('引薦網址',request.headers.get('r'))


    
    return 'Hi' #回傳網站首頁的內容

@app.route('/hi'+'/<name>')
def hi(name):
    return f'Hi,{name}'

#啟動伺服器
app.run() 