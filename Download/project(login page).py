from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox 
from subprocess import call

root = Tk()
root.geometry("1250x650")
root.configure(bg = "#326273")
root.configure(bg = "#326273")

frame = Frame(root, bd = 2)
frame.place(x = 850, y = 350)
root.resizable(False,False)

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()

dango=Frame(root,bd = 5, bg= "white", height= 650, width= 620)
dango.place(x=0, y=0)
Label(root,text="Login Form",bg = "#326273", fg = "Yellow", font=(" Times new roman",24)).place(x = 873, y = 100)

h1 = Label(root,text = "Exam Duty", font = ("Times new Roman",32),background="white").place(x = 166, y = 140)
h2 = Label(root,text = " Allotment System", font = ("Times new Roman",28),background = "white").place(x = 122, y = 190 )

image = Image.open("C:\\Users\\user\\py\\logo.png")
resize = image.resize((200,200),Image.Resampling.LANCZOS)
new = ImageTk.PhotoImage(resize)
label = ttk.Label(root,image=new).place(x = 170, y = 230)

username = Label(frame, text="UserName")
password = Label(frame, text="Password")

username.grid(row=2,column=1,padx = 10, pady = 10)
password.grid(row=3,column=1,padx = 10, pady = 10)

usernamevalue = StringVar
passwordvalue = StringVar

usernameentry = Entry(frame, bd = 3)
passwordentry = Entry(frame, bd = 3)

usernameentry.grid(row=2, column=3,padx = 10, pady = 10)
passwordentry.grid(row=3, column=3,padx = 10, pady = 10)

def login():

    username = usernameentry.get()
    password = passwordentry.get()
    if (username =="") or (password == ""):
        messagebox.showerror("Empty","Please Enter username and password!!")
    else:
    # Check if the username and password are correct
        cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        con.commit()
        if result:
        # Login successful
            response = messagebox.showinfo("Success","Press ok to continue...")
            if response == 1:
                call(["python","Home_page.py"])
            else: 
                return True
        else:
        # Login failed
            messagebox.showwarning("Failed","Please try again later")

Button(frame, text="Login", command = login).grid(row=5, column=3)
root.mainloop()
