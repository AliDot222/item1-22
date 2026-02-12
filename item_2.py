# NAME OF THIS FILE : item2.py

# ord == namayesh adady
print (ord ("a"))# >>> 97
print (ord ("A"))# >>> 65
print (ord ("f"))# >>> 102
print (ord ("s"))# >>> 115
print (ord ("l"))# >>> 108
    # har harf yek mizany dare masalan a==97 \ A==65 
    #   (==) yany alamat mosavi
print ( "ali == ali")   #Syntax not true in this way 
print ("ali" == "ali") #Syntax is True look at the output
print ("ali" <"Ali")
print ("asghar"> "ali")
    #ebteda mire donbal mizun harf aval va agar yeky bod mire baraye moghayese badia

#####

# chr(97) --> a , ord(a) 97
print(ord("س")) #>>> 1587
# Loop through the ASCII values from 1 to 20 and print the corresponding characters
for num in range(97, 123):   #ord("a") = 97  , ord("z") = 122
    print(chr(num)) 

#####
for letter in range(ord('a'), ord('z') + 1):
    print(chr(letter)) 

for letter in range(ord('a'), ord('z') + 1):
    print(chr(letter), end='') #>>> abcdefghijklmnopqrstuvwxyz

for letter in range(ord('a'), ord('z') + 1):
    print(chr(letter), end=' ') #>>> a b c d e f g h i j k l m n o p q r s t u v w x y z 

for letter in range(ord('a'), ord('z') + 1):
    print(chr(letter), end='-') #>>> a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-
#####

for letter in range(ord('a'), ord('z') + 1):
    print(f"{chr(letter)} = {letter}" , end=' | ')

alphabet_list = [f"{chr(letter)}={letter}"        for letter in      range(ord('a'), ord('z') + 1)]
print(alphabet_list) # ['a=97', 'b=98', 'c=99', 'd=100', 'e=101', 'f=102', 'g=103', 'h=104', 'i=105', 'j=106', 'k=107', 'l=108', 'm=109', 'n=110', 'o=111', 'p=112', 'q=113', 'r=114', 's=115', 't=116', 'u=117', 'v=118', 'w=119', 'x=120', 'y=121', 'z=122']

#####

print(chr(97))  # Output: 'a'
print(chr(65))  # Output: 'A'
print(chr(98))  # Output: 'b'

print(chr(97), chr(65), chr(98), sep="-" , end="     ")
print(chr(97), chr(65), chr(98), sep="-")

for i in range(97, 123):
    print(chr(i), end=' ')  # Output: a b c d e f g h i j k l m n o p q r s t u v w x y z

print(chr(8364))  # Output: '€' (Euro sign)
print(chr(9786))  # Output: '☺' (Smiley face)
