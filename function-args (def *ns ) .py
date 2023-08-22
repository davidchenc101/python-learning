"""
def 函數名稱（參數名稱＝預設資料）：
    函數內部的程式碼
def say(msg="hello"):
    print(msg)

say("hello function") #印出hello function
say()                 #印出hello 
"""

"""
def 函數名稱（名稱1,名稱2）：
    函數內部的程式碼

函式名稱(名稱2=3,名稱3=5)     #白話就是用參數地方名字對，可以不用照順序

def divide(n1,n2):
    result=n1/n2
    print(result)

divide(2,4)         #印出0.5
divide(n2=2,n1=4)   #印出2.0

"""

"""
def 函數名稱(*無限參數)：
    無限參數以Tuple資料型態處理
    函式內部的程式碼

#呼叫函式，可傳入無限數量的參數
函式名稱(資料1,資料2,資料3) 

def say(*msgs):
    for msg in msgs:
        print(msg)

say("hello","arbitary","arguments")
"""


## 參數的預設資料
def power(base, exp):
    print(base**exp)


power(3, 2)  # 3的平方
# power(4)  這個會error 因為這邊要兩個參數


# ＝＝＝＝＝＝＝ 因此可給參數預設資料
def power(base, exp=0):  # 如果下面參數沒給值 就是0次方處理
    print(base**exp)


power(3, 2)
power(4)  # 這邊是4的0次方


## 使用參數名稱對應


def divide(n1, n2):
    print(n1 / n2)


divide(2, 4)  # 印出0.5
divide(n2=2, n1=4)  # 印出2.0


# 無限/不定 參數資料
def avg(*ns):
    sum = 0
    for n in ns:
        sum = sum + n
    print(sum / len(ns))


avg(3, 4)
avg(3, 5, 10)
avg(1, 4, -1, -8)
