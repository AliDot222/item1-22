# NAME OF THIS PY FILE = item20.py

####  7 : 40  ↓↓↓↓ first of the file

# dict = { key1 : value1 , key2 : value2 }
# dict = {   (item1)     ,   (item2)     }

# dict[key]     = value  # به چشم مقدار همیشه ببین
# dict.get(key) = value  # یک دیکشنری به اسم دیکتر دارم که این هم کلیدشه و کل این مقداره که نشون میده برای اون کلید
# پس هروقت اینا دیدی با چشم مقدار کلید نگاهشون کن

# list[index]             = value
# list.__getitem__(index) = value
####

my_dict = {"ali" : 0}

def add(key):
    my_dict[key] = my_dict[key] + 1 # مقدار کلید + 1 کن و بریز تو مقدار همون کلید

add("ali")
add("ali")
add("ali")


print(my_dict) #{'ali': 3}

####

dict = {"a": 1}

print(dict.get("a"))     # >>> 1
print(dict.get("h"))     # >>> None
# print(dict["h"])       # >>> Error
print(dict.get("d", 12)) # >>> 12 #درسته دی مقدار دیفالت دادیم ولی برای دیکشنری ست نکردیمش

dict["c"] = dict.get("c" , 1000) # سی رو برای دیکشنریمون ست کردیم در اینجا


print(dict) # {'a': 1,'c': 1000}


####

my_dict = {}

def add(key):
    my_dict[key] = my_dict.get(key, 0) + 1

add("ali")
add("ali")


print(my_dict) # >>> {'ali': 2}

####

class BagOfWord:
    def __init__(self):
        self.words = {} # اتربیوت ورد درست کردیم و یک دیکشنری خالی برایش ست کردیم

    def add(self, key):
        self.words[key] = self.words.get(key, 0) + 1 

document = BagOfWord()

document.add("ali")
document.add("Ali")
document.add("ali")

print(document.words) # {'ali': 2, 'Ali': 1}

#### 


class BagOfWord():
    def __init__(self):
        self.words = {} 
        
    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1

document = BagOfWord()

document.add("ali")
document.add("Ali")
document.add("ALI")

print(document.words) # {'ali': 3}

####

numbers = [10, 20, 30]
print(numbers[0]) # 10               
print(numbers.__getitem__(0)) # 10   

####

class BagOfWord():
    def __init__(self):
        self.words = {} 

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1

    def __getitem__ (self, word):                 # منطق گت کردن را داریم پیاده سازی میکنیم
        return self.words.get(word.lower(), 0) # 0 زمانی برمیگردد که کلید وجود نشداشته باشد 

document = BagOfWord()

document.add("ali")
document.add("Ali")
document.add("ALI")

print(document["ali"]) # >>> 3    # اینجا اومدیم عمل گت کردن انجام دادیم و متد گت کردن صدا زده میشه

####


class BagOfWord():
    def __init__(self):
        self.words = {} # یک دیکشنری خالی به نام obj.words ساختیم

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1 #> value = value+1

    def __getitem__(self, word):
        return self.words.get(word.lower(), 1000) #> value

    def __setitem__(self, word, count):
        self.words[word.lower()] = count #> value = count

document = BagOfWord()

document.add("ali")
document.add("Ali")
document.add("ALI")

document["ali"] = 10 #داریم مقدار 10 را برای کلید "ali" ست میکنیم و قبل تر منطق مجیک متد ست کردن را تعریف کردیم 

print(document["ali"]) # 10

####

# print(dict[key])     -> # گت کردن
# print(list[index])   -> # گت کردن
# print(tupele[index]) -> # گت کردن
# print(set[index])    -> # برای مجموعه گت کردن بر اساس ایندکس وجود ندارد چون در ست ترتیب نداریم

# dict[key]     = x    -> # ست کردن
# list[index]   = x    -> # ست کردن
# tupele[index] = x    -> # برای عنصر های تاپل نمیشه مقدار ست کرد ارور میده
# set[index]    = x    -> # برای مجموعه ست کردن بر اساس ایندکس نداریم

####


class BagOfWord(): 
    def __init__(self):
        self.words = {} # یک دیکشنری خالی به نام obj.words ساختیم
        
    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1

    def __len__ (self):
        return len(self.words) #> dict len

document = BagOfWord()

document.add("ali")
document.add("Ali")
document.add("ALI")


print(len(document)) # چون 1 کلید داریم طول دیکشنری 1 هست

####

class BagOfWord():
    def __init__(self):
        self.words = {} 
        
    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1

    def __getitem__ (self, word):
        return self.words.get(word.lower(), 1000) 

    def __setitem__ (self, word, count): # روش 1
        self.words[word.lower()] = count

    def __setitem__(self, word, count):  # روش 2 بهتره
        self.words.__setitem__(word.lower(), count)

    def __len__ (self):
        return len(self.words)

    def __iter__(self):
        return iter(self.words)
    
document = BagOfWord()

document.add("ali")
document.add("Ali")
document.add("ALI")


print(len(document)) 

####

# __word -> private variable -> متغیر داخلی یا مخفی
#   word ->         variable ->              متغیر

####
class BagOfWord():
    def __init__(self):
        self.__words = {} 
        
    def add(self, word):
        self.__words[word.lower()] = self.__words.get(word.lower(), 0) + 1

    def __getitem__ (self, word):
        return self.__words.get(word.lower(), 1000) 

    def __setitem__ (self, word, count):
        self.__words[word.lower()] = count
        
    def __len__ (self):
        return len(self.__words)

    def __iter__(self):
        return iter(self.__words)
    
