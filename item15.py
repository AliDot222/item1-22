# NAME OF THIS FILE : item15.py

#be in migan kelibreisez ia hamon koroshe >>>>  {}  <<<<
#be in migan berakets    ia hamon brakets >>>>  []  <<<<

#class int = class integer 
#class str = class string  
#class float = class floating       
#class bool = class boolean
#class dict = dictionarys
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# نگهدارنده های مقادیر
a = (1,2,3)
b = {1,4,3}
c = {"a":1 , "b":2}
d = [1,2,3]


## ویژگی های دیکشنری

# دیکشنری : کلید و مقدار 
# keys => str , int , tuple , bool , float , frozenset , None , enum   
# values => everything 
# دیکشنری ها قابل تغییر هستند
# از نسخه 3.7 به بعد ترتیب ورود عناصر حفظ می‌شود
# دسترسی بسیار سریع و رسیدن به مقدار با داشتن کلید

# متدهای مهم:

#   keys()   -> لیست کلیدها
#   values() -> لیست مقادیر
#   items()  -> لیست جفت کلید-مقدار

#   get(k,d) -> مقدار کلید یا پیش‌فرض
#   update() -> ترکیب/تغییر دیکشنری
#   pop(k)   -> حذف کلید و برگرداندن مقدار
#   clear()  -> خالی کردن دیکشنری

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

point_1 = dict(x=1, y=2) 
print(point_1) #>>> {'x': 1, 'y': 2}

#####

point_2 = {"x" : 1 ,"y" : 2}
print(point_2["x"]) #>>> 1 

#####

# فرمول کلی دسترسی به یک مقدار
# moteghaier[index] =  مقدار
#متغییر میتواند : دیکشنری - لیست - تاپل - استرینگ باشد 

#####

point_3 = {"x" : 1 ,"y" : 2}
point_3["x"] = 10
print(point_3)#>>>{'x': 10, 'y': 2}


#####

point_4 = {"x" : 1 ,"y" : 2}
point_4["z"] = 20
print(point_4) #>>> {'x': 1, 'y': 2, 'z': 20}

#####

point_5 = {"x" : 1 ,"y" : 2}
print(point_5["i"])#>>> error 

#####

point_6 = {"x" : 1 ,"y" : 2}
if "a" in point_6 :
    print(point_6["a"])

#####
# متد گت برای دیکشنریه
# کلید بهش میدیم
# یا مقدار یا نان برمیگردونه
# میتونیم یک دیفالت بهش بدیم اگه مقدار نبود جاش بیاد 
# اگر مقدار دیفالت بهش دادیم توی گت کردن نمایش داده میشه و ست نمیشه برای دیکشنری

point_7 = {"x" : 1 ,"y" : 2}   
print(point_7.get("x")) #>>> 1     
print(point_7.get("i")) #>>> None
print(point_7.get("s", 0)) #>>> 0 || in ianiagar kelidi be esm "s" vojod nadasht meghdar 0 ro baraie man returne kon bargardoon
print(point_7)#>>> {'x': 1, 'y': 2}

#####

point_8 = {"x" : 1, "y" : 2, "z" : 3}
del point_8["y"] # hazf iek kilid meghdar ba seda zadan kelid oon va estefate az 'del'
print(point_8) #>>> {'x': 1, 'z': 3}

#####
# خاصیت حلقه برای دیکشنری 
point_9 = {"x" : 1, "y" : 2, "z" : 3}

for key in point_9 :
    print(key) #>>> keys

for key in point_9 :
    print(point_9[key]) #>>> values

#####

point_10 = {"x" : 1, "y" : 2, "z" : 3} # items.({item , item , item , ...}) >>> (item) (item) (item)  

print(point_10.items())  #dict_items([('x', 1), ('y', 2), ('z', 3)])  

for sss in point_10.items() : #('x', 1)|('y', 2)|('z', 3)|
    print(sss , end="|")

for sss in point_10.items() : #('x', 1) ('x', 1)|('y', 2) ('y', 2)|('z', 3) ('z', 3)|
    print(sss , sss, end="|")

for key , value in point_10.items() :
    print(key , value, end="|") # x 1|y 2|z 3|

#####

point_11 = {"x": 1, "y": 2, "z": 3}

# Find the item with the value 2
for key, value in point_11.items():
    if value == 2:
        print((key, value)) #>>> ('y', 2)
        break

####

#break :
# اولین حلقه که در آن هست را میشکند و به بیرون میآید
for i in range(3):        
    for j in range(3):    
        for k in range(3): # <--  halghe inja mishekanad
            if k == 1: 
                break 
        print(i, j, k)
#تنها دو حلقه داریم : for & while

#####

for i in range(3):        
    for j in range(3):    
        for k in range(3):
            if k == 1:       # har vaght k==1 bood mire bara chap
                break        # iani k==1 beshe miam halghe mishkonam bere bara chap
        print(i, j, k)

#####

# .items() --> iek list az item haie dict mide
        
point_12 = {"y": 3, "x": 1, "z": 2}

print(point_12.items()) # Outeput : dict_items([('y', 3), ('x', 1), ('z', 2)])

sorted_by_keys = dict(sorted(point_12.items())) # bar asas x,y,z omade moratab karde
print(sorted_by_keys)  # Output: {'x': 1, 'y': 3, 'z': 2}

sorted_by_keys = (sorted(point_12.items()))
print(sorted_by_keys)  # Output: [('x', 1), ('y', 3), ('z', 2)]

sorted_by_values = dict(sorted(point_12.items(), key=lambda item: item[1]))
print(sorted_by_values)  # Output: {'x': 1, 'z': 2, 'y': 3}

sorted_by_values_desc = dict(sorted(point_12.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_values_desc)  # Output: {'y': 3, 'z': 2, 'x': 1}

sorted_custom = dict(sorted(point_12.items(), key=lambda item: (item[1], item[0])))
print(sorted_custom)  # Output: {'x': 1, 'z': 2, 'y': 3}

sorted_by_keys_case_insensitive = dict(sorted(point_12.items(), key=lambda item: item[0].lower()))
print(sorted_by_keys_case_insensitive)  # Output: {'x': 1, 'y': 3, 'z': 2}

# END OF THE FILE