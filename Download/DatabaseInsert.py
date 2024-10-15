from tkinter import * 
import mysql.connector
from tkinter import messagebox
from tkinter import ttk


root = Tk()

con = mysql.connector.connect(host = "localhost",user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()


Name = Label(root,text= "Name:").place(x=10,y = 10)
e1 = Entry(root).place(x = 80, y = 10)

Address = Label(root,text= "Address:").place(x=10,y = 40)
e2 = Entry(root).place(x = 80, y = 40)

PNum = Label(root,text= "P_Number:").place(x=10,y = 70)
e3 = Entry(root).place(x = 80, y = 70)

gender = Label(root,text= "Gender:").place(x=10,y = 100)
e4 = Entry(root).place(x = 80, y = 100)


def add():
    try:
        global es1,es3,es2,es4
        es1 = e1.get()
        es2 = e2.get()
        es3 = e3.get()
        es4 = e4.get()
        value = (es1,es2,es3,es4)
        sql = "Insert into t_register (t_Name,ph_no,address,gender) values (%s,%s,%s,%s)"
        cursor.execute(sql, value)
        con.commit()    
        messagebox.showinfo("Success","Successfully Added")
    except Exception as e:
        print(e)
        messagebox.showinfo("Failed","Try Again")
        
submit = Button(root,text = "Submit",width=5,height = 1,border = 2,command = add).place(x = 80,y = 140)
root.mainloop()