l=[1]
l[0]=input("enter any variable")
print(l)
ll=['google','facebook','microsoft','apple','tesla',]
print(l.extend(ll))
print(l)
print(len(l))
l=[7,4,9,5,2,1]
l.sort()
print(l)
A=[3,6,9,4]
B=[2,8,6,5]
A.sort()
B.sort()
print(A,B)
C=A+B
print(C)
l=[1,2,3,4,5,6]
print(l.append(1))
print(l)
print(l.append(3))
print(l)
print(l.pop())
l=[3,7,4,8,9,5]
print(l)
print(l.append(3))
print(l)
print(l.append(4))
print(l)
print(l.pop(0))
print(l)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)