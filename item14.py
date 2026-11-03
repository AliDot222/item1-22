# NAME OF THIS FILE : item14.py

x = 10
y = 20

x, y = y, x    #avaz kardan jaie x va y

print("x : ", x)  
print("y : ", y)

#####
# {} == behesh migan set  /  set == majmoee 
#set ha hamishe be tartiban va onsor haie tekrari nadaran to khodeshon
####
# ویژگی های       {set}                    
# اعضای تکراری نداره و اعضای تکراری را حذف میکند 
# ترتیب نداره پس ایندکس هم ندارد 
#  taghir pazir ast iani mishe ina estefade kard :     add    remove   
# فقط داده‌های غیرقابل تغییر می‌پذیره یعنی 
#مجاز ها (int , float, str , tupel, boolean)
# غیز مجاز (obj haie ghabel taghir , list , dict , set)
# عملیات مجموعه ای مثل اجتماع و اشتراک و اینها دارد
#سرعت بالا برای جستجو

####

numbers = [3, 1, 1, 2, 4]   # uniqoes ==bi manannd ha
uniqoes = set(numbers)
print(uniqoes)  # >>> {1, 2, 3, 4} # tavajoh set tartib khasi nadarad || inja baraie tamizi be tartibe
#####

numbers_2 = {1, 2, 3}
# print(numbers_2[0])   #>>> error    #chon > dar set ha shomare index manaii nadare
#                                      #chon dar majmoee ia hamon set hish tartibi daronesh mani nadare  
if 1 in numbers_2 :
    print ("yes")
else:
    print("no")

#####
# add    == اضافه کردن آیتم
# remove == حذف کردن آیتم
# توجه ما صرفا حذف و اضافه میکنیم اما معوم نیست کجا اضافه یا کم میشه چون ترتیب نداریم در ست 

second = {2, 5, 6}
second.add(3)
second.add(3)
second.add(3)
second.add(1)
second.remove(6)
print(len(second))#>>> 4        #len >> toool  , derazi
print(second) #>>> {1, 2, 3, 5} albate tartib moshhakhas nadreha !!

#####

numbers = [1, 1, 2, 3, 4]
a = {1, 2, 3, 4}
b = {1, 5}
print(a | b)##(a.union(b))#gereftan ejtemaie do majmoee ba estefade az karakter puip >>> | <<<
print(a & b)#(a.intersection(b))#gereftan eshterack do majmoee ba estefade az karakter amper sant >>> & <<<
print(a - b)#(a.difference(b))#amal difrense ia hamon ekhteluf
print(a ^ b)#tafazol motegharen #(a.symmetric_difference(b))#iek amal darim be esm 'cemantic difranse' ke ma mitonim in ro ba estefade az karakter keret >>> ^ <<< moshakhas konim    hamon riazi khodemone ke migoftim  : majmoee  A VA B 




