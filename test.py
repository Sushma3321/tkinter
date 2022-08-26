

import tkinter
import tkinter as tk
from tkinter import *

# from tkinter import END


root= tkinter.Tk()
root.title("tkinter ")

root.geometry("800x800")
label=tkinter.Label (root,text="Navgurukul  Campus",font=('arial',60),padx=30,pady=50)
label.pack(side=TOP)

def add_item():
    Listbox.insert(tk.END,user_input.get())
def delete_item():
    Listbox.delete(0,tk.END)
    
def select_item():
    Listbox.delete(tk.ANCHOR)
    
    
button1= Button(root, text='add item', padx=20,pady=20,command=add_item,bg="blue",fg="white",font=('arial',10))
button1.pack( side = TOP)

button2 = Button(root, text=' delete item',width=20, padx=20,pady=20,command=delete_item,bg="red",fg="white",font=('arial',10))
button2.pack( side = TOP)

button3 = Button(root, text='delete select item',width=20, padx=20,pady=20,command=select_item,bg="pink",fg="black",font=('arial',10))
button3.pack( side = TOP)


Listbox = Listbox(root,width=60,height=20,bg="skyblue",fg="black")
Listbox.pack(side=BOTTOM)



user_input=Entry(root,width=20,font=('arial',30),bg="orange",fg="black")
user_input.pack(side=TOP)

root.mainloop()

    
    