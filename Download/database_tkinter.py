import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("Add Detail")
root.resizable(0,0)

try:
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform')

con = mysql.connector.connect(host = "localhost",
user="root", passwd="2020Bca01", database = "t_detail")

cursor = con.cursor()
#cursor.execute("Select * from t_register ORDER BY RAND() LIMIT 3")
cursor.execute("Select * from t_register")
tree = ttk.Treeview(root)
tree['show']='headings'

s= ttk.Style(root)
s.theme_use("alt")

#------------------------------------Define number of columns------------------------------------
tree["columns"] = ("id","t_name","ph_no","address","gender")

#------------------------------assign the width, minwidth----------------------------------------- 
# ---------------------------anchor to the respecive columns--------------------------------------
tree.column("id", width = 50, minwidth=50)
tree.column("t_name", width = 100, minwidth=100)
tree.column("ph_no", width = 50, minwidth=50)
tree.column("address", width = 150, minwidth=150)
tree.column("gender", width = 150, minwidth=150)

#-------------------Assign the headingnames to the respective columns------------------------------

tree.heading("id", text = "ID")
tree.heading("t_name", text = "Invigilator")
tree.heading("ph_no", text = "Phone Number")
tree.heading("address", text = "Address")
tree.heading("gender", text = "Gender")

i = 0
for ro in cursor:
    tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
    i += 1
tree.pack()

frame = Frame(root, bd = 10,height = 50, width = 10)
frame.place(x = 170, y = 230)

uname = Label(frame, text = 'ID: ', fg = "Blue")
uname.grid(row = 1, column = 1)

uname2 = Entry(frame, bg = "#C0C0C0")#----------------
uname2.grid(row = 1, column = 2)

pwd01 = Label(frame, text = "Name:", fg = "Blue")
pwd01.grid(row = 2,  column = 1)

pwd02 = Entry(frame, bg = "#C0C0C0")#------------------------
pwd02.grid(row = 2, column = 2)

ph = Label(frame, text = 'Phone Number ', fg = "Blue")
ph.grid(row = 3, column = 1)

uname21 = Entry(frame, bg = "#C0C0C0")#--------------------
uname21.grid(row = 3, column = 2)

pwd011 = Label(frame, text = "Address", fg = "Blue")
pwd011.grid(row = 4,  column = 1)

pwd022 = Entry(frame, bg = "#C0C0C0")#-----------------------
pwd022.grid(row = 4, column = 2)

gen = Label(frame, text = "Gender")
gen.grid(row = 5, column = 1)

genen = Entry(frame, bg = "#C0C0C0")#-----------------
genen.grid(row = 5, column = 2)

ph = IntVar
pwd01 = StringVar
uname2 = IntVar

def add():
    

Ent = Button(frame, text = "Enter")
Ent.grid(row = 7, column = 1)

root.mainloop() 