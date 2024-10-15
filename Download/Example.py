from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("600x300")
root.title("Hope")

con = mysql.connector.connect(host = "localhost",user="root",passwd ="2020Bca01",database="t_detail")
cursor = con.cursor()

label1 = Label(root,text="Id").pack()
e1 = Entry(root).pack()
label2 = Label(root,text="Name:").pack()
e2 = Entry(root).pack()
label3 = Label(root,text = "Address").pack()
e3 = Entry(root).pack()
label4 = Label(root,text = "Ph.Number:").pack()
e4 = Entry(root).pack()
label5 = Label(root,text = "Gender").pack()
e5 = Entry(root).pack()

def InsertData():
    #global es1,es2,es3,es4,es5
    es1 = e1.get()
    es2 = e2.get()
    es3 = e3.get()
    es4 = e4.get()
    es5 = e5.get()
    try:
        query = "INSERT INTO t_info(ID,T_name,Address,Phone_Number,Gender) values (%s,%s,%s,%s,%s)"
        value = (es1,es2,es3,es4,es5)
        cursor.execute(query,value)
        cursor.commit()
        cursor.close()
        messagebox.showinfo("Success","Data Added")
    except Exception as e:
        print(e)
        messagebox.showinfo("Failed","Try Again")

add = Button(root,text="Add",command=InsertData).place(x =50,y=100)

if(con):
    messagebox.showinfo("Success","Connected")
else:
    messagebox.showinfo("Failed","Unsuccessful")

root.mainloop()