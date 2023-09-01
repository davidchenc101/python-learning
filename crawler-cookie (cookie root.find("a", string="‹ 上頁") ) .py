"""
網路爬蟲的基本流程：
1.連線到特定網址，抓取資料。
2.解析資料，取得實際想要的部分。

《關鍵心法》盡可能地，讓程式模仿一個普通使用者的樣子。

＊Cookie＊
Q:什麼事Cookie？
A:網站存放在瀏覽器的一小段內容。

如果使用者的瀏覽器中，有放一個cookie
(連線時，放在Request Headers中送出。)


＊追蹤連結＊  (追蹤網頁的連結)
(html 網頁原始碼中經常包含超連結，在 a 標籤中，使用者點選 Google ，就會連到 https://www.google.com/ )

HTML超連結<a href="https://www.google.com/">Google</a>

如果我們的需求是抓到一份網頁，再追蹤網頁的超連結，抓到下一份網頁
(網頁的超連結是 a 標籤， href的屬性，抓到 href的網址做第二次連線)


連續抓取頁面實務:
解析頁面的超連結，並結合程式邏輯完成
(抓 ptt 八卦版的第一頁，追蹤他的上一頁連結，抓第二頁)
===>可達到抓很多頁的效果

"""


"""
我的感覺：
1.  coolie 可以存我已經 18 歲那個確認
2.  老師寫程式邏輯，是先寫能抓一夜頁面的爬蟲，再套迴圈
（每一個迴圈就 印當下頁面，並回傳新網址，並讓新網址取代舊網址）

"""


"""
問題：ptt 八卦版有確認18歲畫面，讓爬蟲無法順利
解法：讓 Request Heaaders 攜帶 over18 的 cookie ，讓確認18畫面不會跳出


流程1：去 ptt 八卦版頁面 => 三個小點 => 更多工具 => 開發人員工具 (f12)
流程2：最上方 element 那排的 application
流程3：左邊選單有個 cookies ，點下列選單有 https://www.ptt.cc
(這些資訊就是 ptt 放在我瀏覽器的 cookie)

流程4：在 network 點 index.html ，會看到三個大標                       
流程5：選 Headers 裡面選 Request Heaaders             (發送網路連線時，帶上的附加資訊)       
流程6：看到 cookie 欄位中的 over18 = 1
流程7：複製 over18 = 1
流程8：貼到 req.Request(url,headers={"cookie":"這裡" "User-Agent":""}


流程3說明：
放了五個小資料就是五片 cookie ，有每片 cookie 的名字跟資料  
有個 cookie 是 over18 = 1
意思是進入 ptt 八卦版後，你是否18歲？  
（在我按下我滿18，把 over18 記錄在瀏覽器裡，
下次進入八卦版時，看到你的 over18 是1，就將你帶入八卦版中

只要 over18 = 1 的 cookie 在瀏覽器中，
就不會跳出確認是否18畫面



流程5說明：
cookie 是存放在瀏覽器裡，當瀏覽器跟 ptt 做連線時
會將 cookie 放在 Request Heaaders 裡面，放在 cookie 欄位中，

cookie 欄位中會帶上全部的 cookie ，
但對我們來說重要的只有 over18 = 1

（如果能夠在 Request Heaaders 帶上 over18 的 cookie
我們就可以順利抓到八卦版的資料）


"""


# =============================================================================================
# 抓取PTT八卦版的網頁原始碼(HTML) - 一頁的版本
# =============================================================================================


# (談談 cookie機制)
import urllib.request as req

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
request = req.Request(
    url,
    headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    },
)

with req.urlopen(request) as responce:
    data = responce.read().decode("utf-8")

import bs4

root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)


# =============================================================================================
# 抓取PTT八卦版的網頁原始碼(HTML) -  希望多抓一些頁面
# =============================================================================================

"""
要讓程式很聰明的不斷抓別的頁面，
我們會觀察八卦版的頁面，
有個上頁按鈕，就是一個超連結
（就是一個 "<a 字串</a>"  的 a )

e.g. 我們抓標題是
class = "title"
(觀察後，發現標題都出現在 class = "title")
觀察後，只有文字"上頁"前面的網址能達到我的要求


概念：
抓到第一個頁面之後，
要動態追蹤 上頁的超連結 （在上頁的按鈕 右鍵 檢查）
得到：
<a class="btn wide" href="/bbs/Gossiping/index39231.html">‹ 上頁</a>

觀察後，發現只有“上頁”這個文字
希望利用“上頁”這個文字，抓到前面超連結的網址
(btn wide 有最舊 上頁 下頁 不能當特別之處)

"""

"""
問題：老師寫程式的順序
解法：爬一個網頁，解析成我看得懂的，找到下一頁網址，重複前三個動作

流程1: 想用網路功能， import urllib.request
流程2: 用網路連網頁，因此 with urlopen(url)
流程3: 把東西抓下來，因此 reponse.read().decode("utf-8")
流程4: 想要解析網頁，因此 import bs4
流程5: 我要解的網頁是 html ， root = bs4.BeautifulSoup(data, "html.parser")
流程6: 我要是網頁某個部分，    titles = root.find_all("div", class_="title")
流程7: 印出我想要的全標題， for title in titles:
流程8: 希望他自動去下一頁執行上面功能，去找下一頁網址 nextlink = root.find("a", string="‹ 上頁")
流程9: 因爲下一頁網址只有一半，要人工，return nextlink["href"]    pageurl = "http://www.ptt.cc" + getdata(pageurl)
流程10:重複動作 while count < 3: pageurl = "http://www.ptt.cc" + getdata(pageurl)

"""


