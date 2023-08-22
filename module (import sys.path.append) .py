"""
模組就是一個獨立的程式檔案
將程式寫在一個檔案中，此檔案可重複載入使用

#程式變得太長太多時，可以寫成不同的檔案，重複使用

模組有內建跟自定義的
sys就是內建
geometry就是自定義


e.g.
import sys  #載入 sys 模組

#使用 sys 模組
print(sys.platform)  #印出作業系統
print(sys.maxsize)   #印入整數型態最大值
print(sys.path)      #印出搜尋模組的路徑

另一個用法
import sys as s  #載入 sys 模組

#使用 sys 模組
print(s.platform)  #印出作業系統
print(s.maxsize)   #印入整數型態最大值
print(s.path)      #印出搜尋模組的路徑

"""


# 載入內建的 sys 模組並取得資訊
import sys

print(sys.platform)
print(sys.maxsize)

import sys as s  # 跟上面相同 只是幫他取別名

print(s.platform)
print(s.maxsize)


# 建立 geometry 模組，並載入使用      (建立新模組就是建立新python檔案)

# import geometry  # 因為放到資料夾後路徑會搜不到

# result = geometry.distance(1, 1, 5, 5)
# print(result)

# result = geometry.slope(1, 2, 5, 6)
# print(result)


"""
一般來說 想要使用模組
要跟主程式的檔案放一起 才可以跑 （同資料夾）
（但這樣會很亂 )
(e.g. module.py 跟grometry.py 一個是主程式一個是專門引用的

為了方便找，通常會設一個資料夾專門放模組
(但要是py檔放到資料夾，就不能直接import )

必須透過 sys.path.append("modules")


"""


# 調整搜尋模組的路徑
import sys

sys.path.append("modules")  # 在模組的搜尋路徑列表中「新增路徑」(載入系統模組，在path中新增路徑)
print(sys.path)  # 印出模組的搜尋路徑列表
print("==================")
import geometry

print(geometry.distance(1, 1, 5, 5))
