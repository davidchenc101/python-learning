"""
封包就是用來整理、分類模組
(如果只有一兩個模組，通常用不到封包)

系統的資料夾：封包
系統的檔案：模組

*專案資料夾
    主程式.py           
    *封包資料夾          #建立一個資料夾當作封包
        __init__.py    #封包資料夾裡面除了裝模組外，還必須建立一個特殊的python code （如果沒有這行，就是普通資料夾，寫了這行才是封包資料夾
        模組一.py
        模組二.py

*專案資料夾
    main.py           
    *geometry          
        __init__.py    
        point.py
        line.py        

import 封包名稱.模組名稱
import 封包名稱.模組名稱 as 模組別名

step1:按vscode新增資料夾，取名geometry
step2:在geometry底下，新增python檔，名字叫 __init__.py  (py檔裡面可以空，但必須要有)
step3:可在封包中建立模組，建立第一個叫point.py 跟line.py
step4:打point.py line.py的東西
step5:
step6:





"""


# 主程式
# 如果想使用點的功能
import geometry.point

result = geometry.point.distance(3, 4)
print("距離", result)


import geometry.line

result = geometry.line.slope(1, 1, 3, 3)
print("斜率", result)
