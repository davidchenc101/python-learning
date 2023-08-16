# while 迴圈
n = 1
while n <= 3:  # 要記得加冒號
    print(n)
    n += 1

# 1+2+3+4...+10
m = 1
sum = 0
while m < 11:  # 要注意縮排（在縮排裡有迴圈
    sum = sum + m
    m = m + 1
print("sum = ", sum)  # 沒縮排 就不在迴圈迴圈中


# for 迴圈
for x in [3, 5, 1]:  # 把列表資料一一撈出
    print(x)
for c in "hello":  # 分別把字元撈出
    print(c)
for v in range(5):  # range(3)相當於[0,1,2]的列表  for x in range(3) == for x in [0,1,2]
    print(v)  # for x in range(3,6) == for x in [3,4,5]

# 希望迴圈跑10次
for z in range(11):
    print("這是第", z, "次")

# 1+2+3+4...+10
sum_0 = 0
for b in range(11):  # 希望跑10次 for x in range(10) 0~9 共10次
    sum_0 = sum_0 + b
print(sum_0)
