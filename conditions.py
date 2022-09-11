# Conditions
x = 2
print(x == 2)
print(x == 3)
print(x < 2)
print(x >= 2)
print(x <= 2)


name= "john"
age = 23
if name == "john" and age == 23:
    print("your name is john and your age is also 23.")
if name=="john" or name == "rock":
    print("your name is either john or rock")


name1= "rock"
if name in ["john", "rock"]:
    print("Your name is in the list")

statement = False
statement2 = True

if statement is True:
    pass
elif statement2 is True:
    pass
else:
    pass



n= 3
if n == 2:
    print("yes n is equal to 2")
else:
    print("no n not equal to 2")


# "is" operator
x= [1,2,3]
y=[1,2,3]
print(x == y)
print(x is y)

#  "not" operator
print(not False)
print((not False) == (False))


# Exercise
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")