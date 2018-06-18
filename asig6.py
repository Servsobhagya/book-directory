#create a function to calculate area of circle
r=int(input("enter radius of circle"))
def area():
  a=3.14
  area=2*a**r
  print("area:",area)
area()

# Write a Function Perfect And Perform Task


def perfect(n):
	sum=0
	for i in range(1,n):
		if n%i==0:
			sum=sum + i
	if sum==n:
		print("perfect no:",n)
		
for x in range(1,1001):
	perfect(x)
	
#Print multiplication table of 12 using recursion

def table (n):
	if n>10:
		return n
	else:
		print (12*n)
		table(n+1)
table(1)
print("\n")

# Using Recursion Write a FuncTion To Calculate The Power

def power (n,p):
	s=1
	if (p==1):
		return n
	else:
		s=n*power(n,p-1)
		return s
print(power(5,3))

print("\n")


# Write a Function To Find a Factorial
def fact (x):
	if x==1:
		return 1
	else:
		x=x*fact(x-1)
		return x
a=int(input("enter a number:"))
f=fact(a)
print(f)
d=[()]
d.append(f)
print(d)