# 抓取上一頁的連結
# nextlink = root.find("a", string="‹ 上頁")  # 找到內文是，"‹ 上頁" 的 a 標籤
# print(nextlink["href"])  # 目標是 href 裡面的網址，因此加上 [] 並打屬性的名稱
"""
此時獲取“上頁”的網址，但前面沒有 ptt.cc ，要人工加上
"""


# 整理之後的純code

# 連線加cookie
import urllib.request as req


def getdata(url):
    request = req.Request(
        url,
        headers={
            "cookie": "over18=1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        },
    )

    with req.urlopen(request) as responce:
        data = responce.read().decode("utf-8")

    # 解析網頁原始碼
    import bs4

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)

    # 跑出上頁網址
    nextLink = root.find("a", string="‹ 上頁")
    # print(nextLink["href"])

    # 希望她將上頁網址傳出來（但他上面印ptt內容一樣會做）
    return nextLink["href"]


# # 抓取一個頁面的標題
# pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"
# pageurl = "http://www.ptt.cc" + getdata(pageurl)
# print(pageurl)

pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
    pageurl = "http://www.ptt.cc" + getdata(pageurl)
    count += 1


"""
Q:
想請問若網站有登入頁面時，
怎麼等待使用者輸入帳密後，再繼續下面的抓取動作呢?

A:
使用者輸入帳密之後，大多數網站其實會在 Cookie 中放置一些資訊。
所以我們其實只要實際用電腦輸入一次，
然後觀察和擷取 Cookie 裡頭的資訊放進程式中，
就等於是使用者已登入狀態了。


Q:
想請問您為什麼在過濾文章 有沒有被刪除那個地方
一定要寫if title.a != None 
不能寫 if title.a == True ?

A:
因為 title.a 是一個物件或者是 None，
物件和 True 不會是相等的東西哦。

Q:
老師，想問
1.  第20行nextlink=root.find("a",string="‹ 上頁") ，
為何不用像上一支影片尋找"title"，寫find("div",class......)? 

2.  第21行return nextlink["href"] 的["href"]，
為何要用中括號[]呢?

A:
第一個問題是因為你要找的是特定的連結，
這個鏈結被包在<a href: 連結>上頁<a>這個結構中，
而上一支影片則是找所有titles，
而所有title都是被包在<div class=title> 標題<div>這個結構裡，
如果你用上一支影片的方式找是找不到上一頁的連結的喔


Q:
時間軸24:25
最後一行print(nextLink["href"])
請問要取href屬性網址的話，
為什麼nextLink後面是用中括號包住href呢？ 

A:
我們要取得標籤的屬性，要使用括號，這個算是規矩。


Q:
時間軸28:26
如果第23行這裡的變數已經是pageURL，
為何上方第3行的def getData() 括號內的參數仍維持 (url) 呢？ 
請問這裏的(url)的功用是什麼？

A:
參數只在函式中有效，
所以這個 url 就是接受我們呼叫 getData() 的時候傳遞進去的資料，
在外面的程式中，我們會把本次抓取到下一頁網址放在 pageURL，
然後傳遞到參數中進行下一個網頁的抓取。

Q:
老師請問def getData(url):裡面帶的url參數是對應到哪個呢?
因為試圖把def getData(url)的url改成pageURL發生找不到超連結的狀況，
謝謝老師回復

A:
getData 函式內部會使用到 url 參數，你仔細檢查程式就會看到。
所以你隨意把名字改掉，內部的程式會找不到東西是很正常的。



"""
"""
Q:
如果沒有 decode("utf-8")

A:
</div>\n\t\t\t<div class="title">\n\t\t\t\n\t\t\t\t
<a href="/bbs/Gossiping/M.1691835442.A.ABC.html">
<div class="author">
slimj951</div>\n\t\t\t\t
<div class="article-menu">
\n\t\t\t\t\t\n\t\t\t\t\t
<div class="trigger">&#x22ef;</div>


Q:
如果有decode("utf-8")

A:
                    <div class="item"><a href="/bbs/Gossiping/search?q=author%3Akobe26572153">搜尋看板內 kobe26572153 的文章</a></div>

            </div>

    </div>
    <div class="date"> 8/25</div>
    <div class="mark"></div>


    
Q: root 的樣子

A:
</div>
<div class="r-ent">
<div class="nrec"><span class="hl f3">19</span></div>
<div class="title">
<a href="/bbs/Gossiping/M.1692593913.A.AD2.html">[協尋] 8/18半夜1點半台中向上路東興路車禍影像</a>
</div>
<div class="meta">
<div class="author">ujiasobu</div>
<div class="article-menu">
<div class="trigger">⋯</div>


Q: 
title 沒有點 a 狀況

A:
<div class="title">
<a href="/bbs/Gossiping/M.1693556233.A.957.html">[問卦] 公司新人妹子叫Amber</a>
</div>
<div class="title">
<a href="/bbs/Gossiping/M.1677600392.A.D12.html">[公告] 八卦板板規(2023.03.01)</a>
</div>


Q:
title 有點 a 狀況

A:
<a href="/bbs/Gossiping/M.1693556178.A.A33.html">Re: [問卦] 什麼樣的政見可以打動你</a>
<a href="/bbs/Gossiping/M.1693556228.A.366.html">[問卦]澀谷事變發生在西門町會怎樣？</a>
<a href="/bbs/Gossiping/M.1693556233.A.957.html">[問卦] 公司新人妹子叫Amber</a>


Q:
title 有點 a 有點 string

A:
Re: [問卦] 什麼樣的政見可以打動你
[問卦]澀谷事變發生在西門町會怎樣？
[問卦] 公司新人妹子叫Amber
[問卦] 蔡阿嘎幸運躲過颱風 安全回台


Q:
nextlink 長這樣

A:
<a class="btn wide" href="/bbs/Gossiping/index39316.html">‹ 上頁</a>
"""
