#What is Time Tuple
#time tuple is a useagen of tuple and is used for the ordering and notation of time.
import time
print(time.gmtime())



#Write a program to get formatted time.
print(time.asctime(time.gmtime ()))


#Extract month from the time.
import datetime
s=datetime.date.today()
print("today month is",s.month)


#Extract Day from the Time.
import datetime
s=datetime.date.today()
print("today day is",s.day)


#Extract date (ex : 11 in 11/01/2021) from the time
import datetime
from datetime import date
print("6 in",date.today())


#WAP Time Using Local Time
import time
print(time.localtime())

#Find the Factorial of a Number
import math
s=int(input("enter any no"))
print("factorial is:",math.factorial(s))

#Find the GCD of a Number
import math
n=int(input("enter any no"))
s=int(input("enter any no"))
print("gcd is:",math.gcd(n,s))

#Use OS package
import os
print(os.getcwd())
print(os.listdir())
print(os.environ)









