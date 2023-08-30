"""
網路爬蟲 web crawler基本篇

基本流程：
1.連線到特定網址，抓取資料
2.解析資料，取得實際想要部分


=============================================================================================
抓取資料：
=============================================================================================
關鍵心法
盡可能地，讓程式模仿一個普通使用者的樣子


=============================================================================================
解析資料：
=============================================================================================
json格式資料：使用內建的json模組即可

html格式資料(以標籤為運作單位) 標籤有開頭有結束
<html>
    <head>                          標籤有開頭有結束
        <title>HTML格式</title>
    <head>                          標籤有結束
    <body>
        <div class="list">          標籤的屬性叫class
            <span>階層結構</span>
            <span>樹狀結構</span>
        <div>
    <body>
<html>


html格式資料：使用第三方套件 BeautifulSoup來做解析


=============================================================================================
安裝套件：
=============================================================================================
PIP套件管理工具：安裝python時，就一起安裝在你的電腦裡

利用pip工具，安裝第三方套件BeautifulSoup:
pip install beautifulsoup4

"""

"""
要做網路爬蟲，要先觀察我們要抓的網頁
先打開網頁看個

目標：
ptt有許多文章，每篇文章都有標題
我們希望用程式取抓標題資料

流程1：
觀察網址：html

流程2：
點右鍵 ==> 檢視網頁原始碼


"""

# =============================================================================================
# 抓取 ptt 電影版的網頁原始碼 (html)
# =============================================================================================
# import urllib.request as req

# url = "https://www.ptt.cc/bbs/movie/index.html"
# with req.urlopen(url) as response:
#     data = response.read().decode("utf-8")
# print(data)

# 最後一行會跳出：
# urllib.error.HTTPError: HTTP Error 403: Forbidden
"""
連線被拒絕：因為我的程式不像正常使用者連線
"""
"""
解法：要讓自己的連線像一般的使用者

解法邏輯：
流程1：去 ptt 電影版頁面 => 三個小點 => 更多工具 => 開發人員工具 
流程2：在 Network 情況下，選 all ，重新整理網頁                 (network 網路監控工具)
流程3：點 index.html ，會看到三個大標                          (為了要將網頁顯示出來，做了許多網路連線，我們觀察的是這個網頁本身)
流程4：選 Headers 裡面選 Request Heaaders                    (用瀏覽器發送網路連線到ptt伺服器，會附加許多資訊，代表我們是正常使用者)                      (Request Headers 就是一般使用者做連線時 會發送的資訊 我們必須讓我們的程式也發送這類的訊息 ptt就會認為我們是正常的使用者 )
流程5：看到 User-Agent: ，將一大串複製                         (Mozilla/5.0 (Macintosh; Intel Mac OS X...)                                       (代表我們今天使用的是 怎樣的作業系統 怎樣的瀏覽器)
流程6：貼到 req.Request(url,headers={ "User-Agent":"這裡"}
流程7：
"""

import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個 request 物件，附加 Request Heaaders 的資訊                   (我感覺就是升級版的網址，可以在網址旁邊再塞東西)
request = req.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    },
)
with req.urlopen(request) as response:  # 不要給網址，請給物件
    data = response.read().decode("utf-8")
# print(data)  # 得到 ptt 電影版 html 網頁原始碼


# 我們的目標是 ptt 電影版文章標題
# 但我們爬下來是網頁原始碼（難以判讀）