document = BagOfWord()

document.add("ali")
document.add("Ali")
document.add("ALI")

# __words   baraie ine as kharej class behesh dastresi nadashte bashim
print(len(document)) 

####  8 : 00  ↓↓↓↓

#میخواهیم منطق گتر و ستر را مشخص کنیم در کلاس
class Product():
    def __init__(self, price):
        self.set_price(price)
        
    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0 :
            raise ValueError("value---erorr")
        self.__price = value
        
    price = property(get_price, set_price)

product = Product(1)
product.price = 10
print(product.price) #>>> 10

#### 

class Product():
    def __init__(self, price):
        self.__price = price
        
    def __get_price(self):               #دو آندرلاین پشت برای مخفی کردن نسبت به بیرونه
        return self.__price
    
    def __set_price(self, value):
        if value < 0 :
            raise ValueError("value---erorr")
        self.__price = value
        
    price = property(__get_price, __set_price)

####

class Product:
    def __init__(self, price):       # موقع ساخته شدن آبجکت این متد صدا زده میشه
        self.__price = price

    @property
    def price(self):                  # موقع گت کردن این متد صدا میزنیم
        return self.__price

    @price.setter
    def price(self, value):           # موقع ست کردن این متد صدا میزنیم
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value

product = Product(-1)
print(product.price) # -1             # اینجا اومدیم عمل گت کردن انجام دادیم و متد گت کردن صدا زده میشه
product.price = 2                     # اینجا اومدیم عمل ست کردن انجام دادیم و متد ست کردن صدا زده میشه
print(product.price) # 2              # اینجا اومدیم عمل گت کردن انجام دادیم و متد گت کردن صدا زده میشه

####
# این مثال به برسی بیشتری نیاز دارد برای توضیحات و ستند سازی!
class Product:
    def __init__(self, price):       
        self.price = price           #  حالا setter استفاده می‌شود 
                                     # self.__price این باعث میشه متد ستر برای پرایس صدا نشه  
    @property
    def price(self):                  
        return self.__price

    @price.setter
    def price(self, value):           
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value

product = Product(-1)                #  در قبل مقدار منفی به ستر برای برسی ارسال نمیشد ولی الان میشه

print(product.price) #>>> ValueError ....

####   8 : 12  ↓↓↓↓

class Animal():                       # کلاس پدر یا کلاس سوپر 
    def __init__ (self, x):
        self.x = x

    def eat(self):
        print("eat")


class Cat(Animal):                    # کلاس فرزند یا ساب
    def walk(self):
        print("walk")

class Fish(Animal):                   # کلاس فرزند یا ساب
    def swim(self):
        print("swim")
        
c = Cat(1)

c.eat()    # eat     کلاس کت از انیمال ارث بری کرده پس متد های اونو به ارث برده ازش 
c.walk()   # walk    متد والک برای کلاس کت صدا زده میشه
print(c.x) # 1
# c.swim() # Erorr   چون کلاس کت از فیش ارث بری نکرده

#### 8 : 23 ↑↑↑↑

class Animal():
    def __init__ (self):
        self.age = 1
        
    
    def eat(self):
        print(" - eat - ")


class Cat(Animal):
    def __init__ (self):   # 
        super().__init__() # mire atrebiot pedar baresi mikone agar inkar mikardim nemiraft baresi kone chon migoft class man hkodesh method sazande dare
        self.weight = 2    

    
    def walk(self):
        print("walk")
        

c = Cat()

print(c.age)

####

# super().__init__()

# super() کلاس پدر را صدا میزند 
# .__init__() constructor function pedar ro seda mizanad

####

# jabe.pizaa.gharch # از توی جعبه پیتزا در اوردیم واز پیتزا قارچ هارو دراوردیم

# super().__init__() # از کلاس پدر متد سازنده یعنی متد این ایت رو در اوردیم و با کمک پرانتز صداش زدیم

# c.walk   # اینجا متد والک فقط نام بردیم صدا نزدیم
# c.walk() # اینجا متد والک را صدا زدیم

# super() # صدا زدن متد پدر


# پس پرانتز که جلوی متد یا فانکشن بیاد صداش میزنه

####

def ali():
    print("ali")
    
ali   # متد یا همون فانکشن علی صدا زده نشده فقط نام بردیمش و اتفاقی نمیوفته
ali() #>>> ali  اینجا با اوردن پرانتز متد یا همون فانکشن علی رو صدا زدیم

####

def ali():
    return ("ali")

print(ali()) #>>> ali

####

class Animal():
    def eat(self):
        print("eat")
        
class Bird(Animal):
    def fly(self):
        print("fly")

class Chiken(Bird): 
    pass

class Maneger(Animal, Bird):
    pass

####   ↓↓↓↓   8 : 31 

# تعریف یک کلاس خطای سفارشی که از Exception ارث‌بری می‌کند
# این خطا زمانی استفاده می‌شود که عملیاتی نامعتبر روی جریان انجام شود
class InvalidOperationError(Exception):
    """Exception raised for invalid operations on the stream."""
    pass

        

class Stream:
    def __init__(self):
        self.opened = False

    def open(self): 
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True
        print("Stream opened.")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")

        self.opened = False
        print("Stream closed.")


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")



fs = FileStream()   
fs.open()                # Stream opened.
fs.read()                # Reading data from a file
fs.close()               # Stream closed.

ns = NetworkStream()     
ns.open()                # Stream opened.
ns.read()                # Reading data from a network
ns.close()               # Stream closed.



####   ↑↑↑↑ 8 : 37 end of the file
