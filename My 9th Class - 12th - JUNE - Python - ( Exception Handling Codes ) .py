#!/usr/bin/env python
# coding: utf-8

#                                    #12th-JUNE-22
# 
#                                  9th Class - "Python"
# 
#                                  "Exception Handling" 

# In[ ]:


# Code No :- 1 

# Explanation below code :-

# I have added to numbers -> c = a+b. simple operation and If we print it as a outcome we will get 30.


# In[1]:


a = 10 
b = 20
c = a+b
print(c)


# In[2]:


# Code No :- 2 

# Explanation below code :- 

# If we try to run this below code then we get as a outcome Syntax Error :- Unexpected EOF while parsing.

# So, this is exception which we are geeting at run time or we are getting at complied time.
# It's a Complied time.

# c = a+b - Source code 
#             |
#           Compiler

# This is my source code and these sources code going through a compiler. If we know operating system of compiler design.

# At the time of compilation each and every thing is going to be check. Means there is some check over there.

# We are going to check, syntax each and everything going to be check, whenever my code is going through the compiler.

# Below code we can see that at the time of compiler, it will dectating there is no proper syntax. This is called,
# compile time Error.


# In[3]:


a = 10 
b = 20
c = a+b
print(c


# In[4]:


# Code No :- 3

#  Explanation below code :-

# If we run this code, we are getting an Error, what is the Error.

# This is a Type Error. we are getting an Type Error, once execute it.
# TypeError means here (int) integer and string (str) we can not add.

# a = 10       Source Code 
# b = "v"      Compiler 
# c = a+b      Bite Code or Machine Code
# print(c)     Interpreter

# Whenever we are talking about source code this code going through compiler there will be a bit code.

# So, whenever this code is going through a compiler is there any syntax Error. No, every syntax is fine.
# what exactly happened over here is that.

# My this ( Bite code or Machie code ) going to the ( Interpreter )

# Now real this will happened,mean in the CPU, there will be a small program Interpreter.


# In[6]:


# Continueee....

# Now it is executing our entire code. So it is checking doing some calculation or processing my code.

# ok, c = a+b  a is Integer(Int) and B is a String(str)

# It is checking c = a+b are we able to add these 2 one is "int" and another is "str".

# Only Syntax Error is compiler Error. We would not able to add these two c = a+b  here a is int and b is str.

# So, this time it will through an Error. This is all process call " Run time Error".

# So, Run time Error is a Exception.

# What is "Run Time Error"?

# Run time Error is Exception or Exception is a run time Error.
# Definitely now we should handle this execption. So, these thing call "Exception Handling".

# Codeshare.io -> website where we can share code live. just for understanding.


# In[7]:


a = 10
b = "v"
c = a+b
print(c)


# In[ ]:





#                                              "PYTHON"
#                                        "Exception Handling"
# 
#                            There are 5 keywords to perform these task.
# 
# #1. Try
# 
# #2. Except
# 
# #3. Else
# 
# #4. Raise
# 
# #5. Finally

# In[ ]:





# In[ ]:


# Code No :- 4

# Explanation for Below code :-

# Here I have written two number, Now we are going to do "Exception Handling". Why we need to do Exception handling.

# With the help of these line of code, we will try to understand. We are going to do "input Statement"

# a = int(input("enter first number"))
# b =  int(input("enter second number"))

# Here, what we have to do, we have to do a "Type casting" Int otherwise, It will by default return string(str) value.

# So, now we got a 2 value, we got 2 number. we can perform any operation on this 2 number.

# a = int(input("enter first number"))
# b =  int(input("enter second number"))

# So, what I am going to do is performing operation. Operation will be a divison operation.

# c = a/b - "C" equal a upon b (c = a/b) and I am going to print(c)

# 1.1st number will be 10
# 2.2nd number will be 20

# Outcome is 0.5 Yes, we are getting 0.5 over here.


# In[15]:


# Use 10 & 20 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
c = a/b
print(c)


# In[ ]:


# Code No :- 5

# Explanation for Below code :-

# If i am going to run these below code. by putting value 10 and 0.

# we are getting - ZeroDivisionError: division by zero  As a outcome, we can see we are getting an Error.

# This is the run time Error, This is the exception which we are getting.

# So, we are getting an Error, why we should do a Exception Handling. Suppose we have written this code we are
# running this code we are getting Exception. Over here Exception handling required but why?


# In[ ]:


# Continuee.....

# Let's suppose, this is my project, I am going to build a calculator. Inside this calculator different operation
# will be there.

# I am going to perform a divide operation.

# Apart from that there will be multiplication and there will be addition operation. There will be like 
# Substraction different different operation.


# In[16]:


#  Use 10 & 0 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
c = a/b
print(c)


# In[ ]:


# Code No :- 6

# If I am going to write d = a*b and Print(d)

# If we run this code by putting value of 10 and 20.

# As a outcome we can see we are getting 0.5 and we are getting 200 over here.


# In[17]:


#  Use 10 & 20 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
c = a/b
print(c)
d = a*b
print(d)


# In[ ]:


# Code No :- 7

# lets understand,

# If we run this code by putting value of 10 and 0.  As aoutcome we will get an "ZeroDivisionError: division by zero"

# Why getting an Error, Because I am saying that.

# 10/0 ( 10 division by 0)
# infinite

# 10*0 (10 multiply by 0)

# c = a/b or 10/0
# Print(c)   ( Warning dnt run otherwise laptop hang Just for knowledge).

# d = a*b or 10*0 = 0

# c = a/b ( This is giving me an Error).
# d = a*b ( But a*b it should run, because it giving me outcome atleast "0", But why we are getting an Error)

# d = a*b ( My syntax is fine, my value is fine why I am getting an Error)

# This time Exception Handling is required. 

# Because, In bigger project, Exception Handling must, because of these kind of scenario.

# Everytime we can see whenever we get an Error. As below we can see this Type things we can see on the screen.

# ZeroDivisionError.

# Whenever we are getting an Error, We can see above message pop-up.By looking this type message pop-up, we get scare
# somethings. So these also we should do a Exception Handling.

# Thare is 2 region Exception Handling.


# In[ ]:


# Interview Question :-

# Why we are doing a Exception Handling or Runtime Error. - Give me a region.

# 1. If we are not doing Exception Handling. So, my further code Exception will stop.

# 2. This is not user Friendly.

# Whenever we are doing Exception Handling in Python. There are different different keyword we will able to see.

# 1.Try

# 2.Exception

# 3.Else

# 4.Raise

# 5.Finally

# So, these 5 keyword we are having with the help of these, we can handle Exception.

# With the help of those key word we are going to solve problem.


# In[18]:


#  Use 10 & 0 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
c = a/b
print(c)
d = a*b
print(d)


# In[1]:


# Code No :- 8 

# Warning :-  Do not run below code. This is just for understand for knowledge only. We will get the outcome "infinite"


# #Use 10 & 0 for outcome
# 
# a = int(input("enter first number"))
# 
# b =  int(input("enter second number"))
# 
# c = a/b
# 
# print(c)

# In[7]:


# Code No :- 9

# Let's understand below code :-

# Let's suppose,

# How we can use those keyword and
# How we can handle Exception
# Here we have 2 number.

#a = int(input("enter first number"))
#b =  int(input("enter second number"))

# These 2 numbers as a input and down below code.

# Here in this line code  - c = a/b - (10/0)

# we may be get the exception in my code. For this what we can do is that we can keep this code under "Try" block.

# And Exception message where, I have to keep that Exception message under the "Except "block.

# except :
#    print("b should not be a zero")

# Inside this exception block, I can keep my message. I can print anything over here is ("b should not be a zero").

# Many thing over here when we are handling Exception. In "Except" there will be classes. According to classes,
# We are going to handle "Exception".

# Exception we are getting "ZeroDivision Error".

# Now when we run this code - 10 and 20. As a outcome we will get the 0.5.

# But again, If I am going to run  - 10 and 0. As a outcome, we will - ("b should not be a zero")

# Here, we can see my code is prefectly fine, I am not getting any Error over here.


# In[3]:


# Use 10 & 0 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
try :
    c = a/b
    print(c)

except :
    print("b should not be a zero")


# In[4]:


# Code No :- 10

# Here in this code we are geeting an "Error".
# Code is not going to execute. But when above code, I used - "Try:" and "Except:"

# During that time my code was working prefectly. If I did not use (Try and Except) then, If I try to run the code.

# I am getting an Error.


# In[5]:


# Use 10 & 0 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
c = a/b
print(c)


# In[8]:


# Code No :- 11

# Let's Understand :-

# So, over here we can see my try block and Except block. If I am getting any Error inside my try block.

# try :
#    c = a/b
#    print(c)

# except ZeroDivisionError :
#   print("b should not be a zero")


# Then it is automatically coming to my except block and we are getting as a outcome message.

# print("b should not be a zero") But here what I can define.

# except ZeroDivisionError :
#   print("b should not be a zero")

# Zero devision Error, this will be my class. Based on this. I am able to get an outcome print("b should not be a zero")

# If we run this code by giving - putting 10 & 0 outcome is - ["b should not be a zero"]

# As a outcome we can see we are getting same outcome earlier we got, but here difference is that, we have added this
# line. - ["except ZeroDivisionError"] :


# try :
#    c = a/b
#    print(c)

# This is my try block, inside this try block we can see there is a possibility we may get an "Error"

# So, we have kept these inside "try" block.

# except ZeroDivisionError :
#    print("b should not be a zero")

# Now, inside except, this is a key word except, what we are done here we have defined a class.

# Except(?) - Class according to what, According to the "Error".


# In[ ]:


# continuee......

#  try :
#    c = a/b
#    print(c)

# Over here we can see we may get Zero division Error. Whenever we are going to divide.

# c = a/b or c = 10/20 ( it is fine correct ) / c = 10/0 ( this is not fessible or correct )

# There is high chance that, we may get an "Zerodivision Error".So, that is why we are going to add or define.

# Class Zerodivision Error over here.

# [except ZeroDivisionError : ]    -  Class

# If i am going to write a+b, so "a" is integer value  and "b" is String value.

# So, which class, I should write over here There will be a "TypeError".

# From below chart which class should I write over here.

# Yes, Class mentioning is not menditory but its a good practise to have.

# For Table Google it - "Exception hierarchy in python with example" and is the link for recomendation.

# https://medium.com/building-enterprise-applications-in-python/exception-handling-in-python-part-1-94ef5b49e043

# We should mention (Runtime Error ). But There will be a [Arithmetic Error].

# Arithmetic Error will be there. Directly what we can do we can define these ["Exception"] This is my parent class.

# We can define Exception class also.


# In[10]:


# Use 10 & 0 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
try :
    c = a/b
    print(c)

except ZeroDivisionError :
    print("b should not be a zero")


# In[11]:


# Code No :- 12

# Let's understand :-

# Here in these code we are going to use 2 symbol or 2 parenthesis print()).

# Definitely, it will be a "Syntax Error". 

# a = int(input("enter first number"))
# b =  int(input("enter second number"))

# c =  a/b 
#    print())

# In print we are going to use 2 parenthesis. 

# Except :
#     print( "wrong Syntax")

# In these "Except" we can write a "Syntax Error" but this time we are not writing, because it is not mendatory.

# Simple "Except " block write. If we are going to write a message over here that, ("wrong syntax") 

# d = a+b

# So, if we are trying to run this code we are able to do that.

# Here, As a outcome we are not getting ("wrong Syntax") and we are not able to run this code.

# [d = a+b] Why, because this is a ["Compile time Error"].

# This is a "Compile Time Error", Except block means - whenever we are handling "run time Error" or a "Exception".

# So, definitely we can handle those things with the help of "Try and Except".

# But, we can't handle "Syntax Error" with the help of these "Try and Except".



# In[13]:


# Just run this code, we will get an Error , because of these - (c)) 

a = int(input("enter first number"))
b =  int(input("enter second number"))
try :
    c = a/b
    print(c))

