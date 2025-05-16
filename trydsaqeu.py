import random
a=[1,2,3]
b=a
b.append(4)
print(a)

# string interpolation

x = random.randint(1,10)
print(f"x is {x} ") 

# string interpolation

print(1) #all numbers in python are stored in heap

c = [10,20,30,40,50]
for i in c:
    c.remove(i)
print(c)

#=====
print(bool())

##

i =1
while True:
    if i % 3 ==0:
        break
    print(i)
    
    i+=1
####
n = 10
for i in range(1,n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
n=10
for i in range(n-1,0,-1):
    print(' ' * (n-i) + '*' *(2*i-1))
###  
""" 
for i in range(1,n+1):
    print(' ' * i + '*' * (2*n- 2*i-1)) """
####

my_set = {1,2,3,4}
print(my_set)
n=5
if n in my_set:
    print("yes")
else:
    print("NO")
    my_set.update([n])
    print("new set :",my_set)
    

####

sales = ([0,2,1],[0,3,5])

users, count , amount = sales , 0 , 0

print(users)