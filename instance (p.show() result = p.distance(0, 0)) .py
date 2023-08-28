"""
回顧：
實體物件的建立與使用

類別兩種用法：
第一種：類別與類別屬性      （做一些工作 在class.py的檔案)
第二種：類別與實體物件、實體屬性、實體方法  (此節重點在實體方法)

=============================================================================================
實體屬性
=============================================================================================
實體屬性：封裝在實體物件中的變數

《程式範例》
class Point:
      def __init__(self,x,y):
            self.x = x
            self.y = y
# 建立實體物件，並取得實體屬性資料
p = Point(1,5)
print(p.x+p.y)

"""


"""
開始：
=============================================================================================
實體方法
=============================================================================================
實體方法：封裝在實體物件中的函式

class 類別名稱:
      # 定義初始化函式
      def __init__(self):
            定義實體屬性
      定義實體方法/函式        (其他都一樣，只有這行不同，注意縮排是跟def相同)
# 建立實體物件，放入變數obj中
obj = 類別名稱()  


class 類別名稱:
      # 定義初始化函式
      def __init__(self):
            封裝在實體物件中的變數
      def 方法名稱(self,更多自訂參數):
          方法主體,透過self操作實體物件
# 建立實體物件，放入變數obj中
obj = 類別名稱() 


===============================================
使用方法
===============================================
實體物件.實體方法名稱(參數資料)


《程式範例》
class Point:
      def __init__(self,x,y):
            self.x = x
            self.y = y
      def show(self):           (定義一個實體方法叫做show，唯一重要一定要寫self，self代表實體物件本身，)
          print(self.x,self.y)
p = Point(1,5)  # 建立實體物件
p.show()        # 呼叫實體方法


"""


# =============================================================================================
# Point 實體物件的設計：平面座標上的點
# =============================================================================================


class Point:
    def __init__(self, x, y):  # 先建立一個初始化函式，需要傳入 x 跟 y
        self.x = x
        self.y = y

    def show(self):  # 再來定義實體方法，把x y 實體屬性印出
        print(self.x, self.y)

    def distance(self, targetx, targety):
        return (((self.x - targetx) ** 2 + (self.y - targety) ** 2)) ** 0.5


p = Point(3, 4)
p.show()  # 呼叫實體方法 / 函式
result = p.distance(0, 0)  # 計算座標 3,4 和座標 0,0 之間的距離
print(result)

# 他就是一個函式的概念，
# 所以函式中的參數回傳值都還是保持一制的思考，
# 跟函式是一樣的東西
# 只是封裝在實體物件裡面，我們叫實體方法

"""
我的感覺：
實體方就是物件裡面的函數
p可以 .x .y .show .distance

發現神奇現象：
 def __init__(self, x, y):  
        self.x = x
        self.y = y

 def __init__(self, name):
        self.name = name
        self.file = None 

self.file 這左半邊，想取什麼名都可以
self.x = x 可以改為 self.x23 = x (不會error)
(左邊都是自己取名的，不用管規則)

self.file = None 
可以這樣打的原因為：
1.self.file 因為是在左半邊名字隨便取 可以self.file476
2.self.file 的右半邊，可以是各種name (3*name+you )，也可以等於none

硬要把file打入也可以
 def __init__(self, name, file):
        self.name = name
        self.file = None 

＊這個就變成使用file類別每一次輸入都要兩個參數＊
f1=File("data1.txt")

變成：

f1=File("data1.txt", "None")


"""


# =============================================================================================
# File 實體物件的設計：包裝檔案讀取的程式
# =============================================================================================

# 定義這個class，就是為了產生實體物件

# 檔案讀取流程
# 要有檔案名稱，要做檔案的開啟，要做檔案的讀取
# 把這些流程包裝在一個實體物件中。


# 目標是包裝檔案讀取的程式
class file:
    # 初始化函式
    def __init__(self, name):
        self.name = name  # 把檔案名稱記錄在實體屬性內，額外紀錄檔案物件，一開始叫none（因為沒開啟檔案）
        self.file = None  # 尚未開啟檔案：初期是None 代表空的意思

    # 實體方法 (把開啟檔案的動作定義在實體物件的實體方法中當中)
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")  # 想成self.file是放檔案權限

    def read(self):
        return self.file.read()  # 把檔案中資料讀取出來再回傳


# 157行，open是我取的名字
# 158行，open是系統功能
# 開啟檔案之後，把檔案物件放在實體屬性file裡面


# 讀取第一個檔案
f1 = file("data1.txt")
f1.open()
data = f1.read()
print(data)

# 讀取第二個檔案
f2 = file("data2.txt")
f2.open()
data = f2.read()
print(data)


"""

class file2:

    def __init__(self, name2):
        self.name2 = name2  

    def show(self):
        self.xxx = print("data is exist")
        print("184:",self.xxx)

x1 = file2("andy")
x1.show()

# 大意外：變數不能存功能！（應該算存功能的起始點）
# self.xxx列印出是none，但data is exist會跑出來
#实际上是在将返回的文件对象赋值给了名为 file 的变量。
# 这允许你通过 file 变量来访问和操作打开的文件。
"""


"""
Q:
彭彭老師好，
想問說 def __init__(self, name) 的括號裡面沒有寫 file ，
是因為下面的實體屬性 self.file 一開始定義是 None ，所以可以不用寫出來嗎?  
(如果寫成def __init__(self, name, file)，
後面的 f1=File("data1.txt") 
就要寫成 f1=File("data1.txt", "None")，不知道這樣理解對不對)

ans:
對呦，你的說明蠻好的呀 :)



Q:
請問老師，為甚麼在初始化涵式要先定義file=None，
如果是在實體方法中需要用的變數，
都需要再初始化涵式當中先定義嗎?

ans:
可以不用定義哦，
但我的主觀意見覺得在初始化的時候定義清楚它是空值，
是個好主意 ~



Q:
彭彭老師您好:
為了方便自己理解self.file的部分，自己改了以下這兩行
def__init__(self,name,file):
f1=File("data.txt","None")
程式一樣可以正常運作讀取到資料，意思和本來self.file=None一樣嗎?
謝謝您。

ans
你改的程式不影響原來的運作邏輯哦 ~~~~



Q:
請問一下,在最後初始化函式中,self.name=name和self.file=None有意義嗎?
但是self.file=None的意義在哪? 我刪掉此行，也照樣可以跑檔案出來>_<

ans:
self.file 也可用在 read() 裡檢查 user 是否已呼叫 open() 再呼叫 read():

      def read(self):
        if self.file != None:
            return self.file.read()
        else:
            print("Please call open() first")

老師只是為求易懂簡化寫法，沒特別寫這麼細而已



Q:
我把self.file=None刪掉
程式也能正常運作

我就是看不懂為什麼要打self.file=None
乾脆把她刪掉運作
完全看不懂

ans:
初始化的意義，確實你把這個指令刪掉也可以運作沒錯，
但概念上我們給他一個初始值，告訴自己有這樣的東西在那裡 ~


"""