except :
    print("Wrong syntax")
d = a+b


# In[14]:


# Code No :- 13

# Let's understand :-

# Here what difference is that we have just removed 2 parathesis. From these - print(c))  to these - print(c).

# try :
# c = a/b
# print(c)

# we have removed 2 parathesis and  addition we have added 

# d = a+b
# print(d)

# So, As a outcome we can down below it printed last line code also.

# If we use or put the value of 10 and 0 as a outcome we are getting

# b should not be a zero
# 10


# In[15]:


# Use 10 & 0 for outcome

a = int(input("enter first number"))
b =  int(input("enter second number"))
try :
    c = a/b
    print(c)

except :
    print("b should not be a zero")
d = a+b
print(d)


# In[ ]:


# For Understanding

# In python whenever, we are talking about "Except" there some classes has defined. Which classes ?

# Object oriented programming :-

# Whenever, we are writing a code, we are having two approach for writing this code.

#                          Code 
                            |
# 1. Functional Approach          2. Object Oriented Programming approach

# 1. Functional Approach :-

# Inside this fucntional approach we are just writing a fucntion. There will be function name (A,B,C) whatever &

# We are going to define code over here, inside this function. This is called fucntion Definition.

# IF we call this fucntion ( A, b, c) over here, we will be going to see. We are going to call this fucntion and my

