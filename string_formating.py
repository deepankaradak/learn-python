# String Formatting
name = "John"
print("Hello %s!" % name)

name1= "Mirch"
age = 55
print("%s is %d Years old" % (name1, age))

mylist= [1, 2, 3]
print("A list is %s" % mylist)

# Exercise
'''You will need to write a format string which prints out the data using the following syntax: 
Hello John Doe. Your current balance is $53.44.'''

name2= "John Doe"
Curr_balance = 53.44
print("Hello %s. Your current balance is $%s." % (name2, Curr_balance))