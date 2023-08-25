"""
用python網路連線，並抓取"台北市政府公開"資料

========================================
網路連線
========================================
載入模組：
import urllib.request  #如果想用python連網就用這個內建模組

下載特定網址資料：                           #跟檔案操作語法很像
import urllib.request as request
with request.urlopen(src) as response:    #src是網址:http那個  #會產出一個物件給他名字叫response (response 這個變數裡面放物件)
    data=response.read()                  #使用read來讀取此網頁資料（一次就會把所有資料讀進來）
print(data)

---------（#連線到台大網站後，那個網頁的一堆東西會是一個物件，我將這個物件使用read功能（東西讀取下來存到data這個變數））---------


========================================
公開資料：
========================================
適合資料來源：
（這邊以台北市政府公開資料舉例）

確認資料格式：
json,csv,其他格式

解讀json格式:
使用內建的json模組

"""


# 網路連線
import urllib.request as request  # 使用python連網的套件 url是網址的意思，request是要求

src = "https://www.ntu.edu.tw"
with request.urlopen(src) as response:  # url+open 網址＋打開   （#想連線到台大網站 ）
    data = response.read()
    data = response.read().decode("utf-8")  # 想看中文打這個
print(data)  # 跑出來是台大網頁的html原始碼


# 串接,擷取公開資料     #api就是讓我們用程式連線去自動下載
import urllib.request as request
import json  # 發現是json格式因此用json套件

src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)  # 利用 json 模組處理 json 資料格式
print(data)
# ==================================可以跑，只是有點久==============================================


# 將公司名稱列表出來（抓到一堆東西沒意義，要解讀資料的欄位，要一個抓出來）
clist = data["result"]["results"]  # 此寫法只要是json大多都這樣(要看資料狀況)
print(clist)
for company in clist:
    print(company["公司名稱"])  #'公司名稱'(key): '台灣華協企業有限公司'(value)
"""
圓藝企業股份有限公司
合全產品開發股份有限公司
馭航股份有限公司
典業有限公司
國眾電腦股份有限公司
網上穿越有限公司
"""


# 將抓出資料裝進檔案中
"""
流程1:使用網路模組
流程2:連線到台大網站
流程3:使用語法抓下來read or load
流程4:抓整團資料沒意義，需要使用python的dic功能，我希望我打key會跑出value
流程5:先開啟檔案，再迴圈寫進去我需要的部分

"""
import urllib.request as request
import json

src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)

clist = data["result"]["results"]  # 觀察資料是result 對 results列表
with open("data0825.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")


"""
Q1:
如果想顯示更多：

ans:
在API最後面加上&limit=1000
如：
https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire
更改為：
https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire&limit=1000
"""

"""
Q2:
老師您好
我在嘗試抓取公開資料時，出現錯誤顯示“urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1002)>” 
不確定是不是我的漏了什麼，我看了好幾次....

ans:
如果你使用 Mac 電腦的話，在程式最前面加上以下兩行試試看：
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

成功了 感謝！！！


Q3:
想請問一下老師中間有放入的clist=data["result"]["results"]
這一個作法，在變數data後面放入兩個[][]
這一段用法算是甚麼意思呢~? 
他有沒有一個比較專門的名詞之類的~? 
是專屬於json格式的資料有兩層才這樣做帶入嗎?? 

ans:
只是基本的字典用法而已，JSON 中的大括號在 Python 裡會被詮釋成字典。


"""


"""

#網路連線
import urllib.request as request
src="https://www.ntu.edu.tw"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8") #取得台大網站的原始碼(HTML,CSS,JS)
print(data)

# 串接截取公開資料
import urllib.request as request
import json
src="http://117.56.59.17/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
with request.urlopen(src) as response:
     data=json.load(response) #利用json模組處理 json 模組處理 json資料格式
print(data) 


import urllib.request as request
import json
src="http://117.56.59.17/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組讀取資料
#取得觀測站名稱, 並寫入檔案(weather.txt)
slist=data["data"]
with open("weather.txt","w", encoding="utf=8") as file:
    for name in slist:
        file.write(name["stationName"]+"\n")


"""


"""
有寫跟沒寫clist = data["result"]["results"]  差別
原始：

'addr_x': '306842', 'addr_y': '2774995'}]}}

新：

'addr_x': '306842', 'addr_y': '2774995'}]

差別在最後兩個括號
"""