# my function is going to be execute my definition is going to be execute.

# 2. Object Oriented Programming approach :-

# Inside object oriented programming one things come to picture that is called class.

# Class(ABC) and inside class I am going to define a different different method.

# Function 1 
# Function 2

# Like this end number of function define inside this code. We are going crate object of these class.

# These is called classes in object.

# So, we generally we don't write this fucntional approach, now a days we use the object oriented programming approach.

# This fucntion is nothing this is called method.

# Someone asked, please define what is function and method ?

# So, Method is nothing, method is a function which we are defining inside a Classes.

# As a function, we can called something like this :- (obj.def) This is a function name. We shaw like-

# [ List.append() ] we already know about it.

# Somebody has already written this Append fucntion in the "Python". 

# Whenever we are talking about this "Except" Block.

# Except (" ") whenever we talked about except we have to write some classes. According to the classes we are going

# descriminate what will be my exception.

# Google it about it - ( Exception Hierarchy in Python )


# In[ ]:


# Continueee..

# What is the meaning of Exception Hierarchy in Python?

# Exception Hierarchy :- Exception Hierarchy is whenever we are talking about object oriented programming.

# The three pillar of the object oriented programming :-

# 1.Encapsulation.
# 2.Inheritance
# 3.Polymorphism etc.

#          2.Inheritance 
#                |
#      parent class and Child Class 

# Whenever we are talking about Inheritance,inside this one there will be a parent class and another one child class.

# Class :-

# Whenever we are talking about class. Over here I am going to define  - @Cuboid.Class 

# This is my class and there is my function will be a volume. Over here, I am going to write inside this 
# Function, empty as of now.

# Cuboid - Google symbol for Picture

# Rectangle will be part of these cuboid only.

# Rectangle :- Google symbol for Picture

# Can we inherit these class rectangle, whatever property will be there, with respect to these rectangle.

# So, whenever property will be there, with respect to these rectangle. All these properties, we will be getting in

# my cuboid class.

# We will be able to find out volume and all whatever.

# Class rectangle : - This is my rectangle class, this is my parent class.

# Class Cuboid :- This is my cuboid class, this is my child class, we are going to inherit the properties from

# cuboid to rectangle.

# Parent and child :-

# Why we are saying this concept, because whenever we are talking about exception there will be a 

#hierarchy of this exception.

#                           Base Exception - This will be my parent class

#                          Exception - This will be my child class

#                         Standard Error

# Generally we use these class only considering my parent class. we have seen that, whenever we are going to 
# Handle the exception, So.

# 1.Try 
# 2.Except or Exception

#                       Exception - This is my parent class

#                       Standard Error - This will the Child class


# For Table Google it - "Exception hierarchy in python with example" and is the link for recomendation.

# https://medium.com/building-enterprise-applications-in-python/exception-handling-in-python-part-1-94ef5b49e043
    
# S0, which Error we are getting in our code. It was a - ["ZeroDivision Error"]

# For these someone had already defined the class. These ZeroDivision class. In Python, we just need to call these
# class - ["ZeroDivision Error"]


# In[16]:


# Continuee......

# We can see different kind of Error we can see [ "OS Error" ] for that we have to call these OS Class.

# IF we going to see these ["IO Error"] Based on that we have to define IO class.

# If we going to see - ["Intentation Error "]. So, we have to define these Indentation Class.etc....


# In[17]:


# Code No :- 14


#                                         Question given to solve during class
# 
# 
# Q.Write a program to ask the user to input 2 integers and calculate and print their division. Make sure your 
# 
# program behaves ad follows :-
# 
# 
# #1.If the user enters a non integer value then ask him to enter only integers.
# 
# #2.If denominator is 0, then ask him to input non- Zero denominator.
# 
# #3.Repeat the process until correct input is given.
# 
# #4.Only if the inputs are correct then display their division and terminate the code.
# 

# In[ ]:





# In[22]:


# Below are the code send my Public :-

# 1.Nisha :- just use any number i have use 10 and 0

