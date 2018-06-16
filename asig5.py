#Take a Input From User and Print On Screen
# n=1
# while n<=10:
  # print("hello",n)
  # n=n+1 
    
#Write an Infinite Loop
# n=1
# while n<=10:
  # print("rudoff",n)
  

#Create a List of Integers And Make a New List
# l=[]
# l.append(int(input("enter integer")))  
# l.append(int(input("enter integer")))  
# l.append(int(input("enter integer")))
# n=[]
# for x in l:
	# n.append(x**2)
# print(l)
# print(n)   

#From a list for Integer,Float and String

# if type(n[0])==int:
	# print("int")
# else:
	# print("not int")
# l=[1,2,'a',78,7.2,'b',1.5,4.6]
# l1=[]
# l2=[]
# l3=[]
# for x in l:
	# if type(x)==int:
		# l1.append(x)
	# elif type(x)==float:
		# l2.append(x)
	# elif type(x)==str:
		# l3.append(x)
# print(l1)
# print(l2)
# print(l3)
#Using range(1,101), make a list containing even and odd numbers.
# l=[]
# l1=[]
# for x in range (1,101):
	# if (x%2==0):
	 # l.append(x)
	# else:
	 # l1.append(x)
# print(l)
# print(l1)

#Print Patterns
# for i in range(0,5):
 # for j in range (0,i+1):
  # print("*",end="")
 # print() 

 #Create a User Defined Dictionary
d={}
for i in range (0,2):
  text=input("enter char and int").split()
  d[text[0]]=text[1]
print(d)
#perform inputs and search and deletion from user in list
l=[]
for i in range(0,5):
  l.append(input("enter list:"))
print(l)
l1=[]
l1.append(input("enter to search remove element from list:"))
print(l1)
for x in l:
 if x in l1:
  l.remove(x)
print(l)
  
 



	
		
	


  
  
  
  
  