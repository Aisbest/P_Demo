import math
print("helloworld")
print("*"*10)


'''
linting
debugging
autocompletion
code formating :make coed clean and readable
unit testting
code snippets
'''
print("hello")

x = 1
y = 2

'''
ctrl+alt+n code runner
ctrl+shift+p 
ctrl+` terminal
'''

# variable
student_count = 1000
print(student_count)
is_published = False
# boolean value should start with capital character
course_name = "python programming"
# make sure variable useable and meaningful and describable, it can make your code more maintainable
# can't have sapce on variable name,if we put letters together,it's a bit hard to read
# don't use dirty code


# string
# can use triple quotes to format long string
message = """
Dear professor

"""

# python interpreter sees the second string as the end of the string
# 1 way:use single quotes betweend begin and end,use double quote in the middle of the string
# 2 way:use \,\ is a escape character
# here are another escape character list:\",\',\\,\n
course = "python \nprogramming"
print(course)

# build in function
# what is function? function is basically a reusable piece of code that cary out a task
print(len(course_name))
# number of characters in that string
# get specific character
print(course_name[0])
# negitive index
print(course_name[-1])
# same syntax
print(course_name[0:3])
# what if we don't include start index?
print(course_name[0:])
# what if we don't include end index?

first = "kirin"
last = "sue"
# full = first + " " + last
# format string
# format string is an expression that will be evaluated at run time
full = f"{first} {last}"
print(full)

# everything in python is an object? objects have functions we called methods that we can access use . character
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)


# numbers
# standard operators: + - * / // % **
# integer number  float number  complex number
# two types of division sign
# get float result
print(10 / 3)
# get integer result
print(10 // 3)
# remainder of division
print(10 % 3)
print(10 ** 3)

print(round(2.9))
print(abs(-2.9))

# math module
# module is like a seperated file with some python code,so python we have math module which include lots of mathmatic functions were working with number
# we need to inport this module so we can use it
print(math.ceil(2.2))


# number one is different from string one, because they are two different types
# because two objects can be concatenated if they are same type,so we should convert this string one to number
# x = input("x:")
# y = int(x)+1


# conditional statement
# if elif else
# in python logical operators are short circuit
high_income = False
good_cradit = True
student = False

if (high_income or good_cradit) and not student:
    print("eligible")
else:
    print("not eligible")


age = 20
if 18 <= age < 45:
    print("eligiable")

# use loop to create repetition
for number in range(3):
    print("attempt", number+1, (number+1)*".")

# it can simplipy code and make it cleaner
for number in range(1, 4):
    print("attempt", number, number*".")

# middle parameter is step
for number in range(1, 2, 10):
    print("attempt", number, number*".")

# range function return
# iterable


# while
number = 100
while number > 0:
    print(number)
    number //= 2


# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

print("\n")
count = 0
for number in range(1, 10):
    remainder = number % 2
    if remainder == 0:
        print(number)
        count += 1
print(f"we have {count} even numbers")

# already study build function in python
# learn how to wirte your own function