try :
    a = int(input("enter first number1:"))
    b =  int(input("enter second number2:"))
except Exception :
    print("Enter integer values only")
try :
    c = a/b
    print(c)
except ZeroDivisionError :
    print("Enter non zero value in integer")


# In[23]:


# 2. Anup :- just use any number i have use 10 and 0

a = int(input("enter first number:"))
b =  int(input("enter second number:"))

error=" "
if type(a)!=int:
    error = "Please enter numeric value of a:"
if type(b)!= int:
    error = "Please enter numeric value of b:"
if b == 0:
    error = "Please enter Non O value for b:"
try :
    print(a/b)
except :
    print("Input Error",error)


# In[24]:


# 3. Praneet :- just use any number i have use 10 and 0

a = int(input("enter first number:"))
b =  int(input("enter second number:"))
while a<0:
    a = int(input("enter a positive number1:"))
while b<0 :
    b = int(input("enter a positive number2:"))
try:
    c = a/b
    print(c)
except :
    print("number 2 should not be 0")


# In[26]:


# 4. Abhishek :- just use any number i have use 10 and 0

try:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("b should not be zero")
except ValueError :
    print("enter an integer")


# In[27]:


# 5. Sumit :- just use any number i have use 10 and 0

a = int(input("enter first number:"))
b =  int(input("enter second number:"))
try:
    c = int(a)/int(b)
    print(c)
except ZeroDivisionError :
    print("b should not be 0")
except:
    print("enter integer value")


# In[28]:


# Code No :- 15

# Let's understand :-

# If we are not writing any class over here, still we are able to handle exception.

#except :
#   print("b should not be a zero")

# We are able to get the message or outcome. Put these value 10 & 0 to get the outcome.

# Here we have just only written except : block and we are able to get this message or outcome.


# In[29]:


# Use 10 & 0 for outcome

a = int(input("enter first number:"))
b =  int(input("enter second number:"))
try :
    c = a/b
    print(c)
    d = a+str(b)
    print(d)
except :
    print("b should not be a zero")


# In[30]:


# Code No :- 16

# Here, In this code also we are getting some outcome as my above code.

# Earlier code we did not given or written any class.

# except :
#   print("b should not be a zero")

# still we are getting same outcome. In this code, we have given or written class.

#except ZeroDivisionError:
#    print("b should not be a zero")

# Here, I have given class, then also we are getting same outcome. What is the difference between those both code.

# By giving class also we are getting as result or outcome. Without giving any class also we are getting same outcome.


# In[ ]:


# Continuee...

# The thing is that,

# * If we are not writting this class name ("ZeroDivision Error").

# So, we would not able to get that which Error we are getting in my code.

# When we write code in production, there is thousand lines of code.

# Big project, big line codes. Whenever we are going to handle this "exception" at that time, it is mendatory

# we should write name of the class.

# In class if we look at it, If someone look into my code, then they can understand that its a ["ZeroDivisionError"].


# In[31]:


# Use 10 & 0 for outcome

a = int(input("enter first number:"))
b =  int(input("enter second number:"))
try :
    c = a/b
    print(c)
    d = a+str(b)
    print(d)
except ZeroDivisionError:
    print("b should not be a zero")


# In[32]:


# Code No :- 17

# Let's understand :-

# Here we can see that, ["except ZeroDivisionError"] : but here another except ["ValueError:"] also we are able to get.

# Actually, I am getting this things in my code. I will be get ["ValueError:" ].

# This is my code so :-

# c = a/b
    print(c)
    d = a+str(b)
    print(d)
    
# Here, we are having 2 possibility :-

# 1.1st Possibility is we may get ["ValueError"]

# 2.2nd Possibility is we may get an ["ZeroDivisionError"]


# In[33]:


# Use 10 & 0 for outcome

a = int(input("enter first number:"))
b =  int(input("enter second number:"))
try :
    c = a/b
    print(c)
    d = a+str(b)
    print(d)
except ZeroDivisionError:
    print("b should not be a zero")
except ValueError :
    print("Please input number only")


# In[34]:


# Code No :- 18

# Let's understand both the code Code No 

# Here inside, we have a multiple except block.

#except ZeroDivisionError:
#   print("b should not be a zero")
#except ValueError :
    print("Please input number only")

# Here we have 2 except block.With one try block we can use a multiple execption block.

# try
# except
# print
# except
# Print

# c=a/b
# print(c)

# 1st except block we will able to see with respect to above Error.

# 1st except block --> ZeroDivision Error:

# 2nd Except block ( ValueError :) we can see with respect to these Error.

# d = a+str(b)
# print(d)


# In[1]:


# Use 10 & 20 for outcome

a = int(input("enter first number:"))
b =  int(input("enter second number:"))
try :
    c = a/b
    print(c)
    d = a+str(b)
    print(d)
except ZeroDivisionError:
    print("b should not be a zero")
except ValueError :
    print("Please input number only")


# In[2]:


# Code No :- 19

# Let's understand below code :

# So, above code we have write 2 separate execpt block.

# except ZeroDivisionError:
#   print("b should not be a zero")
#except ValueError :
#   print("Please input number only")

# But in these code, instead of writting these 2 seperate block.

# Except(ZeroDIivisionError, ValueError) :
#      print("b should not be a Zero or please input number only")

# We can write 2 seperate block into one execpt block. we can write it under parenthesis. 

# Now, we can write a message.
# Print("b should not be a Zero or please input number only")

# So, we have seen that 2 codes.There is a 2 syntax to write a same things or same outcome.

# One is 2 seperate way except block, Another way is combined both into a parenthesis into a one except block.


# In[3]:


# Use 10 & 20 for outcome

a = int(input("enter first number:"))
b =  int(input("enter second number:"))
try :
    c = a/b
    print(c)
    d = a+str(b)
    print(d)
except ZeroDivisionError:
    print("b should not be a zero")


