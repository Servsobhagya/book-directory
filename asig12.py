#Name and handle the exception occured in the following program
try:
 a=3
 if a<4:
  a=a/(a-3)
  print(a)
#Error=ZeroDivisionError
except ZeroDivisionError:
  print("ZeroDivisionError")
  
# Name and handle the exception occurred in the following program:
try:
 l=[1,2,3]
 print(l[3])
except IndexError:
 print("IndexError")

#What will be the output of the following code:
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not
	
#OUTPUT raise NameError("Hi there")  # Raise Error
# NameError: Hi there

#What will be the output of the following codetdef AbyB(a , b):

def AbyB(a , b):
 try:
  c=((a+b)/(a-b))
 except ZeroDivisionError:
		print("a/b result in 0")
 else:
  print(c)
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#Write a program to show and handle following exceptions:
#index error

 
try:
 l=[1,2,4]
 print(l[5])
except IndexError:
 print("Index Error")

 #value error
try:
 l=[1,2]
 int("abc")
except ValueError:
 print("ValueError")

#import error
try:
 import threading
 from threading import time
except ImportError:
 print("ImportError")
#Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18)
class AgeTooSmallError(Exception):
	pass
age=0
while age<18:
	age=int(input("enter your age"))
	try:
	 if age<18:
	  raise AgeTooSmallError("age is tool small")
	except Exception as e:
	 print(e)
	
	