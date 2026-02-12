# NAME OF THIS FILE : item9.py

matrix = [[1,2], [3,4], [5,6]] 

print (matrix[0]) #>>>  [1, 2]
print (matrix)    #>>> [[1, 2], [3, 4], [5, 6]]

####

zeros = [0]* 10
print (zeros) #>>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(len(zeros)) #>>> 10

####

print ([[1,2],[3,4]]* 3) # >>> [[1, 2], [3, 4],     [1, 2], [3, 4]     ,    [1, 2], [3, 4]]

####

first    = [1, 2, 3]
last     = ["4", "5"]
combined = first + last 

print (combined) #>>> [1, 2, 3, '4', '5']

####

numbers_1 = list(range(21))     #range(21)  = 0, 1,..., 19, 20 
numbers_2 = list(range(1, 21))  #range(1,21)= 1, 2,..., 19, 20
chars = list("hello world")     

print (numbers_1) #>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print (numbers_2) #>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(chars)      #>>> ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

print(len(chars)) #>>> 11

####

letters = ["a", "b", "c", "d"]

print(letters[1])  #>>> b
print(letters[0:3])#>>> ['a', 'b', 'c']

####

letters = ["a", "b", "c", "d"] 
letters[0] = 2
print(letters) #>>> [2, 'b', 'c', 'd']

####

numbers =list(range(21)) # 0 -> 20

print(numbers)      #>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numbers[1:5]) #>>> [1, 2, 3, 4]
print(numbers[-1])  #>>> 20
print(numbers[3])   #>>> 3
print(numbers[::2]) #>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(numbers[::-1])#>>> [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-2])#>>> [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
print(numbers[::2]) #>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# [key] or [index]

# [start  :  end  ]
# [start  :  end  :  shart]

# esm_iterabel[]  این ترکیب داره به مقدار یا مقدار های خاص با ایندکس مشخص اشار میکنه 
# esm_iterabel[] --> values

####

numbers = [1, 2, 3]

print(*numbers) # >>> 1 2 3      * omad baar hkali listemono kard

####

numbers = [1, 2, 3]

first , second , third = numbers

print (first , second , third ) #>>> 1 2 3

print(type(first)) # <class 'int'>
####

numbers = [1, 2, 3, 4, 5, 6]

first , second , *others = numbers    # inja * miad baghie bur list khali mikone dakhel others

print (first , second , others )  #>>> 1 2 [3, 4, 5, 6]
print (first , second , *others ) #>>> 1 2 3 4 5 6            # inja * miad bar others ghali mikone

####

numbers = [1, 2, 3, 4, 5, 6]

first , *others , second = numbers

print (first , second , others) #>>> 1 6 [2, 3, 4, 5]
print(first  , others , second) #>>> 1 [2, 3, 4, 5] 6

print (first , *others, second) #>>> 1 2 3 4 5 6
print (first , second , *others)#>>> 1 6 2 3 4 5