# In[4]:


# Code No :- 20

# Let's understand :-

# With the help of "TypeError: We can get the Value or we can able to handle the situation.


# In[7]:


# Use 10 & a for outcome

a = int(input("enter first number:"))
b =  input("second number:")
try :
    d =a+b
    print(d)
except TypeError:
    print("Please input number only")


# In[8]:


# Code No :- 21

  # For Understanding :-

# So,we are having Total 5 keyword :-

#1.Try

#2.Except :-

# In except, we have seen a multiple except block with one try block.

# Yes, we can as many as "Except" block we can use with respect to try block.

#3.Raise :- 

# Another concept called raise, we can create our own exception, Means we can raise the exception at the particular
# time, we can create our 

#4.Custom Exception :-

# Also, These two things we are trying to understand.Apart from that, we can see.

#5.Finally :-

# Finally concept also, what is the meaning of these finally concept also. Before these one, if we want to know
# more about these exception.There is 2 function has been given in "Python".

# (a) Format_exc()

# (b) exc_info()

# Why we are using these 2 fucntion for getting a more detail about my exception.


# In[12]:


# Code No :- 22  


# For Understanding :-


# For Table Google it - "Exception hierarchy in python with example" and is the link for recomendation.

# https://medium.com/building-enterprise-applications-in-python/exception-handling-in-python-part-1-94ef5b49e043

# Now once if we are going to check these exception Hierarchy. Exception Hierarchy means we have :-

# Parent class  and  child class 

# Base exception  and Exception are - These are exception is parent class.

# Arithmetic Error :- This is child class.

# ZeroDivision Error :- This is a child Class of Arithmetic Error.

# So, there is a conviences that, whenever we are writing a code, child class should come at first place.
# Then a parent class means of these over here.

# ZeroDivision Class and Arithmetic class

# Whenever our code is going to be execute, if I am getting "ZeroDivision Error".

# So, it will check with respect to the except block.

# Arithmetic CLass and ZeroDivision Class 

# If we are writing like this parent class 1st "Arithmetic class" then we are writing "Child class or ZeroDivision Class"
# would not execute it would not get chance to execute.

# Convience is that, 1st we should write a child means "ZeroDivision Error".

# Then we should write these "Arithmetic Error". Why we are doing, because when we are writing like these.

# Arithmetic CLass and ZeroDivision Class - It would not able to execute.
    


# In[13]:


# Code No :- 23


# In[14]:


# Question :- 

# Write a program to ask the user to input 2 integer and calculate and print their division. Make sure your

# program behaves as follows :

# If the user enters a non integer value ask him to enter only integers.

# If denominator is 0, then ask him to input non-Zero denominator.

# Repeate the process until correct input is given.

# Only if the inputs are correct then display their division and terminate the code.

# Meaning of these sentence below is question.

# a 
# b
# a/b
# a = "s"
# print(only int)
# b = 0
# print(only non zero)


#                            #Dn't run this code just for understanding otehrwise hang the pc.
#                            
#                            # Outcome will be "Infinite" so it will continuee provide outcome non stop.
# 
# #while true :
# 
#        print("vijay")
#        
#     

# In[15]:


# Code No :- 24

# Explanation below code :-

# If I will going to run or execute this code.

# start giving name 

# Amit
# Tarun
# Ajay
# Vijay
# Vijay

# If I am going to write other name then, it will keep going to giving me write another name.

# But when at time, If I will write "Vijay". Then, it will stop there and print "Vijay".

# So, it will be asking untill, I am not giving proper name. Then it will break my condition.


# In[16]:


# Use Amit, Trun, Ajay, Vijay and Vijay for outcome

while True :
    name = input("write your name:")
    if name == "vijay":
        print("vijay")
        break


# In[17]:


# Code No :- 25

# It keep generating codes.


# In[30]:


# Use 10 and a | 10 and 0 | 10 and 20 for outcome

while True :
    try :
        a = int(input("enter first number"))
        b = int(input("enter second number"))
        c = a/b
        print(c)
        break
    except ValueError:
        print("there should not be string")
    except ZeroDivisionError :
        print("Non zero denomitor")


# In[31]:


# Code No :- 26

# Explanation :-

# If we write wrong value definitely,it will through the "exception".

# If I am going to write over here input("enter a string").

# It will be working fine. It is giving me a "Vijay"


# In[32]:


# Use Vijay string for outcome

input("enter a string")


# In[ ]:


# Code No :- 27

# Explanation :-

# If I am going to do a type casting and run the code. As a outcome it will through the Error.

# The Error name will be "ValueError" :

# As a outcome we can see below -

# ValueError: invalid literal for int() with base 10: 'vijay' 


# In[33]:


# Use Vijay string for outcome, But unfortunately its giving me Error.

int(input("enter a string"))


# In[34]:


# Code No :- 28

# Explanation :-

# So, here we can keep the type casting inside the "Try Block"

# inside Except, we can write - Print("string not allow"). Because, we have the integer value.


# In[35]:


# Use "Vijay" string for outcome.

try :
    int(input("enter a string"))
except:
    print("string not allow")


# In[36]:


# Code No :- 29


# In[ ]:


# For Understand only :-

# Let's talk about 2 things over here.

# There is 2 function has been given in Python.

# (a) Format_exc()

# (b) exc_info()

# These 2 function we will be talk about.

# After that ;-

# Raise Block
# Custom Excception
# Finally Block


# In[38]:


# Code No :- 30

# Let's understand this code.

# The code, I have written over here is.

# print("div:",c)

# Over here, print I am going to write the value of "C". It will be "Division (div)" Column (:).

# Now, we can see inside except block.

# "Except :"
#       print("b should not be a Zero")

# Inside execpt block the message, I have written. - print("b should not be a Zero")

