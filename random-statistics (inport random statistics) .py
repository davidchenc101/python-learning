"""
學習 random 和 statistics 模組
（兩者都是python內建模組）

==========================================
亂數模組：
==========================================
載入模組:
import random

從列表中隨機選取 1 個資料:
random.choice([0,1,5,8])  (從0,1,5,8隨便挑一個)

從列表中隨機選取 2 個資料:
random.sample([0,1,5,8],2) 
random.sample([0,1,5,8],3)  #選三個

隨機調換順序：
import random
＃將列表的資料「就地」隨機調換順序  (會直接動到原本data資料)
data=[0,1,5,8]
random.shuffle(data)
print(data)

隨機亂數：
import random
＃取得0.0 ~1.0 之間的隨機亂數
random.random()          #可以取0到1之間的每一個數字
random.uniform(0.0,1.0)  #指定0.0到1.0之間
（uniform代表機率相同，可以寫 (1.0,5.0) 求1~5之間的亂數

常態分配亂數：
import random
random.normalvariate(100,10)
#取得平均數100，標準差10的常態分配亂數  （大部分取到的數字在90~110之間，只有少部分會到130,50,60




==========================================
統計模組：
==========================================
載入模組:
import statistics

計算平均數：
import statistics
statistics.mean([1,4,6,9])  #計算列表中數字的平均數  1,4,6,9的平均

計算中位數：
import statistics
statistics.median([1,4,6,9])  #計算列表中數字的中位數  1,4,6,9的中位數

計算標準差：
import statistics
statistics.stdev([1,4,6,9])  #計算列表中數字的標準差  1,4,6,9的標準差


"""

# =======================================
# 亂數模組
# =======================================
import random

# 隨機選取
data = random.choice([1, 5, 6, 10, 20])
print(data)

data = random.sample([1, 5, 6, 10, 20], 3)  # 可隨機選取多個
print(data)

# 隨機調換順序
data = [1, 5, 8, 20]
random.shuffle(data)
print(data)

# 隨機取得亂數
data = random.random()  # 0~1之間的隨機亂數
print(data)

data = random.uniform(60, 100)  # 中間數字出現機率是相等的
print(data)

# 取得常態分配亂數
data = random.normalvariate(100, 10)  # 平均數100 標準差10 得到資料多數在90~110間
print(data)


# ==========================================
# 統計模組
# ==========================================
import statistics as stat

data = stat.mean([1, 4, 5, 8])  # 算1,4,5,8的平均
print(data)

data = stat.median([1, 4, 5, 8])  # 算1,4,5,8的中位數
print(data)  # 中間的數，不受極端值影響

data = stat.stdev([1, 4, 5, 8])  # 算1,4,5,8的標準差
print(data)  # 資料的分散狀況
