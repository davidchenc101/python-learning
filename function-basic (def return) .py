"""
函式：就是一個程式區塊
我們把常用的程式包裝起來
未來如果需要重複利用會比較方便

函式參數的設計：
參數可以讓我們的函式有彈性


定義：
def 函式名稱（參數名稱）：
    函式內部程式碼

def sayhello():
    print("hello")

def say(msg):  #把參數印出來
    print(msg)

def add(n1, n2):  
    result=n1+n2
    print(result)

呼叫：
sayhello()

say("hello function")
say("hello python")

add(3, 4)
add(7, 8)


回傳值：
def 函式名稱（參數名稱）：
    函式內部程式碼
    return         #結束函式，回傳none

def 函式名稱（參數名稱）：
    函式內部程式碼
    return 資料  （數字，字串，布林值，物件，列表，字典）

    
e.g.
def say(msg):
    print(msg)
    return

value=say("hello function")
print(value)    #會印出空(印出None)

e.g.
def add(n1, n2):  
    result=n1+n2
    return"hello"

value=add(3,4)
print(value)    #會印出hello


############################                                
##回傳值的設定##
定義函數是input msg參數
執行print動作 但回傳值為空

呼叫時 (say("hello function"))
，跑到第45行say(msg)，做完print
會回傳空(return 沒東西就是空)，
空再放入value
#############################

有意義程式：
e.g.
def add(n1, n2):  
    result=n1+n2
    return"result"

value=add(3,4)
print(value)    #會印出7


"""


# 定義函式
# 函式內部程式碼，若是沒有函式呼叫，就不會執行
def multiply():
    print(3 * 4)


def multiply2(n1, n2):
    print(n1 * n2)


def multiply3(n1, n2):
    print(n1 * n2)
    return


# multiply2跟multiply3
# 這兩個是一樣的（一模一樣）


# 呼叫函式
multiply()  # 這是動作，會直接print，
multiply2(10, 8)

value = multiply2(4, 5)  # 這是把值給value，有動作print，但值是空
print(value)

""" 
動作歸動作，值歸值
104行會執行print，但回傳值是空
107行是要將值給value，value=none

執行107行
會將4,5帶入參數
會print 4*5 （第一次）

將回傳值給value  (value = none)
會print value  (第二次)

"""


# 回傳值的好處
# 如果程式有在外部繼續再操作資料的需求
# 就會採用回傳值來處理
def multiply4(n3, n4):
    return n3 * n4


value = multiply4(3, 4) + multiply4(4, 5)


# 程式的包裝 (函式最重要的用途)


# 如果沒有此功能，我希望1加到10
# 又希望寫1加到20
"""
sum=0
for n in range(1,11):
    sum = sum+n
print(sum)

sum=0
for n in range(1,21):
    sum = sum+n
print(sum)
"""

# 發現類似工作一直做一直做
# 持續複製貼上>>>>>就會用到程式的包裝


def calculate():  # 要縮排才是在函式裡面
    sum = 0
    for n in range(1, 11):
        sum = sum + n
    print(sum)


calculate()
calculate()  # 輕鬆很多


def calculate2(max):  # 加入彈性
    sum = 0
    for n in range(1, max + 1):
        sum = sum + n
    print(sum)


calculate2(10)
calculate2(20)
