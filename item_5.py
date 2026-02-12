# NAME OF THIS FILE : item5.py

succsessful = True

for number in range (3) : 
    print ("attempt")
    if succsessful :
        print  ("succsessful")    
    else :
        print ("attempt 3 times and failed")
    

succsessful = False

for number in range (3) : 
    print ("attempt")
    if succsessful :
        print  ("succsessful")
        break           
    else :
        print ("attempt 3 times and failed")
        
    
    
succsessful = False

for number in range(3):
    print("attempt")
    if succsessful:
        print("successful")
        break
else:
    print("attempt 3 times and failed")

    
