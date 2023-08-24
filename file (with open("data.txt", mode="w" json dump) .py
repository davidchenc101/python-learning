"""
檔案操作流程 
開啟檔案 > 讀取或寫入 > 關閉檔案


＊開啟檔案＊
=================================
檔案物件＝open(檔案路徑,mode=開啟模式)   是要讀or寫or讀寫

開啟模式：
讀取 -r
寫入 -w
讀寫 -r+


＊讀取檔案＊
=================================
#讀取全部文字
檔案物件.read()   

#一次讀取一行
for 變數 in 檔案物件：
    從檔案依序讀取每行文字到變數中  #一行字串到一個變數中

#讀取 JSON 格式
import json
讀取到的資料＝json.load(檔案物件)


＊寫入檔案＊ （儲存檔案的意思）
===============================
#寫入文字
檔案物件.write(要存的字串)

#寫入換行符號
檔案物件.write(“這是範例文字\n”)

#寫入 JSON 格式
import json
json.dump(要寫入的資料,檔案物件)


＊關閉檔案＊
=================================
檔案物件.close()    #把檔案關閉以釋放資源


＊最佳實務＊
=================================
with open(檔案路徑,mode=開啟模式) as 檔案物件：
    讀取或寫入檔案的程式

#如果寫這種的，就不用寫close，安全且可靠
#以上區塊會自動，安全的關閉檔案

"""


# ===========================================================================================
# 儲存檔案
# ===========================================================================================
file = open("data.txt", mode="w")  # 開啟 #會存在跟file.py同個資料夾中  #檔案路徑最簡單就是選檔名
# file = open("data.txt", mode="w",encoding="utf-8") #如果想打中文就打這個 (open可以指定編碼)
file.write("hello fil")  # 操作
file.close()  # 關閉
"""
會產生新的檔案(data.txt)在資料夾裡
(如果沒找到同檔名會新創一個)
(寫的時候是把整個檔案全蓋掉全重寫)
"""

# 最佳實務寫法：(不用寫close，會自動將檔案釋放跟關閉)
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("測試中文\n好棒棒")


# ===========================================================================================
# 讀取檔案 (讀取只能讀已經存在的)
# ===========================================================================================
with open("data.txt", mode="r", encoding="utf-8") as file:
    data = file.read()
print(data)


# 把檔案中的數字資料，一行一行的讀取出來，並計算總和
sum = 0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:  # 第一行放入line 第二行放入line (只是剛好程式是一行走完下一行，才能一行一行讀取)
        sum = sum + int(line)  # 第一行轉成數字放入sum
print(sum)


# ===========================================================================================
# 使用 JSON 格式讀取，覆寫檔案
# ===========================================================================================
import json


# 從檔案中讀取json資料，放入變數data 裡面
with open(
    "config.json",
    mode="r",
) as file:
    data = json.load(file)  # json讀取進來他是一個字典
print(data)  # data 是一個字典資料
print("name ", data["name"])
print("version ", data["version"])


# 如果我們希望改json的資料 (流程：改完資料再寫進去)
data["name"] = "cool name"
# 把最新的資料覆寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)  # 把字典的結構轉換成對應的 JSON 格式字串，然後儲存到檔案中


"""
json懶人包：
json: javascript object notation (javascript 物件表示法)

第一段：
var point = new onject();
point.x=3;
point.y=4;
point.get=function(){
    alert(this.x+","+this.y);
};

第二段：
var point={"x":3 , "y":4 ,
"get": function(){alert(this.x+","+this.y)}

}

有json可以用短短的第二段 表示囉唆的第一段
不但可以放值也可以放功能
(可以視為python的字典)


"""


# ----------------------------------疑惑區-------------------------------------------------------------


# for x in range(11):
#     sum=sum+x

# with open("data.txt",mode="r") as file:
#     for line in file:             #file這邊也算個列表？
#         sum = sum + int(line)
# print(sum)

"""
請問file是物件還是一個變數?
ans:file 是變數，裡面存放一個物件。

2. 之前在教for語法的時候，有說in的後面必須是列表，現在這樣使用是否代表儲存的檔案物件"file"本質是一種列表呢？
ans:
這個問題非常的好，其實 for in 的後面不一定要是列表，
他是一個更廣泛的概念就做 Iterable Object，但這個概念有點深入，所以我入門教學的時會稍微簡化或省略細節。

ans:
file 物件本身是一個 Iterable Object 所以可以放在 for in 的後面。
for data in file.read() 則是把 file.read() 取得的字串放在 for in 的後面，不太一樣的狀況。

ans:
file 可以粗略的理解成是一個檔案物件，對於檔案物件做 for 迴圈會有一行一行讀取的效果，不會算進換行符號 \n。
這個和你直接用字串去跑 for 迴圈是不同的。
"""
