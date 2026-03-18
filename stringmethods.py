#3rd 05 friday
data_of = "my age and my total price "
print(data_of.format( age ='48', my_total_price = "4763" ))
print(len(data_of))
res = data_of.format(age = {'30'}, price = ['140'])
print(res)
print(data_of.format())
txt = "for only dollars!"
print(txt.format(price=49))
ress = data_of.capitalize()
print(ress)
joined_data = txt.join(data_of)
print(joined_data)
saved = data_of.center(40, "a")
print(saved)
print(len(saved))

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:10])

b = "Hello, World!"
print(b[4:11])

b = "Hello, World!"
print(b[-12:-1])

a = "Hello, World!" # use to capitalize a code 
print(a.upper())

my = "hello abdul" # use in case sensitivity
print(my.lower())

a = " Hello, abdul"
print(a.strip()) # use in removing space from both the begining/end of code

a = "Hello, World!"
print(a.replace("W", "J")) # use to replace a code 

a = "Hello, World!"
print(a.split(",")) # split codes
a = "hello - abdul"
print(a.split("-"), a.replace("h","A"))

a = "Hello"
b = "World"
c = a + " " + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
dd = f"my name is john, i am {36}"
print(dd)

calls = 74 
received = f"my name is abdul, 'i am {calls + 34}'"
print(received)

tt = "my name is abdul and with me is \"saleem\""
print(tt)


score = 8456
my_score = f"my price is {score:2f} for tea"
print(my_score)

print( "is this a cat \\ a dog") # \\  in a sentence gives one blacklash

sf = "this is my book and\tthat belong to him "
print(sf)

txt = "Hello\bworld!"
print(txt) 

bb =("this is my book")
print(bb.capitalize())
print(bb.title())

jj = "this is my book and that belong to him "
kk = jj.center(90,"s")
print(kk)
print(len(kk))

nn = "this is my book and that belong to him "
print(  nn.encode())

Sf = "this\tis\tmy\tbook\tand\tthat\tbelong\tto\thim "
print(Sf.expandtabs(4))

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

