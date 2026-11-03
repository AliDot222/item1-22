# NAME OF THIS FILE : item19

x = 1
print(type(x)) #>>> <class 'int'> 

#####

class Point :                   
    def draw(self):               
        print("draw_mamamia")

point = Point()

point.draw() #>>> draw_mamamia 

print(type(Point)) #>>> <class 'type'>    
print(type(point)) #>>> <class '__main__.Point'> || __main__ iek module ast
print(isinstance(point, Point))#>>> True 
print(isinstance(point, int)) #>>>False 

####

# instance = مثال 
# در برنامه نویسی : مثالی از یک کلاس یا نمونه ای از یک کلاس

####

print(type(isinstance))#>>> <class 'builtin_function_or_method'>
print(type(print))     #>>> <class 'builtin_function_or_method'>

#####

# اتربیوت = ویژگی
# اتربیوت ها مقادیر هستند
#متد ها یک کاری انجام میدهند
# def __init__(self) --> Constructor function = متد سازنده(سازنده کلمه کلیدی و مهمیه)

class Point :
    def __init__(self,x,y): # آرگومان های 1 و 3 در پارامتر های ایکس و ایگرگ ذخیره میشوند
        self.x = x          # سلف به آبجکتی که در آینده ساخته میشه اشاره داره 
        self.y = y          # ایگرگ راست پارامتر و ایگرگ چپ اتربیوت هست 

    def draw(self):         # متد درا را ساختیم
        print('DRAW')

point = Point(1, 3) # آرگومان های 1 و 3 را به سازنده ارسال کردیم

               # point = self = obj
print(point.x) #     خروجی 1  صدا زدن اتربیوت ایکس
print(point.y) #خروجی 3  صدا زدن اتربیوت ایگرگ
#      obj.Attribute
point.draw()   # خروجی   DRAW  صدا زدن متد درا 

#####

class Point :
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
    def draw(self):
        print(self.x , self.y) # متد draw میاد مقدار self.x و self.y را چاپ میکند

point = Point(5,7)  # اینجا اومدیم ابجکت پوینت درست کردیم
other = Point(1, 2) # اینجا اومدیم ابجکت آزر درست کردیم

point.draw() #>>> 5 7 
other.draw() #>>> 1 2

#####

class Point :
    def __init__(self ,x ,y): # x,y پارامتر هستند
        self.x = x
        self.y = y

    def draw(self):           # slef پارامتر اجباری برای هر متد در کلاس ها
        print(f"{self.x}, {self.y}")

point = Point(3, 1)
other = Point(5, 3)

point.draw()
other.draw()

# اینجا اومدیم ست کردیم
point.z = 10   # اتربیوت زد را با مقدار ده برای ابجکت پوینت اضافه کردیم 
#              #The attribute z -> instance attribute.
Point.c = 11   #The attribute c -> Class attribute.
####

class Point :
    default_color = "red"       # Class Attribute
    
    def __init__(self ,x ,y):    
        self.x = x              # Instance Attribute
        self.y = y              # Instance Attribute
    
    def draw(self):
        print(f"{self.x}, {self.y}")

p = Point(3, 1) # آبجکت p ساختیم 
s = Point(0, 0) # آبجکت s ساختیم 
# این آبجکت ها که در بالا ساختیم متعلق به کلاس point هستند 
print(p.default_color) #>>> red 
print(s.default_color) #>>> red
print(Point.default_color) #>>> red

####

class Point :
    default_color = "red"       
    
    def __init__(self ,x ,y):
        self.x = x                
        self.y = y
    
    def draw(self):
        print(f"{self.x}, {self.y}")

p = Point(3, 1) # آبجکت p ساختیم 
s = Point(0, 0) # آبجکت s ساختیم 

Point.default_color = "blue" # اومدیم مقدار بلو رو برای کلاس اتربیوت دیفالت کالر ست کردیم

print(p.default_color) #>>>  blue
print(s.default_color) #>>> blue 
print(Point.default_color) #>>>  blue

