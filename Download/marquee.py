from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()
def go():
    try:
        
        gusion = "Select count(*) from t_register"
        cursor.execute(gusion)
        lesly = cursor.fetchall()[0]
        #response = messagebox.askokcancel("Information","Required {} teacher's for invigilation".format(lesly) )
        #enter.delete(0,END)
        #enter.inser(0,lesly)
        #enter.configure(0,lesly)
        la.configure(text ="Required teacher:{}" .format (lesly))
    except:
        print("error")

root = Tk()
la = Label(root, text = "")
la.pack()
enter = Entry(root, show= "*")
enter.pack()
Button(root, text = "Please click me", command= go).pack()
root.mainloop()