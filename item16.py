# NAME OF THIS FILE : item16.py

value = [] 
for numbers in range(5) :
    value.append(numbers*2)
print(value) # >>> [0, 2, 4, 6, 8]
#####

#              # map(function, itrebel) >> maghadir iterabel parameter haie function hastan
def double(x): # in function ro tarif mikonim ke parametr 'x' tahvil begire va "x*2" bargardone 
    return x * 2

n = [1,2,3]

print(list(map(double, n))) # Output: [2, 4, 6]   || maghadir x be onvan parameter midim be double
print(list(map(double,[10,20,30]))) # Output:  [20, 40, 60]

#####

print(list(map(lambda x: x * 3, range(5)))) # Output: [0, 3, 6, 9, 12]

#####

value = [0,0,0,0,0] # صفرا دکوری هستند
for numbers in range(5):
    value[numbers] = numbers * 2
print(value)  # Output: [0, 2, 4, 6, 8]

#####

value = []
for numbers in range(5):
    value.append(numbers * 2)

print(value)


#####

value = []
numbers = 0
while numbers < 5:
    value.append(numbers * 2)
    numbers += 1
print(value)  # Output: [0, 2, 4, 6, 8]

#####

def multiply_by_2(x):
    return x * 2
print(list(map(multiply_by_2, range(5))))  # Output: [0, 2, 4, 6, 8]

#####

print([numbers * 2 for numbers in range(5)]) # >>> [0, 2, 4, 6, 8]

#####

point = {"z": x*2 for x in range(5)} # x = lastest in range = 4
print(point) # >>> {'z': 8}
point_2 = {x:x*2 for x in range (5)}
print(point_2) # >>> {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

#####

value_2 = (numbers*2 for numbers in range(5))
print(value_2) # >>>   <generator object <genexpr> at 0x0122A6F0> || ma mikhastim ie tuple tahvil bede amu generator object tahvil dud 

#####

value_2 = (numbers*2 for numbers in range(5))
print  (value_2) #>>> <generator object <genexpr> at 0x0148A6F0>
#generator objeckt itrebel va ghabel peimaiesh pas ma in karo mikonim :
for x in value_2:
    print(x , end=" ") #>>> 0 2 4 6 8 

##### riding :
#baraie neshon dadan size baiad madule paiin ro tarif konim 
from sys import getsizeof
value_2 = (numbers*2 for numbers in range(1000))
print("generator", getsizeof(value_2))  #>>> generator 56 || size== 56 bite

from sys import getsizeof

print("generator", getsizeof(value_2)) #>>> generator 56

from sys import getsizeof
y = (x*2 for x in range(1000))
print("generator", getsizeof(y)) #>>> generator 56

from sys import getsizeof
y = [x*2 for x in range(1000)]
print("generator", getsizeof(y)) #>>> generator 4508

from sys import getsizeof
y = [x*2 for x in range(100000)]
print("generator", getsizeof(y)) #>>> generator 412228

# END OF THE FILE