#### 

class Point :
    default_color = "red"
    
    def __init__(self ,x ,y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"{self.x}, {self.y}")

p = Point(3, 1) # obj p sakhtim
s = Point(0, 0) # obj s sakhtim

p.default_color = "blue" # مقدار بلوو را برای اینستنس اتربیوت دیفالت کالر ست کردیم

print(p.default_color) #>>>  blue
print(s.default_color) #>>> red 
print(Point.default_color) #>>>  red

####

class Point :
    def __init__(self ,x ,y):
        self.x = x
        self.y = y

    @classmethod #به پایتون می‌گوید که این متد متد کلاس است نه متد نمونه ||  nemone = instance
    def zero(cls): #cls دقیقا مثل self است، اما برای کلاس. cls <- ghanon name gozari -> Point 
        return cls(1, 1) # Class -> cls  ->  Point  <-  self <- obj

    def draw(self):
        print(f"{self.x}, {self.y}")

p = Point.zero() #ما متد کلاس zero را مستقیماً روی کلاس Point صدا زدیم.
#zero() یک آبجکت جدید Point با x=1 و y=1 می‌سازد و آن را به p نسبت می‌دهد.
p.draw() #>>> 1, 1

# با این روش ما اومدیم متد زیرو ساختیم که بتونیم باهاش به ابجکت های جدید مقدار مشخص دهیم
# مثلا در پروژه های بزرگ چندین ابجکت هستند که یک مقدار ثابت میگیرند
#به جای اینکه بنویسم
#ppp = Point(0,0,0,0,0,0,0)
#sss = Point(0,0,0,0,0,0,0)
#rrr = Point(0,0,0,0,0,0,0)
#hhh = Point(0,0,0,0,0,0,0)

# این مقدار را جداگانه ذخیره میکنیم
# zero() --> cls(0,0,0,0,0,0,0)

#ppp = Point.zero()
#sss = Point.zero()
#rrr = Point.zero()
#hhh = Point.zero()

#zero()  =  یک Factory Method است (متدی که آبجکت با مقادیر پیش‌فرض می‌سازد)

####

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f" {self.x} {self.y} "
    
    def draw(self):
        print(f"Point({self.x},{self.y})")

point = Point(1, 2) 
print(point) # <__main__.Point object at 0x015182B0>

####

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):          # موقع پرینت از این منطق استفاده میشه
        return f"{self.x,self.y}" #اینجا منطق را پیاده سازی کردیم
    
    def draw(self):
        print(f"Point({self.x},{self.y})")

point = Point(1, 2) 
print(point) #>>> (1, 2)

####

# __eq__(self, other): ==
# __ne__(self, other): !=
# __lt__(self, other): <
# __gt__(self, other): >
# __le__(self, other): <=
# __ge__(self, other): >=
    
####

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y # منطق برابر بودن را اینجور ست میکنیم

point = Point(1, 2)
another = Point(3, 4)

print(point == another) # False
# اگر __eq__ را تعریف نمیکردیم منطق ما برابر بودن مقدار ها نبود بلکه مکان حافظه بود 

####
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y # منطق بزرگتر بودن ست کردیم

point = Point(5, 6)
another = Point(3, 4)

print(point > another) # True
print(point < another) # False
# چون __gt__ صدا زدم منطق پایتون علامت کوچک تر از فلان  را هم درک کرده با اینکه باید مجیک متد __lt__ را صدا میزدیم

####

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other) :
        return (self.x + other.x , self.y + other.y) # وقتی دو ابجکت جمع میشوند از این منطق پیروی میشود

point = Point(5, 6)
another = Point(3, 4)

print(point + another) # (8, 10)

####
# # نتیجه اینکه برای بعضی از عمل ها در کلاس ها باید مجیک متد  را صدا زد  __x__

#### VIDEO TIME 7 : 40 ↑↑↑↑   END OF THIS FILE




