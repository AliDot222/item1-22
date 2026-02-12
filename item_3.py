# NAME OF THIS FILE : item3.py

temperatuor = 30

if  temperatuor  > 30 : # 31,32, ...
    print("its warm")
elif temperatuor > 20 : # 21,22, ... ,30  
    print("its nice")
elif temperatuor < 20 : # 19,18,
    print("its cold")
else:
    print('...') # baraie vaghti gheir int dadan

#####

age = 10
if age >= 18 : 
    print("eligible")
else:
    print("not eligible")

#####



age = 19
message = "eligible"    if   age>= 18      else "not eligible"
print (message)

#####

def Acceptability(age): #Acceptability = ghabel ghabool boodan
    return "eligible" if age >= 18 else "not eligible"
print(Acceptability(18))



