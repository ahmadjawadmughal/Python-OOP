"""
# Q:1

x = 1
while x < 11:
    print(x)
    x += 1


# Q : 2

for stars in range(1,5):
     
    for i in range(5,0,-1):
        print(i * '*')
        
    
    

# Q : 3

a = 3
for table in range(1,11):
    print(a,'x',table, '=',table * a) 


# Q : 6


def rmkey(dict1):

    for i in dict1:
        a = dict1['b']
        

    return a
        
q = rmkey({'a':10, 'b' : 20 , 'c': 30})
print("b:",q)

#Q:4


def fib(n):
    for i in n:
        a = i + i
        
    return a
        

print(fib([0,1,1,2]))


#Q:5

import re

txt = "x is 10 and y is 20"
re.search = (r"\d\d",txt)
"""
"""
x = 123
print(x.reverse())
        


# for practice

def add(x):
    return (x+x)
a=add('1')
print("Output:",a)

# and
A = ['1','2','3']
for a in A:
   print(2*a)
    

# and

for i in range(1,5):
    if i != 1:
        print(i)



# Rectangle



arr = [29,9.0,6,8]
for i in enumerate(arr):
    print("arr:",i)


for i in range(0,100,10):
    print("range of 10:", i )




dict1 = {"a":90,"b":100000}
for i in dict1:
    print(i)


print("values of dict1:",dict1.values())
a = dict1.values()
print(type(a))
for value in a:
    print("value Iterate:",value)
print("keys of dict1:",dict1.keys())
b = dict1.keys()
print(type(b))








for key,value in dict1.items():
    print(key)



for i in enumerate(dict1):
    print(i)


for i in dict1.key():
    print("keys",i)


# class

class Person:

    country = "Pakistan"
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname


    def __str__(self):
        
        return f"{Person.country},{self.fname},{self.lname}"

obj = Person("Kate","Alison")
print(obj)
"""

# create an animal class
# craete constt variables
# Instance variable
# str method
# create an object
# access attribute of objects
# access complete object.

class Animal:

    define = "Properties of"
    def __init__(self,specie,breed,origin,lifespan,eye_color):
        self.specie = specie
        self.breed = breed
        self.origin = origin
        self.lifespan = lifespan
        self.eye_color = eye_color


    def __str__(self):
        
        return f" {Animal.define} {self.specie}:- breed:'{self.breed}',origin:'{self.origin}',& avg_lifespan:'{self.lifespan}',eye color: mostly '{self.eye_color}'"

obj = Animal("😽","Ragdoll","Riverside",13,"Blue")

new_obj =  Animal("😽","Scot Fold","Scotland",15, "Copper")

rabbit = Animal("🐇","Netherland Dwarf rabbit","Netherland",12,"Brown")

print("cat breed:",obj.breed)
print("\n")
print("cat lifeSpan:",obj.lifespan)
print("\n")
print("cat eyeColor:",obj.eye_color)
print("\n")
print("cat origin:",obj.origin)
print("\n")
print("2nd cat breed:",new_obj.breed)
print("\n")
print("2nd cat avg_lifespan:",new_obj.lifespan)
print("\n")
print("2nd cat eye color:",new_obj.eye_color)
print("\n")
print("Origin of 2nd cat:",new_obj.origin)
print("\n")
print(rabbit)
print("\n")
print(obj)
print("\n")
print(new_obj)
















    





























    



























 
