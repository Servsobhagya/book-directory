#sets create intersection and diffrence of a set
n=set(input("enter element 1: "))
m=set(input("enter element 2:"))
print (n)
print(m)
print("diffrence between two sets",n-m)
print("intersection between two sets",n&m)
print("compare between two sets",n==m)
d={}
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
name=input("ernter name:")
marks=int(input("enter marks:"))
d[name]=marks
print(d)



d={}
l=[]
for x in range(4):

	name=input("enter name")
	marks=int(input("enter marks"))
	l.append(marks)
	d[name]=marks
	 
print(d)
l.sort()
print(l) 


l=["M","I","S","S","I","S","S","I","P","P","I"]
a = l.count('M')
b = l.count('I')
c = l.count('S')
e = l.count('P')
d={}  
d["m"]=a
d["i"]=b
d["s"]=c
d["p"]=e
print(d)

t1=[1,2,3,4,5]
t2=["serv","rudoff","amit"]
print(len(t1))
print(len(t2))
print(t1,t2)
print(max(t1))
print(min(t1))
print(max(t2))
print(min(t2))


t=[1,2,3,4,5]
k=t[0]*t[1]*t[2]*t[3]*t[4]
print(k)

