print(' I\'m Harsh Raj ') # \' is for '
print('Be it \\ dfg') # \\ is for \
print("git bash \"") # \" to print 
# output lineA \n lineB
print(" lineA \\n lineB")
print(" lineA \\t lineB")
print("this is 4 backslash \\\\\\\\")
# output \" \'
print("\\\" \\\' ")
# \' - '
# \\ - \
# \\\' - \
# this is double backslash \\
print("this is double backslash \\\\")
# these are /\/\/\/\/\ mountains
print("these are /\\/\\/\\/\\/\\ mountains")
#he is    awesome (use escape sequence insted of manual spaces)
print(" he is\t awesome")
# \" \n \t \' as an output
print("\\\" \\n \\t \\\' "
print(r"this is \" backlash"
nes (16 sloc)  309 Bytes

number1=2
print(number1)
number1 = 4
print(number1)
# string, number
name = "Harsh"
print(name)
name= 123
print(name)
#rule one
#1number=4
#letter ..................... first_letter
_name= "Harsh"
#ulsd = 34
user_one_name = "Aman" # snake case writing
userOneName = "Ayush" # camel case writin
# strings collection of single or double qoutes
first_name = "Harsh"
last_name = "Raj"
full_name = first_name+" " + last_name
print(full_name)
# print(first_name+3) # error
# print(first_name + str(3)) # no error
# print(first_name + "3") # no error
print(first_name*3)
# user input
# input function
name= input("Enter your name: ")
print("Your name is "+ name)
# string
age = input("Enter your age: ")
print("Your age is "+ age)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
# number_one = int(input("Enter first number:")) # 4
# number_two = int(input("Enter second number:")) # 4
# total= number_one+ number_two  # total= 44
# print("Total is "+ str(total))
# str
# 4 --> "4"
# int
# "4" --> 4
number1 = str(4)
number2= int(4)
number3 = float(4)
print(number2 + number3) #float
# name= input("Enter your name: ")
# age= input("Enter your age: ")
name, age= input("Enter your name and age").split(",")
print(name)
print
name = "Harsh"
age = 18
print("hello " + "your age is "+ str(age)) # ugly syntax
#string formatting
print("hello {} your age is {} ".format(name,age+5)) #python 3
print(f"hello {name} your age is {age+5} ") # 3.6 clean
# a=int(input("Enter any number: "))
# b=int(input("Enter any number: "))
# c=int(input("Enter any number: "))
# d= a+b+c
# print(f"Average is {d/3}")
a, b, c= input("enter any three numbers separted by comma: ").split(",")
print(f"avarage of three numbers : {(int(a)+int(b)+int(c))/3}")
#string indexing
language="Python"
# positions (index number)
# p = 0/-6
# y = 1/-5
# t = 2/-4
# h= 3 /-3
# o = 4 / -2
# n = 5 / -1
print(language[-2])
Footer
© 2022 GitHub, Inc.
# slicing/ selecting sub sequences
lang="Python"
# print(lang[0:7])
# print(lang[2:4])
print(lang[:3])
Footer
© 2022 GitHub, Inc.
# print("Harsh"[-1::-1])
print("Harsh"[::-1]) # trick
a=str(input("Enter your Name:- "))
print(f"Reverse of your Name is {a[::-1]}"
# string methods part one
name = "HaRsh rAj"

# 1 len() function
length = len(name)
print(length)

# 2 lower() method
print(name.lower())

# 3 upper() method
print(name.upper())

#4 title() method
print(name.title())

#5 count() method
print(name.count("a"))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
name, char= input("Enter comma seprated Name and Character :- ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count: {name.lower().count(char.lower())}")
# name = "      Har    sh   "
# dots="..........."
# print(name+dots)
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)
# print(name.strip()+dots)
# print(name.replace(" ", "")+ dots)

name, char= input("Enter comma seprated Name and Character :  ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count: {name.strip().lower().count(char.strip().lower())}")
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()
# strings are immutable
string = "string"
new_string = string.replace('t','T')
print(new_string)
Footer
© 2022 GitHub, Inc.
name= "harsh"
name += " raj"
print(name)
age=19
age-=1
print
#strings

name= "harsh"
# string indexing
print(name[1])
#string slicing
print(name[-1:0:-1])
#take user input
#name=input()
#take two user inputs
username,age=input().split(",")
print(username)
print(age)
#len function
print(len(name))
# lower, upper, title method
print(username.lower())
print(username.upper())
print(username.title())
# find, replace, center method
print(username.center(len(name)+5,"*"))
print(name.find(username))
print(name.replace('h','H'))
# strings are immutable
 syntax
# if conditon

age= input("Enter your age:- ")
age=int(age)
if age>=14:
    print("line a")
    print("You are above")
    # Exercise Solution
winning_number= 27
user_input= input("Guess any number b/w 1 & 100: ")
user_input= int(user_input)
if user_input==winning_number:
    print("YOU WIN!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")
         check two conditions at same time
# and, or
name='abc'
age = 19
# if name=='abc' and age==19:
  #  print("condition true")
# else:
  #  print("condition false")

if name == 'abc' or age > 19:
    print("condition true")
else:
    print("condition false ")
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privac
 Exercise-WATCH COCO
# ASk User's name and age
# if user's name start with ('a' or 'A') and age is above 10 then
# print 'you can watch coco movie'
# else print 'sorry, you cannot watch coco.'

# solution
user_name= input("Enter your name:- ")
user_age= input("Enter your age:- ")
user_age=int(user_age)
if user_age >=10 and (user_name[0]=='a' or user_name[0]=='A'):
    print("You can watch coco")
else:
    print("you cannot watch coco")
Footer
# ASk User's name and age
# if user's name start with ('a' or 'A') and age is above 10 then
# print 'you can watch coco movie'
# else print 'sorry, you cannot watch coco.'

# solution
user_name= input("Enter your name:- ")
user_age= input("Enter your age:- ")
user_age=int(user_age)
if user_age >=10 and (user_name[0]=='a' or user_name[0]=='A'):
    print("You can watch coco")
else:
    print("you cannot watch coco")
FloatingPointError
# if elif statement
# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 10 to 60 (250)
# above 60 (200)
age = input("Enter your age:- ")
age=int(age)
if 0<age<=3:
    print("Your ticket price is free")
elif 3<age<=10:
    print("Your ticket price is 150")
elif 10<age<=60:
    print("Your ticket price is 250")
else:
    print("Your ticket price is 200")
    nes (7 sloc)  136 Bytes

name = "Harsh"
# in keyword
# if with in
if 'H' in "Harsh":
    print("H is present in name")
else:
    print("not present")
    # check empty or not
# important
name= input("Enter your name:- ")
if name:
    print(f"your name is {name}")
else:
    print("You didn't write anything")
     loops
# while, for loop
# print("Hello world") # 10 times
i=1
while i<=10:
    print(f"Hello World{i}")
    i=i+1
    # loops
# while, for loop
# print("Hello world") # 10 times
i=1
while i<=10:
    print(f"Hello World{i}")
    i=i+1
    # sum 1 to 10
total = 0
i=1
while i <= 10:
    total+=i
    i+=1
print(total)
n = input("Enter a number:- ")
n= int(n)
total = 0
i=1
while i<=n:
    total+=i
    i+=1
print(total)
# problem
# ask user to input a number containing more than one digit
# example 1256
# calculate 1+2+5+6 and print

# algorithm
# ask user to input in string, i.e don't change string to input
# example  "1256"
# pick string character one by one and change to int

 # solution
number= input("Enter a number:- ")
total = 0
i=0
while i < len(number):
    total+= int(number[i])
    i += 1
print(total)
 infinite loop
while True:
    print("hello world")
    for i in range(1,11):
    print(f"hello world:{i}")

