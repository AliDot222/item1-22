# NAME OF THIS FILE : item21

####  8 : 37  ↓↓↓↓ FIRST OF THE FILE  

from abc import ABC, abstractmethod

class InvalidOperationError(Exception): # حالا این متد همه ویژگی های پدر را به ارث برده
    pass

class Stream(ABC):        # ABC یعنی ما نیتونیم دیگه از این کلاس آبجکت به وجود بیاریم
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("stream is already close")
        self.opened = False

    @abstractmethod  # این باعث میشه که هرکلاسی بخواد از استریم ارث بری کنه باید همچین متدی را در خودش داشته باشه
    def read():    
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    pass

class MemoryStream2(Stream):
    def read(self):
        pass

f = FileStream() 
n = NetworkStream()

e = MemoryStream()  #>>> Erorr چون متد رید را نداره 
e2= MemoryStream2() 

####

from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

te = TextBox()
dr = DropDownList()


def draw(obj):
    obj.draw()

draw(te)
draw(dr)

####

from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

te = TextBox()
dr = DropDownList()

def draw_list(objs):
    for obj in objs:
        obj.draw()

draw_list([te, dr])

####

class TextBox():
    def draw(self):
        print("TextBox")

class DropDownList():
    def draw(self):
        print("DropDownList")

te = TextBox()
dr = DropDownList()

def draw_list(objs):
    for obj in objs:
        obj.draw()

draw_list([te, dr]) 



#### 9 : 51  ↓↓↓↓

class Text(str):
    def duplicate(self):
        return self + self

text = Text("Python")
print(text.duplicate())

####

class TrackableList(list):
    def append(self, object):
        print("append called")
        super().append(object)

list = TrackableList()
print(list.append("1"))

####

class TrackableList(list):
    def __init__(self, *args):
        super().__init__(args)  # args tuple رو تبدیل به list می‌کنه
    def append(self, item):
        print("append called")
        super().append(item)

my_list = TrackableList(0, 1, 2, 3)
print(my_list)  # [0, 1, 2, 3]


#### 9 : 57  ↓↓↓↓

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x ==  other.x  and  self.y == other.y       
    
p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2) #>>> True

### raveshi behtar
# اگر کلاسی داشتیم که قرار بود دیتا ذخیره کنه بیاییم از نیم تاپلد استفاده کنیم

from collections import namedtuple

# class_name = "Class"
# fields = ["x", "y"]

PO = namedtuple("Class", ["x", "y"])

p2 = PO(1, 2) # ia Class(x=1, y=2)
p1 = PO(1, 2) # ia Class(x=1, y=2)

print(p1)         #>>> Class(x=1, y=2)
print(p2)         #>>> Class(x=1, y=2)
print(p1 == p2)   #>>> True

p1.x = 3 # Erorr عمل ست کردن نداریم

####  9 : 0  ↑↑↑↑ END OF THE FILE 