"""
		<div class="r-ent">
			<div class="nrec"><span class="hl f3">47</span></div>
			<div class="title">
			
				<a href="/bbs/movie/M.1693240050.A.312.html">[情報] 最近 DC 電影的預算與票房數據</a>
			
			</div>
			<div class="meta">
				<div class="author">godofsex</div>
				<div class="article-menu">
					
					<div class="trigger">&#x22ef;</div>
					<div class="dropdown">
						<div class="item"><a href="/bbs/movie/search?q=thread%3A%5B%E6%83%85%E5%A0%B1%5D&#43;%E6%9C%80%E8%BF%91&#43;DC&#43;%E9%9B%BB%E5%BD%B1%E7%9A%84%E9%A0%90%E7%AE%97%E8%88%87%E7%A5%A8%E6%88%BF%E6%95%B8%E6%93%9A">搜尋同標題文章</a></div>
						
						<div class="item"><a href="/bbs/movie/search?q=author%3Agodofsex">搜尋看板內 godofsex 的文章</a></div>
						
					</div>
					
				</div>
				<div class="date"> 8/29</div>
				<div class="mark"></div>
			</div>
		</div>


我們想要的只有 “[情報] 最近 DC 電影的預算與票房數據”
"""


# =============================================================================================
# 解析原始碼，取得每篇文章的標題
# =============================================================================================

import bs4

# data是剛剛從ptt電影版抓下來的網頁原始碼，丟給 beautifulsoup 他會幫我們解析 html 格式文件
root = bs4.BeautifulSoup(data, "html.parser")
# print(root.title)
"""root代表整份網頁，title是標題 （一個網頁的標籤）     <title>看板 movie 文章列表 - 批踢踢實業坊</title>
 會抓到整份網頁的 title 裡面的文字"""
# print(root.title.string)  # if 我想要 title 裡的文字但不要 title


# 我們真正的目標是文章的標題，點入網頁原始碼看，觀察特殊之處
"""
			<div class="title">
			
				<a href="/bbs/movie/M.1693362505.A.165.html">Re: [討論] 讓子彈飛 兩碗涼粉的局要怎麼破？</a>
			
			</div>

"""
# 我們發現每一篇文章標題都被 a 標籤包裹，再被 div 標籤包裹

titles = root.find("div", class_="title")  # 尋找 class="title" 的 div 標籤

titles = root.find_all(
    "div", class_="title"
)  # 尋找所有 class="title" 的 div 標籤，會得到一個列表（有一個中括號）

"""
beautifulsoup 給我們許多工具使用，叫 find
從網頁中尋找標籤，我要的標籤叫 div ，
給一些篩選條件class_叫"title"

用一個 find 表示要找的標籤名稱，篩選條件
"""

# print(titles)
"""得到：
<div class="title">
<a href="/bbs/movie/M.1693362505.A.165.html">Re: [討論] 讓子彈飛 兩碗涼粉的局要怎麼破？</a>
</div>
"""

# print(titles.a.string)
# titles 代表 div ， .a 代表頭尾的 “<a href=“ ”</a>”， .string 代表“[討論] 讓子彈飛 兩碗涼粉的局要怎麼破？”


# 把 ptt 電影版頁面中每個標題一次抓出，並印出
for title in titles:
    if title != None:  # 如果標題包含 a 標籤（被刪除的文章沒有 a 標籤），印出來
        print(title.a.string)


# 統整
"""
我們想抓取資料，解析資料
抓取資料有個難題，我們要讓自己的程式，看起來像一般使用者
其中最關鍵的是，要在我們的要求(request)中設定 headers
最重要的設定叫 "User-Agent"，會讓對方知道我們使用什麼瀏覽器，什麼作業系統
這樣ptt伺服器會認為我們是一個正常使用者
我們就會抓到資料
（記得 urlopen 是 open request物件

現在要解析資料
資料是 html ，html 不好解析，
因此我們去安裝 beautifulsoup
安裝完後，使用套件工具協助解析，解析完後
就可以用 bs4 的工具，對標籤做篩選，找到我們想要的部分


"""


