from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(user = "root",host = "localhost",passwd= "2020Bca01", database = "trial")
cursor = con.cursor()
root = Tk()

def insert():
    try:
        global e1, e2
        e1 = selectshif.get()
        e2 = choice.get()
        value = (e1, e2)
        sql = "Insert into swap (Name, status) value (%s,%s)"
        cursor.execute(sql,(value))
        con.commit()
        if choice == t:
            messagebox.showinfo("Selected","Here")
        elif choice == t1:
            messagebox.showinfo("Selected","There")
        label1.configure(text=choice.get())
        messagebox.showinfo("Successful","Correct")
    except:
        print("Error")
label1 = Label(root, text = "Show it here")
label1.grid(row = 2, column = 0)
selectshif = Entry(root, bd = 0, bg = "Grey")
selectshif.grid(row = 0, column = 0)
choice = StringVar()
t = Radiobutton(root, text = "Here",value = "0", variable= choice)
t.grid(row = 1, column = 0)
t1 = Radiobutton(root, text = "There",value = "1", variable= choice)
t1.grid(row = 1, column = 1)
Button(root, text = "Insert",command= insert).grid(row = 3, column= 0)
root.mainloop()