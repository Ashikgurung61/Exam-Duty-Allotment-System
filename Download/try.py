from subprocess import call
from tkinter import * 
root= Tk()
def open_py_file():
    call(["python", "date.py"])

o = Button(root, text = "Click me!!, ",command= open_py_file).pack()
root.mainloop()