"""
Q:

請問root=bs4.BeautifulSoup(data,"html.parser")
後面的"html.parser"是做什麼的，為什麼要加那一句? 謝謝

A:
請 beautifulsoup 調用內部的 HTML 解析器來解析文件 ~


Q:
老师 我用和你一样的步骤 但是我没有办法抓到网页的编码. 
我的报错事
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)> 
请问这是什么原因?

a:
如果你是 Mac 電腦，請在程式前面加上
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


Q:
如果用  data = requests.get(url).content  好像就不用User-Agent
但我不太明白這兩個差在哪?

A:
requests 是要額外安裝的第三方套件，我們影片中用的是原生的模組，可以做一樣的工作，但它會幫你處理一些細節。


Q:
請問為什麼find_all("div",class_="title") 裡面的class_要有底線??
只打class好像不行

A:
因为class是内建关键字，所以必须用class_。
或者您也可以用字典方式操作{"class"："title"}
"""


# 困擾許久問題，沒法裝bs4套件
#
# 解法：
# 要升級pip3，再下載beautifulsoup4
# （但不確定前面刪除python有沒有影響

"""
純code:


import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"

request = req.Request(url,headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    },
)

with req.urlopen(request) as response: 
    data = response.read().decode("utf-8")


import bs4

root = bs4.BeautifulSoup(data, "html.parser")

titles = root.find_all( "div", class_="title")  

for title in titles:
    if title != None: 
        print(title.a.string)


"""
"""
寫code的順序：
順序 1: import urllib.request as req
順序 2: with req.urlopen(request) as response: 
順序 3: response.read()                             (只有讀到網頁，沒讀到有效資訊)
順序 4: bs4.BeautifulSoup(data, "html.parser")
順序 5: root.find_all( "div", class_="title")  
順序 6:
順序 7:
順序 8:
順序 9:
順序 10:


思考順序:我希望爬ptt網頁的標題資料
順序 1: 我希望我可以連網路
順序 2: 開啟網頁
順序 3: 資料抓下來
順序 4:我想要讓python可以讀 html
順序 5:變成我看得懂的樣子
順序 6:
順序 7:
順序 8:
順序 9:
順序 10:

1.
--------------------------------------------------------------------------------------------
舉販賣機為例，你很清楚輸入是「10元銅板」然後按了一個按鈕，「碰！」輸出「鋁箔包綠茶」。寫程式的話就是：

10元 = 參數

按按鈕 = 觸發/函數

鋁箔包綠茶 = return

2.
--------------------------------------------------------------------------------------------
此時如果一道題目是問你：「寫個提款機程式吧！」
那麼第一步呢，其實不是直接敲鍵盤（啊不過腦袋很清楚的話就直接敲鍵盤啦！）而是簡單像我這樣寫：

def 提款(提款卡 , 密碼,提領金額 ):

return 現金

以剛剛的提款程式為例，我會先去思考提款這個流程有哪些需要注意的地方，
也就是：「什麼情況下這個流程會出錯？這是很重要的，我們其實可以先不想流程本身

真正做到不重不漏，就會直接用反面去思考，
所以什麼情況下我們會無法提款呢？第一個就是參數輸入不全，對嗎？好比少了密碼、少了提領數字。
所以簡單在你的程式碼寫上第一個if：

不斷問自己然後呢才能做到不漏，
比如：如果你的提款數字有問題其實還有可能是：
帳戶的錢不夠，對吧？這裡你可能會興奮地寫下if account < 提款額度，沒錯，再來呢？
密碼有沒有可能錯誤？有！所以 if 密碼錯誤 ：沒錯吧？注意到了嗎，所有的問題都環繞在參數上，感受到先寫出input的威力了嗎？


3.
--------------------------------------------------------------------------------------------
搭建好if的流程後，我們就想if會發生什麼事情，比如：

if 提款卡 = null(沒有) or 密碼 = null or 提款金額 = null:

就說：「請輸入XX」。

所以這邊就是很簡單：根據參數來思考反面事件，然後思考怎麼處理缺失，處理缺失的方法也很多，就是思考該讓使用者回到程式的哪一步，
好比沒有密碼，就讓他回到「提款機的登入流程」，
以先前的販賣機來說，沒有投錢，就讓他回到：「可以投錢的流程」。


"""
