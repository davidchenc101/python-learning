# 數字運算
# (2的三次方是8 2**3) (3/6只取整數是 3//6)
x = 3 + 6
print("x=", x)
x = x + 1
print("x=", x)

# 字串運算
s = "hello" + "would"
s = "good\nmorning"
s = "hello123" * 3
print("s=", s)

# 字串會對內部的字元編好，從0算起
a = "eigenvalue"
print("a[0]=", a[0])
print("英文單字前4個字＝", a[0:4])  # 0到4其實是五個 不包含最後一個
print("從某字後面全部＝", a[1:])
print("從頭到某字＝", a[:3])
