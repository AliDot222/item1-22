# NAME OF THIS FILE : item11.py

#dar inja(append va insert va pop va ...) ba nam method shenakhte mishan
#dar inja(letters) ba naame moteghaier 
#dar inja([]) ba naame list
#dar inja(har chiz ke dakhele liste ) behesh migan onsor
# be har harf daron iek string migan karakter masalan  "hello word"   'h' iek karakter dar in string ast
########
x = ["a", "b" , "c"]
y = x[0] # x ba index 0 beriz toye y
print(y) #>>> a

####

letters = ["a", "b", "c"]
letters.append("d")                #append == add == afzodan
print(letters) #>>> ['a', 'b', 'c', 'd']

#####

letters = ["a", "b", "c"]
if "z" not in letters :
    letters.append("z")
print (letters) #>>> ['a', 'b', 'c', 'z']

####

browsing = [1, 2, 3]
browsing = ['a'] + browsing + ['z']

print(browsing)  # ['z', 1, 2, 3, 'z']

####

letters = ["a", "b", "c"]
#index  = [ 0    1    2 ]
letters.insert(0 , "d")       
letters.insert(2 , "z")             #insert == dakhel kardan 
#name.insert(index, onsor)
print(letters) #>>> ['d', 'a', 'z', 'b', 'c']
                   #[ 0    1    2    3    4 ]
####

letters =["a", "b", "c", "d", "f"]
letters.pop() # hazf akharin onsor -> 'f'
letters.pop(0) # hazf onsor ba index 0 -> 'a'

####

letters = ["a", "b", "c", "d"]
x = letters.pop()

print(x) #>>> d
print(letters) #>>> ['a', 'b', 'c']

####

letters = ["a", "b", "c", "d", "f"]
letters.remove("c")                  # agar onsor nabood -> error
if "z" in letters :
    letters.remove("z")
print(letters) #>>> ['a', 'b', 'd', 'f']


####

letters = ["b", "a", "b", "c", "b", "h", "b"]
letters.remove("b")# faghat iek  "b" ro az samt chap hazv mikone 
letters.remove("b")# hazv "b" dovom
print(letters) #>>> ['a', 'c', 'b', 'h', 'b']

####                                          

letters    =      ["a", "b", "c", "z", "n", "h", "f"]
#shomare index >>#[ 0    1    2    3    4    5    6 ]                                 
del letters [2:5]#[           2    3    4           ] 
#del letters [6] #gheir ghabel ghabole chon bad az amaliat del[2:5]
#                #tedad 3 onsor hazf shode vatedad onsor ha be 4
#                #onsor taghir karde 
del letters [1]
print(letters) #>>> ['a', 'h', 'f']

####


letters    =      ["a"]

if letters[4] :
    del letters[4]


####
letters =["a", "b", "c"]
letters.clear()     
print(letters)

####

letters =["a", "a", "b", "c", "d", "b"]

print(letters.index("b")) #>>> 2              #peida kardan "andis" ia "index"
#                                             #iek onsor ba seda zadan oon     
#                                             #amaa agar do "b" masalan dashte bashim index "b" digar ra nemidahad 
if "z" in letters :
    print(letters.index("z"))
else : print("'z' Not found") #>>> 'z' Not found

if "a" in letters :
    print(letters.index("a"))  
else : print("'a' Not found") #>>> 0

####

letters =["a", "b", "c", "d", "a", "a"]

print(letters.count("a")) #>>> 3                
print(letters.count("b")) #>>> 1                   #counte = shomaresh kardan
print(letters.count("w")) #>>> 0 

####

# list.append()
# list.insert( , )
# list.pop()
# list.remove()
# list.clear()
# list.index()
# list.count()

# del list[]


####

lst = [ "reza", "ali", "mina", "ali", "hossein" ]

lst = [x       for x in lst        if x != "ali"] 
# for x in lst  --> aval x bia done done az lst bardar
# if x != "ali" --> agar shart baraie x bargharar bood bia va
# x             --> x bargardon 


print(lst) # >>> ['reza', 'mina', 'hossein']

####


numbers_1 = [7, 10, 15 , 3 , 8, 2]
numbers_2 = [7, 10, 15 , 3 , 8, 2]

numbers_1.sort() #sort == moratab kardan  #sort dar halat aadi be sorat soodi moratab mikone
numbers_2.sort(reverse=True) #reverse  = iek kibord Argument va baraie nozoly kardan liste tavajoh shavad list har che bood miad va nozoli mikonaesh va moratab nemikone!

sorted(numbers_1)
sorted(numbers_1 , reverse= True)     


     
####

items = [
    ("product 1" , 10),
    ("product 3" , 9 ),
    ("product 2" , 12)
]


items.sort()  # inja be sorat pish farz dare item haro bar asas 1,2,3 moratab mikone

print(items)

####

items = [
    ("product 1" , 10),
    ("product 3" , 9 ),
    ("product 2" , 12)
]

def sort_item (x) :                                          #parametr mitone har esmi dakhelesh bezarim mesl go , ali , ... bad ono dar edame seda bezanim
    return x[1]#iek function tarif kardim be esm sort_item va parametr (x) ke karesh ine ke index haie shomare 1 ro kharej kone

items.sort(key = sort_item)  #dar inja function ke tarif kardim be onvan key baraye sort seda mizanim

print(items)

####

items = [
    ("product 1" , 10),
    ("product 3" , 9 ),
    ("product 2" , 12)
]

