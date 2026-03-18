print("hello world")

if 4>2:
    print("True")
    # indentration

a = '''
this is my ball
jgjhfgjhgh
ghhuieghdjkdfghd
gjhdywhh
'''
print(a)

#this is my name
#guidghjwejk

#snake case: my_name_is _ab
#camel case: myNameIsAb
#passcal case:MyNameIsAb

print(10 == 9) 
print(10<=9)

A = 300
B = 50

if A < B:
    print("A is greater than B")
else:
    print("B is not greater than A")

print(bool("big"))
print(bool(24))

C = "fat"
D = 23

print(bool(C))
print(bool(D))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

class myclass():
    def _len_(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

a = "Suleman"
print(a.casefold())

a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = f"My name is John, I am {age}"
print(txt)

s = "my school bag"
print(s.center(46))

if 5 > 2:
  print("Five is greater than two!")

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([80000,65000,31000,7500])
plt.title("linegraph")
plt.subplot(2,2,1)
plt.plot(x,y)
plt.show()