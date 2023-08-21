# 集合的運算
s1 = {3, 4, 5}
print("測試3是否在集合中：", 3 in s1)
print("測試3是否不在集合中：", 3 not in s1)

s2 = {1, 2, 3}
s3 = {2, 3, 4}
s4 = s2 & s3  # 交集，取兩個集合中，相同的資料
print(s4)
s5 = s2 | s3  # 聯集，取兩個集合所有資料，但不重複 （enter上方）
s6 = s2 - s3  # 差集，從s2中，減去和s3重疊的部分
s7 = s2 ^ s3  # 反交集，取兩集合中，不重疊的部分 （取不重疊的部分

s = set("hello")  # 字串拆結成集合 ＃set(字串)
print(s)
print("h" in s)  # 可測試h有沒有在字串中


# 字典的運算 key-value 配對
dic = {"apple": "蘋果", "bug": "蟲子"}
print(dic["apple"])

dic["apple"] = "大蘋果"  # 把apple的值改為新值
print(dic["apple"])

print("apple" in dic)  # 是判斷apple是不是有在key裡，跟value沒關

del dic["apple"]  # 刪除apple這個key，只剩bug的key
print(dic)

# 以列表資料r產生字典 （列表資料就是(3,4,5))
dic2 = {x: x * 2 for x in [3, 4, 5]}
print(dic2)