#         #(aem1 =  esm2: esm2 [shomare onsor baraie baresi])
items.sort(key=lambda x: x[1]) 
print(items)                                    #lambda > asusan ie function bi nume ke mitonim on ro be iek function dige be onvan vorodi bedim
#                                                #kholase code baraie anjam in kar bedon niaz be def 

####

items = [
    ("product 1" , 10),
    ("product 3" , 9 ),
    ("product 2" , 12)
]  #(     0        1 )

for item in items :     
    print(item)         
print("#######################")
prices = []

for item in items :
    prices.append(item[1]) 
    
print (prices) #>>> [10, 9, 12]
print("#######################")
prices_2 = []

for sss in items :
    prices_2.append(sss[0])

print (prices_2) #>>> ['product 1', 'product 3', 'product 2']

####

lambda   item   :  item  [0]
# لامبدا یک فانشن بدون نامه که یک کاری رو انجام میده
# لامبدا ورودی به نام آیتم میگیره
# و مقدار عنصره با ایندکس صفر از آیتم میگیره

# baraie har item ، item[0] ro bede biron

####

i = [1 , 2]
result = (lambda a : a[1])(i)

print(result) #>>> 2

####

items = [
    ("product 1" , 10),
    ("product 3" , 9 ),
    ("product 2" , 12)
]
x = map(lambda   piece  : piece  [1] , items)  #map mesl ie karkhonast ke fanction  || map(function, itreble) sakhtar koli
xy= [map(lambda   piece  : piece  [1] , items)]
y = map(lambda   item   :  item  [0] , items)  #lambda ro behesh komak mikone       || map miad amal finction ro done done ro itreble ejramikone
 

print(x,y,xy)#>>> <map object at 0x01E88160> <map object at 0x01E881C0> [<map object at 0x01E88220>]
####

items = [
    ("product 1" , 10),
    ("product 3" , 9 ),
    ("product 2" , 12)
]
prices_1 = list(map(lambda retur_n  : retur_n[1]   , items)) # [10, 9, 12]
prices_2 = list(map(lambda retur_n  : retur_n[1]*10, items)) # [100, 90, 120]
prices_3 = list(map(lambda item     :    item[0]   , items)) # ['product 1', 'product 3', 'product 2']
prices_4 = list(map(lambda item     :    item[0]*2 , items)) # ['product 1product 1', 'product 3product 3', 'product 2product 2']

####
# lambda arguments: expression   || argument = estedlal || expression = baiian
#arguments : فهرستی از پارامترهای جدا شده با کاما
#expression:عبارت واحدی که ارزیابی و برگردانده می شود


# لامبدا میتوه دو جور ورودی بگیره یا بهش آرگومان بعدا بدیم یا مستقیم بدیم مثل دو مثال پایین
 
add_ten = lambda x: x + 10              
print(add_ten(5))  # 15

add_one = (lambda x: x + 1)(5)
print(add_one) # 6

# lambda iek x migire va in bala saresh miare --> x + 10 ia x + 1
####


#lambda    migire   :   bala saresh miare bar migardone
#lambda        in   :   out


####
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, numbers)))  # Output: [1, 4, 9, 16, 25]

# x done done az numbers bar midare
# x ** 2  natije nahaii ke barmigarde
# map() mige in amal roie hame emal kon

#####

from functools import reduce
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, numbers))  # Output: 120
print(reduce(lambda x, y: x + y, numbers))  # Output: 15

#####

points = [(1, 2), (4, 1), (5, 4), (2, 3)]
print(sorted(points, key=lambda x: x[1])) # Output: [(4, 1), (1, 2), (2, 3), (5, 4)]

#####

def fun(parameter1, parameter2):
    print(parameter1, parameter2)


fun("argument1", "argument2") #>>> argument1 argument2



####

def apply_function(f, x):
    return f(x)
print(apply_function(lambda x: x ** 2, 10)) # Output: 100

#####

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

#####

def make_incrementor(n):     #make_incrementor = afzaiesh dahande
    return lambda x: x - n

incrementor = make_incrementor(5)       #|| n = 5
print(incrementor(10))  # Output: 5     #|| x = 10

##### ساختار ساده از لامبدا

incrementor = lambda x: x - 5
print(incrementor(10))

# اینکرمنتور یک فانکشن هست
# این فانکشن طبیعیه که ورودی بگیره دیگه
# ده میشه آرگومان و ورودی به تابع ماست
# ایکس هم میشه پارامتر که در بخش عملیات فانکشن بلا سرش میاریم
# عملیات ادامش هم میشه عملایت فانکشنمون

#####

items = [
    ("product 2",15),
    ("product 3",9),
    ("product 1",25)
]
prices = [item[1] for item in items] # [15, 9, 25] 
#                                                           #filter(function, iterable)
filtred = list(filter(lambda item : item[1] >= 10 ,items)) # [('product 2', 15), ('product 1', 25)]

filtred = [item   for item in items   if item[1] >= 10]      # [('product 2', 15), ('product 1', 25)]

print(filtred)

#####

things = [(3,4), (1,2), (5,9), (10,112)]

x = [adad[1]   for adad in things]
print(x) #>>> [4, 2, 9, 112] 


####

things = [(3,4), (1,2), (5,9), (10,112)]

y =[adad[1] for adad in things   if adad[1] > 7]
print(y) #>>> [9, 112]
