import random 

#2nd_may
#rules in naming a variable
# variable name can start with (a-z, _)
# variable name can contain (A-Z, 0-9, _)
#variable name must not start with number or special charaters
#variable name is case sensitive

number_1 = 3000
number_2 = 2000
result = number_2 + number_1
print(result * 3)
number_22 = int("300")
print(number_22, type(number_22))

#listing
friuts = [ "apple", "banana", "cherry"]
print(friuts, type(friuts))

friutss = list( ("apple", "banana", "cherry"))
print(friutss, type(friutss))
print(random.randrange(1,101))

data_of ="hello"
print("my length character :", len(data_of), data_of[4])

for aa in data_of:
    print(data_of)


if data_of.startswith("e"):
    print("the data is :", data_of)
else:
    print("not found")