# If i am going to run this code - 10 and 0 | 10 and 0 | 10 and 20 div : 0.5 

# Here if I write 10 & 20 it will break the as a outcome we can see - [div : 0.5 ]


# In[39]:


# Use 10 and 0 | 10 and 0 | 10 and 20 for outcome

while True :
    try :
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
        c = a/b
        print("div:",c)
        break
    except :
        print("b should not be a Zero")


# In[40]:


# Code No :- 31

# Explanation :-

# If i am going to write 
# except ZeroDivisionError as e :
#        print(e)

#If we are going to print(e) directly If I am going to write 10 & 0.As a outcome what we are getting- ["division by zero"]

# I have not written any message inside print() only we have written print(e).

# But still I am able to get a outcome message. - ["division by zero"].

# If we write any message inside print(.......), I will get the output.

# Why print(e) - giving me an outcome, because of these line code.

# Except ZerodivisionError as e:  This is [ "Alice" ] name.


# In[41]:


# Use 10 and 0 | 10 and 20 for outcome

while True :
    try :
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
        c = a/b
        print("div:",c)
        break
    except ZeroDivisionError as e :
        print(e)


# In[42]:


# Code No :- 32

# Explanation :-

# If we run this code, As a outcome we can see 10 and 0.

#(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000002867F5A1BC0>)

# As a outcome, we can see here, its giving me a entire things.

# It is giving me a more detail with respect to my exception.

# If we working on a project while doing debugging entire code. So, sure we call these - ["exc_info())"].

# So, what is the system(sys) over here. Sys nothing its a module. Module is [.py] or dot py file or dot python file.

# Suppose, I am writting my python file.

# abc.py anything instead of ABC

# This is a module, directly I can import this module functionally in order file. Same things we are going to do over here.

# Someone has already written these file (SYS), we are importing these system file inside our code and we are using
# these ("exc_info())") method.

# If we put these value 10 and 20 - As a outcome we are getting outcome (0.5)


# In[ ]:


# FOr understanding :-

# Module, we have 2 types

#1.Build - in Module and
#2.Custom Modules

# So, (Sys) system is a Build - in Module.


# In[43]:


# Use 10 and 0 | 10 and 20 for outcome

import sys
while True :
    try :
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
        c = a/b
        print("div:",c)
        break
    except :
        print(sys.exc_info())


# In[2]:


# Code No :- 33

# Explanation :-

# Now we have seen packaging and unpacking. 

# a,b,c = (1,2,3)

#a = 1
#b = 2
#c = 3

# If I write like this -  a,b,c = (1,2,3)

# I am print a outcome will be 1, If I am print b outcome will be 2,  If I am print c outcome will be 3.

# (1,2,3) This is a my Tuple and we are going to unpacked Tuples inside these (a,b,c) variable.

# I am writing over here - [ a,b,c =sys.exc_info()] - Below then this line code are "Tuples".

# So, I can decode these entire "Tuples" inside these variable (a,b,c).

# So, in "a" what I am getting print "a" will be my exception class.

# print("exception class",a)
# print("exception message",b)

# Here what, I am printiing, exception message. Definitely these will be my exception message.

# exception class < class."zeroDivisionError", Here are able to get.

# print("line number,c.tb_lineno") - with the help of these line - [c.tb_lineno] atribute we can get the line no. also.

#[ c = a/b ] - Exception message division by zero line number "6".

# Line no 6, here is the c = a/b

# Why because in [c = a/b] we are getting an Error, line no 6. Like these we can decode our entire "Error".


# In[4]:


a,b,c = (1,2,3)


# In[5]:


a


# In[6]:


b


# In[8]:


c


# In[10]:


while True:
    try :
        a = int(input("first number:"))
        b = int(input("second number:"))
        c = a/b
        print("div:",c)
        break
    except :
        a,b,c =sys.exc_info()
        print("exception class",a)
        print("exception message",b)
        print("line number,c.tb_lineno")         


# In[11]:


# Code No :- 34

# Explanation :-

# This line code for above code understanding.


# In[12]:


while True:
    try :
        a = int(input("first number:"))
        b = int(input("second number:"))
        c = a/b
        print("div:",c)
        break
    except :
        a,b,c =sys.exc_info()
        print("exception class",a)
        print("exception message",b)
        print("line number,c.tb_lineno")


# In[13]:


# Code No :- 35

# Explanation :-

# Let's discussed 1 more module that is called "Traceback"  module.

# # Import sys.exc.info()

# import traceback.format_exc()

# As of now we have imported sys module insisde "Sys", module we have exc,info(). These method we are having,

# by putting #hastagee symbol  let make it comment as of now.

# Now, we are having 1 more method import traceback inside these module, we are having function called format_exc().

# If we call these function, it will give me a same output.

# break
# except :
#    print(traceback.format_exc)

# Here this line of code, I will going to add or make change. If I will call or type 10 & 0. execute code.

# import traceback
#while True:
#    try :
#        a = int(input("first number:"))
#        b = int(input("second number:"))
#        c = a/b

# These entire ["traceback"] Error above outcome we can see. - ["ZeroDivisionError: division by zero"]

# Traceback is a module actually, inside these we are having this fucntion.["format_exc())"]

# If we run these code by puttung this 2 value 10 and 20. As a outcome we will get the [0.5] outcome.

# Now, if we run below code.

# a = 10
# b = 0
# a/b

# ["ZeroDivisionError: division by zero"] - outcome 


# In[ ]:


# Continuee.....

# sys.exc_info() is  (function)- we understood.

# "Traceback.format_exc())"  - we are having this module.

# This thing also we can call, and we are getting description about, my execption. 

# Why we are getting this descrription whenever we are running the large code or doing any project at that time,

# it help us to debugging the project.

# Whenever we are going to code our project we have to code in such a way. We are going to handle each and every
# exception along with these kind of funtion.

