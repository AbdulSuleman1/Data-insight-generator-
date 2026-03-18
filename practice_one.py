import sys
import random


print("my name is suleman")
print("my name is suleman", "abdulrahman")
print("my name is suleman, abdulrahman")
print(sys.version)
work  = 300
Work = 200
result = work + Work
print(result/10)

big = str(300)
print(big, type(big))
Big = float(big)
print(Big)

a = (random.randrange(1,90))
print(a)

s = ["sule","abdul","saleem","faruk"]
print(s, len(s), type(s), s[3])

for d in s:
    print(s,d)

if s.__contains__("s"):
    print("my data is :",True)
else:
    print("my data is :",False)


nice = "the book cost '20' while the pencile cost '39'"
print(nice.capitalize())

b = "Hello, World!"  # slincing
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:10])

b = "Hello, World!"
print(b[4:11])

b = "Hello, World!"
print(b[-12:-1])

calls = 74 
received = f"my name is abdul, 'i am {calls + 34}'"
print(received)

gsf = f"this book cost {56} naira"
print(gsf)





txt = "Good night Sam!"

x = "mSa"
y = "eJo"
z = "odnght"
w = 2
b = 5
print(str.maketrans(x, y, z))

if w > b:
    print(True)
else:
    print(False)
    


