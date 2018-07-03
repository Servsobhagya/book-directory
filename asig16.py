#Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
# from tkinter import *
# root=Tk()
# b=Button(root,text="hello world")
# b.pack()
# b1=Button(root,text="exit",command=exit)
# b1.pack()
# root.mainloop()

# Write a python program to in the same interface as above and create a action when the button is click it will display some text.
# from tkinter import *
# def show():
	# print("hello world")
# root=Tk()
# b=Button(root,text="click",bg="blue",font="black",command=show)
# b.pack()
# b1=Button(root,text="exit",bg="blue",font="black",command=exit)
# b1.pack()
# root.mainloop()

#Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
# from tkinter import *
# def show():
	# var.set("rudoff")
# root=Tk()
# var= StringVar()
# b=Button(root,text="click",command=show)
# b.pack()
# b1=Button(root,text="exit",command=exit)
# b1.pack()
# var.set("how are you")
# label=Label(textvariable=var)
# label.pack()
# root.mainloop()

# Write a python program using tkinter interface to take an input in the GUI program and print it.
from tkinter import *
def show():
	print(entry.get())
root=Tk()
entry=Entry(root,bg="blue",width=40)
entry.pack()
b1=Button(root,text="click",command=show)
b1.pack(side=TOP)
b2=Button(root,text="exit",command=exit)
b2.pack()
root.mainloop()