# "Traceback.format_exc())" - So, we will getting a description (10 & 0 value) about my exception. 

# Without using any class, we are getting amount of outcome which we are looking for. Instead  of using class fucntion

# If we use these "Trace or sys.exc())" fucntion we will going to get outcome.

# Raise Exception :-

# Inside this raise execption, what we are going to do its a manual custom exception. Custom means a custom line. with 
# the help of code let's understand the custom means.


# In[14]:


# Import sys.exc.info()

# import traceback.format_exc()


# In[15]:


import traceback
while True:
    try :
        a = int(input("first number:"))
        b = int(input("second number:"))
        c = a/b
        print("div:",c)
        break
    except :
        print(traceback.format_exc())


# In[16]:


# Code No :- 36

# Explanation :-

# Raise Exception :-

# Inside this raise exception, what we are getting to do its a Manual custom exception. Custom means a custom line with
# the help of code, let's understand the custom means.

#  a = int(input("first number:"))
#  b = int(input("second number:"))

# If we enter the value or 0 and 10 - If I am going to do "TypeCasting" means putting "int". After that 0 and 10.
# As a outcome we are getting 0 and 0.

# But, my condition is this number or outcome should be a 0 (Zero).

# If I am giving these number is Zero.So, we have to raise the exception at that point of time.

# If we enter 10 and 0  also we as a outcome we can see over here we are getting as "Error" as a outcome, why because
# line no.3 (a/b). It is giving me a execption, we are giving wrong input means 0 "zero".


# In[20]:


# use  0 and 10  for outcome / Use 10 and 0 also

while True:
    try :
        a = int(input("first number:"))
        b = int(input("second number:"))
        a/b


# In[1]:


# Code No :- 37

# Explanation :-

# if a<0 or b<0: raise Exception ("negative number not allowed") or,
# If a<0 or b<0 :  - ("Negative number not allowed")

# Single line also we can write or in 2 line also this code.

# over here this line, we have written a condition.

# My condition, I have written,

# a<0 - a is less than "0" zero.
# b>0 - b is less than "0" zero.

# Then at that time we have to raise a Exception and Inside these exception only we are going to raise
# these message. ("Negative number not allowed")

# c = a/b
# print("div is", C)
#break
#except valueError :
#  print(" ")

# except ZeroDivisionError :
#   print("Please enter non zero denomitor")

# except Except as e :
#  print(e)

# I am writing further code over here,
# c = a/b
# There will be a "break"

# Now, I am going to write Except block.

# 1.ValueError :
# 2.ZeroError Error :
# 3.Exception

#Last one more 3.Except block, that except block will be a Exception. Over here, I am going to print this (e).

# If we run this code. As a outcome what we are getting.


# In[ ]:


# Continueee.....

# while True:
#    try :
#        a = int(input("first number:"))
#        b = int(input("second number:"))

# while True condition is a and b.

# if a<0 or b<0 :
#            raise Exception("negative number not allowed")

# a<0  - a is less than "O" / b<0 - b is less than "0".  Here a & b is not same both are different.
# Now, we going to raise the exception.

# Exception :- 

# This is actually a built-in class which I have written over here. I can write my custom class also.
# How we can raise the custom execption. For these things is the keyword has been given - ["Raise"]

# Where we have written this raise keyword.

# if a<0 or b<0 : - with respect to this above condition. - Exception (" Negative number are not allowed") &

# Exception this will be the execption message which we are passing. (" Negative number are not allowed") 

# c = a/b
#       print("div:",c)
#       break

# a/b or a upto b - If here  a = 10 , b = 20 then divide('div')

# otherwise a =10 and b = 10 then - It will come over here this line - [except ZeroDivisionError:]

# If we passing - a =10 and b = a - It will come over here this line - [except ValueError:]

# If we are passing if a<0 or b<0 : - which is a<0 or b = 10 both case, it will come to this line - or it will
# give me

# except Exception as e :
#       print(e)

# This is why -  10 and 12232 - If we will put 0 or 10. It will come under the line code print that code.

# outcome - div:0.0008175277959450621

# We have written simple code and we have handle the execption with respect to that code.

# If we give written simple code and we have handle the exception with respect to that code. If we put 0 and 10.

# If we put 0 and 10.- outcome will be - div is 0.0


# In[22]:


# Use 10 and 0 | 10 and a | 10 and -10 | 10 and 12232 for outcome

while True:
    try :
        a = int(input("first number:"))
        b = int(input("second number:"))
        if a<0 or b<0 :
            raise Exception("negative number not allowed")
        c = a/b
        print("div:",c)
        break
    except ValueError:
        print("please enter int only")
    except ZeroDivisionError:
        print("Please enter non Zero denomitor")
    except Exception as e :
        print(e)


# In[ ]:


# Code No :- 38

# Explanation :-

# Both the code - If we put - [324423 and -32432 ] and again second code - [10 and -20].As a outcome it will be ["Error"]

# Let's understand this code :-

# we can create a "Custom Exception" also. We will work with same code last one but few changes inside.

#  if a<0 or b<0 : - raise NegativeNumberExecption("negative number not allowed")

# So, over here instead of writting Exception (build-in) Exception. I am giving my own name.

# Earlier code - Exception 

# Now change - Negative NumberException.

# This is my custom name with respect to my data.

# Another change -

# except Exception as e :
# Now change - Except NegativeNumber Exception as e :

# If we run this code.  - put -  [32456 | -32457] and [10 | -20] if we run this code as a outcome we will get an Error.

# Why we are getting NameError over here. Because we did not define class.

# If we define class before running this code, then only we will not get any "Error".


# In[3]:


# Use 32456 | -32457 as a outcome it's a "Error"

# Custom Exception

