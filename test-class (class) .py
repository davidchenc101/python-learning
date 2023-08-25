"""
類別的定義與使用：
===================================================================================
類別：一種python語法的結構，可將變數或函式封裝在裡面
（封裝在類別裡的變數或函式，就叫類別的屬性）
===================================================================================

想使用類別有兩步驟：
第一步：定義類別
第二步：使用類別中的屬性

======================================
定義類別：
======================================
class 類別名稱：
    定義封裝的變數
    定義封裝的函式

    
#定義Test的類別
class Test:
    x=3
    def say():
        print("hello")

# x 跟 say 就是 Test類別的屬性
# x 跟 say 是封裝在 Test 類別的裡面，就是 Test類別的屬性


======================================
使用類別：
======================================
類別名稱.屬性名稱

#定義Test的類別
class Test:
    x=3
    def say():
        print("hello")

#使用Test的類別
Test.x+3     取得屬性 x 的資料 3
Test.say()   呼叫屬性 say 函式




"""


# 定義類別，與類別屬性（封裝在類別中的變數和函式）
# 定義一個類別 IO ，有兩個屬性 supportedStcs 和 read
class IO:  # 這個叫 IO類別
    supportedSrcs = ["console", "file"]

    def read(src):
        if src not in IO.supportedSrcs:
            print("not supported")
        else:
            print("read from", src)


# 使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")
