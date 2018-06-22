#Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
import time
time.sleep(5)
from threading import Thread
def display():

	print("child class:",threading.current_thread())
t=Thread(target=display)
t.start()
	

#Make a thread that prints numbers from 1-10, waits for 1 sec between
import threading
import time
time.sleep(1)
from threading import Thread
def display():
	for x in range(1,10):
		print("a")
t=Thread(target=display)
t.start()


# Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
# Delay goes like 2sec-4sec-6sec-8sec-10sec
l=[1,2,3,4,5]
import threading
from threading import Thread
import time
def display():
	s=2
	for x in l:
		print(x)
		time.sleep(s)
		s=s+2
t=Thread(target=display)
t.start()
	
	#Call factorial function using thread.
import threading
from threading import Thread
def factorial():
	fact=1
	n=int(input("enter any no"))
	for x in range(1,n+1):
		fact=fact*x

	print(fact)
t=Thread(target=factorial)
t.start()
	
	

	

	
