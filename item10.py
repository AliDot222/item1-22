# NAME OF THIS FILE : item10.py

letters = ["a", "b", "c"]
for letter in enumerate (letters) :    #enumerate  ==  iekaiek shomordan
    print (letter)                     #enumerate  --> (index , value)


letters = ["a", "b", "c"]
for letter in enumerate (letters) :
    print (letter[0],letter[1])

 
letters = ["a", "b", "c"]
for index , letter in enumerate (letters) :
    print (index)


letters = ["a", "b", "c"]
for index , letter in enumerate (letters) :
    print (letter)