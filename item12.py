# NAME OF THIS FILE : item12.py

list_1 = [1, 2, 3]
list_2 = [10, 20, 30]
print(list(zip(list_1,list_2))) #>>> [(1, 10), (2, 20), (3, 30)]
print(list(zip(list_1,list_2,"ab"))) #>>> [(1, 10, 'a'), (2, 20, 'b')]
print(list(zip(list_1,list_2,"abc"))) #>>> [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]

list_3 =[1, 2, 3]
list_4 =[10, 20]
print(list(zip(list_3,list_4))) #>>> [(1, 10), (2, 20)]  || zip miad onsor ha ba index haie barabar kenar ham dakhel tuple mizare

####

browsing = []

browsing.append(1) # afzodan az chap be rast
browsing.append(2)
browsing.append(3)

print(browsing) #>>> [1, 2, 3]  

browsing.pop()  # hazv az az rast be chap
browsing.pop()
# browsing.pop()

if not browsing :     # agar browsing listi khali bood = False --> if not (False): --> if True:
    print("disable")

print(browsing)

####

# list khali == False
# not False == True

####

from collections import deque              
#حذف و اضافه به آخر و اول لیست خیلی سریع تر 
dd = deque([])    # داریم میگیم این لیست خالی دکیو هست

dd.append(1)          # اضافه به صف از راست
dd.appendleft(0)      #اضافه به صف از چپ
dd.pop()              #حذف از راست صف
dd.popleft()          # حذف از چپ صف

print(type(dd)) # <class 'collections.deque'>


