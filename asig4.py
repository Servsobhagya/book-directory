#Take a Input from user and check whether it is leap year or not
l=int(input("enter year:"))
if(l%4==0):
  print("this is a leap year")
else:
  print("this is not a leap year") 
 
#Check The Dimensions Of Square Amd Rectangle
length=int(input("enter length:"))
breadth=int(input("enter breadth:"))
if(length==breadth):
  print("this is a square")
else:
  print("this is a rectangle")  
#Determine The Oldest And The Youngest People
person1=int(input("enter age:"))
person2=int(input("enter age:"))
person3=int(input("enter age:"))
if(person1<person2):
  print("person1 is youngest")
elif(person2<person3):
  print("person2 is youngest") 
else:
  print("person3 is youngest")
if(person1>person2):
  print("person1 is oldest")
elif(person2>person3):
  print("person2 is oldest") 
else:
  print("person3 is oldestt")
  
#Write an if statement to lets competitor know which of these prises they won.
n=int(input("rate klins from 1 to 200:"))
if(1<=n<=50):
 print("sorry no price this time")
elif(51<=n<=150):
 print("congratulations you won a wooden price")
elif(151<=n<=180):
 print("congratulations you won  books")
elif(181<=n<=200):
 print("congratulations you won  chocolates") 
 
#Print Total Cost after getting discount
quantity=int(input("quantity:"))
print("discount of 10% on 1000")
if(quantity*100>1000):
  print("cost is",(quantity*100)-(10))
else:
   print("cost is",quantity*100)  
 
 
 