# NAME OF THIS FILE : item18

#( syntaxEroor ): ke iany ma syntax eshtebah neveshtim va 
#( valueEroor ) : ke iani ma meghdar eshtebah vared kardim 
#(index error) :
# be mesal haie zir dehgat konid 



#####

try :
    num = [1,2]
    print(num[5]) #>>> IndexError: list index out of range || be in modell erorr migim exeption iani estesna 
except IndexError :  
    print("error 1 : index error in line 11")

#####

# age = int(input("age:")) #agar harf vared konim >>> ValueError

######
try:
    age = int(input("age: "))
    # Put any other code here that might raise an exception.
except ValueError: #iani agar except valueError dad in karo bokon :
    print("error 2: ValueError")
else :
    print("no exception thrown") 
    
#####

try:
    age = int(input("sen khod ra vared konid: "))

except ValueError as ex:
    print(ex)
    print(type(ex))
    print("error 2: ValueError")
else :
    print("no exception thrown")

#####

try:
    age = int(input("sen khod ra vared konid: "))
    xfactor = 10/age
except ValueError:
    print("error 2: ValueError")
except ZeroDivisionError :
    print("age can not be 0")
else :
    print("no exception thrown")

#####    #video > ( 6:32 - 6:44 )

try: 
    age = int(input("sen khod ra vared konid: "))
    xfactor = 10/age
    
except (ValueError, ZeroDivisionError):
    print("error 2: ValueError")
    print("age can not be 0")
else :
    print("no exception thrown")
    
#####

try:
    file = open()   #file dar nja iek esm moteghaier hast ie esm sade
    age = int(input("age:"))
    sss = 10/age
except ValueError :
    print("ValueError  !")
else :
    print("ok")
finally :
    file.close() #baraie bastan fili ke baz kardim (dar akhar)
    
#####

try:
    with open("namefile1" , 'r') as file , open("namefile2", 'w') as target :
        print("file oppend")
    age = int(input("age:"))
    sss = 10/age
except Exception :
    print("Erorr !!")
else :
    print("ok")

#####

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed") 

######

def calculate_xfactor(age):
    if age == 0:
        raise ValueError ("ValueError")
    return 10/age

try :
    result = calculate_xfactor(-1)
    print(result)
except ValueError as ex :
    print(ex)

######

def calculat_xfactor(age) :
    if age == 0 :
        raise  ValueError("age can not be 0 or less")       #raise => baraie partab exseption ia estesna dar function def 
    return 10/age  


try:
    result = calculat_xfactor(0)
    print(f"age:{result}")

except ValueError as ex:
    print(ex)
    
#####

print((lambda age: 10/age      if age != 0    else    exec('raise ValueError("age can not be 0 or less")')  )(100)) # ba mesal paiin tavajoh kon dar inja (100) jaigahesh mesl (rang(5)) dar code paiine || exec() hamon care exept ro anjam mide vali be sorat khati
#####
print(          list(map(lambda x: x * 2, range(5)))     ) # Output: [0, 2, 4, 6, 8]
#####
print((lambda x : x * 2)(100))               #>>> 200
print(list(map(lambda x : x * 2 , [1,2,3]))) # [2, 4, 6]
print(lambda x : x * 2 ,100)   #>>> <function <lambda> at 0x00000205899B8A40> 100

#####

def calculat_xfactor(age) :
    if age <= 0 :
        raise ValueError("age can not be 0 or less")       #raise => baraie partab exseption ia estesna dar scop ha 
    return 10/age

try:
    calculat_xfactor(-1)
except Exception as ex:
    print(ex)

#####

from timeit import timeit #karbord majhol timeit gereftan zaman baraie ghete code || import timeit iani gharar bede timeit ro allan ma dar code paiin timeit ro seda zadims kenar print

code1 ="""
def calculat_xfactor(age) :
    if age <= 0 :
        raise  ValueError("age can not be 0 or less")       #raise => baraie partab exseption ia estesna dar function def 
    return 10/age

try:
    calculat_xfactor(-1)
except Exception as ex:
    pass
"""
print(timeit(code1,number=1000)) # in code ro 1000 bar tekrar kon va neshon bede cheghadr zaman bord

#####

from timeit import timeit 

code2 = """
def calculat_xfactor(age):
    if age <= 0 :
        return  None
    return 10/age

xfactor =  calculat_xfactor(-1)
if xfactor == None:
    pass
"""
print(timeit(stmt=code2, number=1000))

##### video_time => ( 6:32 - 6:50 )  ^^^

def calculat_xfactor(age):
    if age <= 0 :
        raise  ValueError("erorr")
    return 10/age

try:
    xfactor =  calculat_xfactor(-10)
    print(f"10/age :{xfactor}")
except (ValueError , TypeError ) as ex:
    print(ex)

####
try:
    number = int(input("adad vared konid: "))
    result = 10 / number
    file = open("file.txt", "r")
    
except Exception as error:
    print(error)
    print(type(error).__name__)
    e = type(error).__name__
    
    if e == "ValueError":
        print("Lotfan yek adad motabar vared konid!")
    elif e == "ZeroDivisionError":
        print("Adad nemitavanad sefr bashad!")
    elif e == "FileNotFoundError":
        print("File peyda nashod!")
    else:
        print(f"Khata-ye nashenas: {error}")

# END OF THIS FILE