# break 強制結束迴圈
# =============================
# n=1
# while n<5:
#   if n==3:
#       break
#   n+=1
# print(n)
# =============================
# n最一開始是1,1不等於3,會執行n+=1
# break會直接跳到 print(n)
# 迴圈一塊只有while到n+=1


# continue 強制繼續下一圈
# =============================
# n=0
# for x in [0,1,2,3]:
#   if x%2==0:
#       continue
#   n+=1
# print(n)
# =============================
# x最一開始是0,  0/2餘0
# continue會直接跳到 for x in [0,1,2,3]:
# if餘數＝0,跳到for,不會碰到n+=1
# if餘數非0,,碰到n+=1,再跳for
# n+=1 是else的感覺
# ===============================
# 附上正統的迴圈結構
"""
n=1;
while n<5:
    print("變數n為：",n)
    n+=1
else:
    print(n)
"""

"""
for c in "hello":      ＃取出H放入c
    print("逐一取得字元",c)
else:
    print(c)
"""


# 問題1
# else是不是回圈的一塊?
# for x in range(5):
#   if ...
#       ...
#       break
# else:
#   ...
# =============================
# 如果答案是yes
# >>> 進入if後自然不會有else的東西  ok
# <<< 但每一次都會跑else   error

# 如果答案是no
# >>>每一次都會跑else的東西 error
# <<< 但跑1234不會跑else  ok
"""
正確思考方式
要將for回圈跟if else分開思考
else並非迴圈一塊

for只跑if 的地方
如果沒找到if條件就下一輪
如果有找到if條件，有break會跳出迴圈
跳出後會跑到else那行
＝＝＝＝＝＝＝＝＝＝＝＝＝＝
但因為不在if裡面 這邊else不作為（可忽略）
＝＝＝＝＝＝＝＝＝＝＝＝＝＝

if enter 9
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
if 0*0==9    一次
但else在外面 所以不會跑else
if 2*2==9    三次
但else在外面 所以不會跑else
if 3*3==9    第四次 正確
顯示”“”整數平方根",i“”“
break後跳出迴圈 走到else
但else是if管的 可忽略else 所以不顯示else資訊

if enter 8
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
if 1*1==8    二次
但else在外面 所以不會跑else
if 2*2==8    三次
但else在外面 所以不會跑else
.......................
.......................
if 8*8==8    第九次 
會跳到else
顯示"沒有整數平方根"

"""
"""
正確寫法:
n = input("輸入一個正整數")  #讓使用者輸入數字
n = int(n) #轉換輸入成數字
for i in range(n):     # i從0~n-1
    if i*i == n:
        print("整數平方根",i)
        break #如果找到平方根，就break 跳出for 迴圈
else:
    print("沒有整數平方根")

"""

# ==================================
# break 的簡易範例
n = 0
while n < 5:
    if n == 3:
        break
    print(n)  # 印出迴圈中的n
    n += 1
print("最後的n:", n)  # 印出迴圈結束後的n
##小小補充 ctrl加/ :可以一次全註解


# continue 的建議範例
m = 0
for x in [0, 1, 2, 3]:  # <---<--^
    if x % 2 == 0:  #           |
        continue  # ->-->--->--->
    print(x)
    m += 1
print("最後的m:", m)


# else的建議範例
sum = 0
for b in range(11):  # 0~10的列表
    sum += b
else:
    print(sum)  # 印出0+1+2+...10


# 綜合範例：找出整數平方根
# 輸入9，得到3，輸入11，得到沒有
v = input("輸入一個正整數：")
v = int(v)  # 轉換輸入成數字
for i in range(v):
    if i * i == v:
        print("整數平方根", i)
        break  # 用break強制結束回圈時，不會執行else區域
else:
    print("沒有整數平方根")
