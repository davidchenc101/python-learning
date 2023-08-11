# 有序可變動列表 list
grades = [12, 60, 15, 70, 90]
print(grades)
print("列表中第一個資料＝", grades[0])
grades[0] = 55
print("55放入第一個資料=", grades[0])
print("列印1號到3號=", grades[1:4])
grades[1:4] = []
print("刪除列表（用空取代1-3號", grades)
grades = grades + [100, 33]
print("原來列表加新列表＝", grades)

# lenth=len(列表)
# len(grades)

# 巢狀列表
data = [[3, 4, 5], [6, 7, 8]]  # 第0組是345,第0組的第1位是4,第0組的第2位是5
print(data[0][1])

data[0][0:2] = [5, 5, 5]  # 把3跟4換成三個5
print(data)

# 有序不可變動列表 Tuple
data2 = (3, 4, 5)
print("data2＝", data2)
# 跟list差別在 打這串會error
# data[0]=5  #不能把5放入data2[0]的位置（因為是小括號
