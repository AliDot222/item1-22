# NAME OF THIS FILE : item13.py

#  () == tuple  == listie ke mitonim az rosh bekhonim
# iani faghat mitonim azash bekhonim 
# na mitonoim onsori be onsor hash ezafe konim 
# na mitonim onsoriro taghir bedim 
# na mitonim onsori ro remove konim

#be in migan kuma                         >>>>  ,  <<<<
#be in migan kolen                        >>>>  :  <<<<
#be in migan kelibreises ia hamon koroshe >>>>  }  <<<<
#be in migan brakets     ia hamon brakets >>>>  [  <<<<
#be in migan double quotation             >>>>  "  <<<<
#be in migan single quotation             >>>>  '  <<<<
#be in migan angle brackets               >>>>  <> <<<<
#####


point  =  (1, 2)
point_1 = (1, 2)   #() = tuple   ,  1 , 2 ham onsor hashan
point_2 = 1, 2     # namaieshi digar 
print(type(point)) #>>> <class 'tuple'>

point_3 = (1, 2) + (3, 4)
print(point_3)   #>>>  (1, 2, 3, 4)

point_4 = (1, 2) * 3 
print (point_4) #>>>  (1, 2, 1, 2, 1, 2)

mylist = [1, 2]
point_5 = tuple(mylist)
print(point_5) #>>>  (1, 2)

point_6 = tuple("neon")  #dar (str == string) ha be har harf migim karakter masalan ckarakter 'n'
print(point_6)  #>>>  ('n', 'e', 'o', 'n')

point_7 = (1, 2, 3, 4)

print(point_7[2])  #>>>  3
print(point_7[-1]) #>>>  4
print(point_7[0:2])#>>> (1, 2)   

#ravesh unpack kardan:
point_7 = (1, 2, 3)
x, y, z = point_7
print(x, y, z)     #>>>   1 2 3

if 1 in point_7 :
    print("exist") #>>> exist   |   exist = vojod durad

if 4 in point_7 :
    print("exist")
else :
    print("4 not found") #>>> 4 not found
    
    
point_8 = (1, 2, 3)

point_8[0] = 10

print(point_8) #>>> error / ma nemitonim tuple haro taghir bedim 

point_9 = [1, 2, 3]

point_9[0] = 10  # point_9 andis 0 ro ba 10 avaz kon

print(point_9) # >>> [10, 2, 3]

#####

from array import array

numbers = array("i" , [1,2,3])

print(numbers)

# اگر آرایه بخواهید که فقط یک نوع داده (مثلاً فقط عدد) ذخیره کند و کارایی بالا داشته باشد از این ماژول استفاده می‌شود.
# یعنی الان در مثال بالا اینتجر قبوله در لیست بالا
# اگر فلوت بهش بدی ارور میده
#ارری از نظر سرعت خیلی بهینه تر از لیست ساده هست 

#####