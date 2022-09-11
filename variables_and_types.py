#1 integer point

myint= 7
print(myint)

#2 floting point

myFloat = 7.0
print(myFloat)

myFloat2= float(7)
print(myFloat2)

#3 strings

string1= "Hey Brother!"
print(string1)

string2= 'hello sir, how was your day'
print(string2)

# string3 = 'Don't worry about aphostrophys'
string4= "Don't worry about aphostrophys"
print(string4)

# simple operator

one =1
two= 2
three= one + two
print(three)

state1= "Hello"
state2= "World!"
result= state1+ " " + state2
print(result)

# Assignments

a, b = 1, 2
print(a, b)

a1= 1
a2= 2
s1= "hello"
# result2= a1+ a2+ s1
# print(result2)

# exercise
'''The target of this exercise is to create a string, an integer, and a floating point number.
 The string should be named mystring and should contain the word "hello". The floating point 
 number should be named myfloat and should contain the number 10.0, and the integer should be
  named myint and should contain the number 20.'''

mystring1 = "hello"
myfloat = 10.0
myint = 20

if mystring1 == "hello":
    print("String: %s" % mystring1)
if isinstance(myfloat,(float)) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint,(int)) and myint == 20:
    print("Integer: %d" % myint)

