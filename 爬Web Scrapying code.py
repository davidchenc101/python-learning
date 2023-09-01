import urllib.request as req


def getdata(url):
    request = req.Request(
        url,
        headers={
            "cookie": "over18=1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        },
    )

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")

    for title in titles:
        if title.a != None:
            print(title.a.string)

    nextlink = root.find("a", string="‹ 上頁")
    return nextlink["href"]


pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"

count = 0
while count < 3:
    pageurl = "http://www.ptt.cc" + getdata(pageurl)
    count += 1
