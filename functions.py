# Functions
def my_function():
    print("hello world")

def function_with_arguments(username, greeting):
    print("Hello %s, From my Function!, I wish you %s" % (username, greeting))


def sum_of_two_num(a, b):
    return a + b

# call functions
my_function()
function_with_arguments("John","a greate new year!")
sum_of_two_num(1,2)

# Exercise
'''
Add a function named list_benefits() that returns the following list of strings: "More organized code",
 "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

Add a function named build_sentence(info) which receives a single argument containing a string and
 returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

Run and see all the functions work together!
'''

def list_benefits():
    return "More organized code","More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(info):
     return "%s is a benefit of functions!"% info

def end():
    list_of_benefits = list_benefits()
    for info in list_of_benefits:
        print(build_sentence(info))

end()