while True:
    try :
        a = int(input("first number:"))
        b = int(input("second number:"))
        if a<0 or b<0 :
            raise NegativeNumberExecption("negative number not allowed")
        a = a/b
        print("div:",c)
        break
    except ValueError:
        print("please enter int only")
    except ZeroDivisionError:
        print("Please enter non Zero denomitor")
    except NegativeNumberExecption as e :
        print(e)


# In[ ]:


# Code No :- 39

# Explanation :-

# Let's understand :-

# Earlier Code why we got NameError.

# Because, Here if we are going to add this line of code or if we define this code before writing that code,
# then my outcome will not going to give me an Error.

# Class NegativeNumberExecption (Exception):
# Pass

# So, Exception class in "Python" already they have define and we are calling this class. "Python" create already
# define this way if you write then only it will work.

# If we are going to define this class ("NegativeNumberExecption") in our code then only it will run.

# "Pass " we have define because, if we don't have to write anything during that time we use "Pass".

# Now, If we run this code. - 10 and -10 - as a outcome - negative number not allowed.

# We can see as a outcome it is giving me an Answer. Its not giving me an any "Error". Because we have already define,
# our own class over here.

# Class NegativeNumberExecption(Exception) :
# Pass

# Because of these line code we define that is why while running code its not giving me an any "Error".


# In[5]:


# Use - 10 | -20 as a outcome it's a "Error"

while True:
    try :
        a = int(input("first number:"))
        b = int(input("second number:"))
        if a<0 or b<0 :
            raise NegativeNumberExecption("negative number not allowed")
        a = a/b
        print("div:",c)
        break
    except ValueError:
        print("please enter int only")
    except ZeroDivisionError:
        print("Please enter non Zero denomitor")
    except NegativeNumberExecption as e :
        print(e)


# In[6]:


# Code No :- 40

# Let's understand :-

# Let's understand Final Block :-

# 1.Try
# 2.Except
# 3.Finally

# Why we need a final Block?

# We have already use Try & Except Block. Now let's understand final block.

# So, here in this code.

# If we run this below code by using [10 and 23] 

# As a outcome - 

# dont use zero in denomitor
# hello
# python

# As we can see outcome my don't use Zero in denomitor this line coming under Except we can see and we are able 
# to print that Hello and Python message also.


# In[11]:


# Use - 10 and 23 

try :
    a = int(input("first number:"))
    b = int(input("second number:"))
    C = a/b
    print(c)
except:
    print("dont use zero in denomitor")
    
print("hello")
print("python")


# In[ ]:


# Code No :- 41


# Let's understand :-

# In python they have introduce Finally block.
# Why they have introduce this finally block.

# Because, If we want to run code in any situation in all the situation, then we should use these final block.

#print("hello")
#print("python")

# This code are very crucial. In these code many things, depend.

# Let's understand :-

# Let's suppose, we have created one database of any organization and we forgot to close the connection, in that
# case there will be a some kind of loss.

# If we are using paid service or some important work using "SQL" or "NOSQL" database.

# 2. Let's Suppose :-

# We are using cloud Services & inside these cloud service, we have deploy some application & those application
# we forgot to terminate after deployment that senerio it will charge.

# So, this types of important document or file, we should keep inside final block.

# If we did not keep these file under "Final Block" that is also ok no problem. But, there is a possibility that
# we might get an Error.

# So, always make sure, we should keep those file or code inside the "Final Block".


# In[13]:


# Use 10 & 20  as a outcome we can see below.

try :
    a = int(input("first number:"))
    b = int(input("second number:"))
    C = a/b
    print(c)
except:
    print("dont use zero in denomitor")
    
print("hello")
print("python")


# In[14]:


# Code No :- 42

# Let's understand :-

# "Else Block" :

# If we will going to run this code.

# If we use - 10 & 0 - as outcome - ["Dont use zero in denomitor"]

# If we are getting any execption this try block.So, these block not going to execute.

# If we use 10 & 20 - As a outcome will be - 0.5 and 


# In[16]:


# Use 10 & 0  as a outcome we can see below.

try :
    a = int(input("first number:"))
    b = int(input("second number:"))
    C = a/b
    print(c)
except:
    print("dont use zero in denomitor")
else:
    print("Python rocks !!")


# In[ ]:


# Code No :- 43                    # Else #

# Let's understand :-

# If we are not getting any exception inside the try block.

# Just after try Block this else block will be executed.


# In[17]:


# Use 10 & 20  as a outcome we can see below.

try :
    a = int(input("first number:"))
    b = int(input("second number:"))
    C = a/b
    print(c)
except:
    print("dont use zero in denomitor")
else:
    print("Python rocks !!")


# In[ ]:


# Code No :- 44                               # Finally #


# Let's understand :-

# If we will going to write finally.So, definitelly we will be able to get these outcome also.


# In[19]:


# Use 10 & 0  as a outcome we can see below.

try :
    a = int(input("first number:"))
    b = int(input("second number:"))
    C = a/b
    print(c)
except:
    print("dont use zero in denomitor")
finally:
    print("Python rocks !!")


# In[21]:





#                                      Just for understanding how Finally Block use
#     
#     
# 
# #Lets understand :-
# 
# #Senerio -
# 
# #Suppose I have written - String = "database connection".....
# 
# #"String for database connection" and I got Error.
# 
# #Then I will try to keep that Error line under the "TRY BLOCK" & 
# 
# #I will write message inside execpt block try and except both are fine.
# 
# #So, what we have to do, we have to close the connection of this database.
# 
# #So, any how I have to close the database connection because its important file of my project, if I will not close
# #it will charge in cloud.
# 
# #So, I will write or close this inside finally because, there is surety with respect to my code that my connection
# #will be closed or what I was trying to do will be close, if code coming under finally block.
# 
# #If we will write without finally also, I will get outcome or result.
# 
# #But that is not a good practise, always try to write inside finally block.

# In[ ]:




