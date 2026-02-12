# NAME OF THIS FILE : item4.py

for number in range (4) : # range(4) = 0,1,2,3
    print ("message")

# for "esm halghe" in "vahed tedad tekrar ha" :
#    amali ke baiad tekrar beshe
#    agar "esm halghe" seda bazanim miad done done kharej mikone 

for number in range (4) : # number donedone az range kharej mikonad || number esm kol in halghe ast 
    print (number) # number az range aval 0 barmidare bad 1 bad 2 bad 3

    
for number in range (4) :
    print ("number+1")

for number in range (4) : 
    print (number+1)

for number in range (4) :
    print (number*10)

for number in range (4) :
    print (number+1 * ".")       ## error mide chon dar riaziat aval amal zarbe bad jame pass :

for number in range (12) :
      print ((number+1) * ".")

for number in range (1,4) :
    print (number)

for number in range (1,10) :
    print (number)

for number in range (1,10,2) :
    print (number)

for number in range (1,10,3) :
    print (number)

for ali in range (3) : # esm halghe = ali
      print ("salam")

for x in range (4):         
    for y in range (2) :
        print (f"({x},{y})")


for x in "python" :   # x done done karacter haro kharej mikone
    print (x)

for x in [1,2,3,4,5] : # x done done onsor haro kharej mikone
    print (x)

    
for x in range(5):
    print(x, end="_") #>>> 0_1_2_3_4_

for x in range(5): # range(5) = 0 1 2 3 4 
    if x < 4:
        print(x, end="_")
    else:
        print(x) #>>> 0_1_2_3_4


result = "_".join(str(x) for x in range(5))
print(result)

result = [x for x in range(3)]
print(type(result))  # <class 'list'>
print(result) # [0, 1, 2]

gen = (x for x in range(3))
print(type(gen))  # <class 'generator'>  // چون تاپل ها غیر قابل پیمایش هستند و جنریتور برامون برمیگردونه

code = [x        for x in range(5)] 
print(code) # [0, 1, 2, 3, 4]



# nokte :     ord(str) --> true      ord(not str)  --> error
if False :
    hx = 2
    print (ord(hx) - ord(0)) #>>> 50 - 48 = 2

hx = "2"
print (ord(hx) - ord("0")) #>>> 50 - 48 = 2

###

for x in range (3): # range (3) ->0,1,2 ||| pas scope 3 bar ejra mishe
    print (x)

for x in range (3): # range (3) ->0,1,2 ||| pas scope 3 bar ejra mishe
    print ("hello") # 3 bar hello neveshte mishe
    

# for esm in iterable : # tedad iterabel = tedad ejra shodan scope
#     print(esm)
#     print("hi")
