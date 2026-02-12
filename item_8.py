# NAME OF THIS FILE : item8.py

def ali (hi) : # dastor def baraie tolid function || 'ali' esm function || 'hi' parametr 
    print(f"{hi}") 
ali("salam") #>>>     salam
####

def ali (hi) :
    return (f">>>{hi}<<<")
print(ali("salam")) #>>>    >>>salam<<<

####

def ali (hi) :
    print(f"yooo  {hi}")  #>>>  yooo  salam 
print(ali("salam"))       #>>>  None // print dovomi ino barmigardone

#####

def greet (first_name) :
    print (f"hi {first_name}")

def ali (ghabol_shodan) :
    print (f"mobarake{ghabol_shodan}")

greet ("reza") #>>> hi reza
ali ("ghabool shodid :D") #>>>mobarakeghabool shodid :D

#####

def greet (first_name , last_name) :
    print (f"hi {first_name}___{last_name}__123456")
greet ("reza","morudi") #>>> hi reza___morudi__123456

####

def greet ( first ,second ) :
    print (f"hi {first} {second}")
greet ("x","y") #>>> hi x y

####

def greet () :
    print ("hi everyone")
def ali () :
    print ("///hi///")

greet() #>>> hi everyone
ali()   #>>> ///hi///
greet() #>>> hi everyone
greet() #>>> hi everyone
 
#####

def greet () :
    print ("ali")

greet() #>>> ali

######

def greet2 (firt_name) :
    return (f"hi {firt_name}")
message = greet2 ("MOHAMMAD")
print (message)

#######

def greet (name) :
    return f"{name}"
message = greet("b")
print (message)

####

def get_greeting (first_name) :
    return f"hi {first_name}"
message = get_greeting ("neon")
file = open("item8_line76.txt","w")
file.write(message)

####

message = "z"


def greet(name) :
    return  f"{name}"
peigham = greet("b")

print(message)
print(peigham)

####

def multiply (*numbers) :
    total = 1000                         # total = shoro avalin zarb
    for number in numbers :
        total +=  number   #== total = total + number || total ra jam dar number kon va total ra bar gardon 
    return total 
print (multiply(2, 2, 4, 6))  #multiply   =    1000  + 2 + 2 + 4 + 6   =    1014

def multipl (*numbers) :
    total = 0
    for number in numbers :
        total += number        # vaghti tamam numbers ha tamam mishan akharin number ham be dron total rikhte mishe va total az halghe miad biron
    return total               # total ke omad biron tavasot return bazgasht dade mishe
print (multipl(2,3,5)) #>>> 10


def mult (*numbers) :
    print(numbers)
    total = 1
    for num in numbers :
        total += num
    print(total)


mult(1,2,3)


def save_user(**user):   # ** میاد بار به صورت یک دیکشنری خالی میکنه
    print(user)
    print(user["id"])


save_user(id=1 ,name = "ali" ,age=32 )  #>>> {'id': 1, 'name': 'ali', 'age': 32}
#                                       #>>> 1

####

def save_user(**user):  
    print(user)
    print(user["id"])


# save_user(1 , "ali" , 32 ) # >>> Erorr 
# save_user(id : 1 , name : "ali" , age : 32 ) # >>>  Erorr 



