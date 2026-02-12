# NAME OF THIS FILE : item6.py

number = 100 

while number > 0 : 
    print (number)
    number //= 2          #   این علامت یعنی تقسیم کن اگه باقیمونده خورده داشت اونو حساب نکن
print ("Done")

####
# number = 200 
# while number > 0 :
#     print (number)
#     # number = number //2    #or
#     number //= 2             #or 


# 25 / 2 = 12.5
# 25//2 =  12.0

# 3 /2 = 1.5
# 3//2 = 1.0

### در پایین یسری کد میبینی که ما با شرط کاری کردیم که اجرا نشن هیچ جوره چون همواره و همیشه فالس هستند

# شرط ساده
if False:
    print("این هرگز اجرا نمی‌شود")
    x = 10

# با پرانتز (اختیاری)
if (False):
    print("این هم اجرا نمی‌شود")

# شرط با else
if False:
    print("اجرا نمی‌شود")
else:
    print("in code ejra mishe")


#if True : 
#    code in bakhsh ejra mishe

#if False :
#    code in bakhsh ejra nemishe


a,b,*c= [1,2,3,4]

print (a) #>>> 1
print (b) #>>> 2
print (c) #>>> [3, 4]
