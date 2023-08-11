# 判斷式
x = input("請輸入數字：")  # 取得字串形式的使用者輸入（吃進去是字串）
x = int(x)  # 將字串轉為數字型態

if x > 100:
    print("大於100")
elif x > 50:
    print("大於50，小於等於100")
else:
    print("小於等於100")

# 四則運算
n1 = int(input("請輸入數字一："))
n2 = int(input("請輸入數字二："))
op = input("請輸入運算符號：+ - * /：")
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("不支援此運算")
