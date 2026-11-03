# NAME OF THIS FILE : item17

numbers = [1, 2, 3]
print(numbers[0], numbers[1], numbers[2]) #>>> 1 2 3
print(*numbers) #>>> 1 2 3 || dar inja * omade bar maro khali karde va * baraie har chizi ke ghabel peimaiesh bashe karbodie || * = azterix
# * miad bar ro khali mikone mesl ranande neisan mashti
#####

values = list(range(5))
values = [*range(5)]
print(values) #>>> [0, 1, 2, 3, 4]
print(*range(5)) #>>> 0 1 2 3 4   #  * = ranande neisan   omad bar haro khali karde 

#####

chars = [*"hello"]
print(chars) #>>> ['h', 'e', 'l', 'l', 'o']

#####

first = [1, 2]
second = [4, 5]
values = [*first, 10, *second, *"hello"]
print(values) #>>> [1, 2, 10, 4, 5, 'h', 'e', 'l', 'l', 'o']

#####

first = {"x" : 10}
second = {"x" : 2, "y" : 5}
combined = {**first, **second}   
print(combined) #>>> {'x': 2, 'y': 5}  
#dar inja omade "x" : 2 gharar dade dar python akharin amal emal mishe be mesall badi tavajoh konid

#####

print({"a" : 1, "b" : 2, "a" : 3}) #>>> {'a': 3, 'b': 2}

# END OF THE FILE