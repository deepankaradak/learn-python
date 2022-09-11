mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
# print(mylist[0])

for x in mylist:
    print(x)

mylist2 = [1, 2, 3]
# print(mylist2[10])

# Exercise
'''In this exercise, you will need to add numbers and strings to the correct lists using the
 "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 
 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using
 the brackets operator []. Note that the index is zero-based, so if you want to access the second
  item in the list, its index will be 1.'''

numbers1= []
strings1= []
names= ["james", "steffen", "rocky", "laxxy"]

numbers1.append(1)
numbers1.append(2)
numbers1.append(3)

strings1.append("hello")
strings1.append("world")

second_name = names[1]

print(numbers1)
print(strings1)
print("the second name in the name list is %s" % second_name)