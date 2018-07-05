#Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.


import tkinter
from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry('200x200')
a=Label(root,text="Dictionary \nNames and Mobile Number",bg="blue")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

w=Scrollbar(f1,orient="vertical",)
w.pack(side=RIGHT,fill=Y)
mylist=Listbox(f1,width=30 , font=("Helvetica", 12),yscrollcommand=w.set)



d={"bikram":999,"rajat":895,"vijay":567,"vivek":5658,}

for key in d:
    mylist.insert(END,'{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
w.config(command=mylist.yview)
root.mainloop()



#Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
import tkinter
from tkinter import *

def show():
    k=entry.get()
    v=entry2.get()
    mylist.insert(END,'{}: {}'.format(k, v))
    d[k]=v
    print(d)

root=Tk()
root.title("Dictionary")
root.geometry('200x200')
a=Label(root,text="Dictionary \nNames and Mobile Number",bg="blue")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

w=Scrollbar(f1,orient="vertical",)
w.pack(side=RIGHT,fill=Y)
mylist=Listbox(f1,width=30 , font=("MT Bold", 12),yscrollcommand=w.set)



d={"bikram":999,"vijay":895,"niki":567,"virat":5658,"rudoff":6576,"yuvi":45747,"rohit":5345,"hacker":45678,"ram":4586,"serv":809687}

for key in d:
    mylist.insert(END,'{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
w.config(command=mylist.yview)

entry=Entry(root,width=20)
entry.pack()
entry2=Entry(root,width=20)
entry2.pack()
b=Button(root,text="insert",bg="pink",command=show)
b.pack()
root.mainloo