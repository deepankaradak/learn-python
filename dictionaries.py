# Dictionaries
phonebook = {}
phonebook["john"] = 9902164587
phonebook["jazz"] = 9845635214
phonebook["mirch"] = 9456354412

print(phonebook)

#
phonebook1 = {
    "john":11111,
    "mirch":22222,
    "shown":33333
}
print(phonebook1)

#Iterating over dictionaries
phonebook2 = {
    "miirch": 986542,
    "shilon": 365148,
    "bhirax": 754587
}
for name, number in phonebook2.items():
    print("phone number of %s is %d" % (name, number))

# Removing a value
phonebook3 = {
    "chassy": 845672,
    "stifller": 828282,
    "rock": 888547
}
del phonebook3["chassy"]
print(phonebook3)
# or
phonebook3.pop("rock")
print(phonebook3)

# Exercise
'''
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
'''

phonebook4 = {
    "jack": 938273411,
    "Jill": 938273441,
    "Hill": 938273442
}
# print(phonebook4)
phonebook4["Jake"] = 938273443
# print(phonebook4)
phonebook4.pop("Jill")
# print(phonebook4)
if "Jake" in phonebook4:
    print("jake is now listed to the phonebook")
#
if "Jill" not in phonebook4:
    print("Jill is no more listed to phonebook")    