# f=open('new.txt','r')
# x=int(input("enter any:"))
# fd=f.readlines()
# while x:
	# print(fd[-x])
	# x=x-1
# f.close

# Write a Python program to count the frequency of words in a file.
# count=0
# f=open('new.txt','r')
# for line in f:
	# words=line.split()
	# count +=len(words)
# print(count)

#Write a Python program to copy the contents of a file to another file
# with open('new.txt','r') as f1:
	# with open('txt.txt','w') as f2:
		# for line in f1:
			# f2.write(line)
#Write a Python program to combine each line from first file with the corresponding line in second file.
with open('new.txt','r')as f1:
	with open('txt.txt','r')as f2:
		for line1,line2 in zip(f1,f2):
			print(line1+line2)

#Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import os
import random
random_list=[]
random_list1=[]
for x in range (100):
	random_list.append(x)
random.shuffle(random_list)
with open('1.txt','w') as f1:
	for x in range(10):
		f1.write(str(random_list[x])+"\n")
os.remove('2.txt')
with open('1.txt','r+') as f1:
	with open('2.txt','w') as f2:
		random_list=f1.readlines()
		for x in range(len(random_list1)):
			random_list1[x]=int(random_list1[x])
		random_list1.sort()
		for x in random_list1:
			f2.write(str(x)+"\n")