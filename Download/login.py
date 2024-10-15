from tkinter import * #Import all the tkinter modules
from tkinter import ttk # import specifically that is ttk module
from Home_page import * #Importing another modules / files with a same folder
from PIL import Image, ImageTk #Image Library
import mysql.connector # This module is used for connecting to the specific database called mysql database
from tkinter import messagebox # import specific module called messagebox module from tkinter

root = Tk()
root.title("Login")
root.geometry("1250x650+30+15")
root.configure(bg = "#326273")
#root.state('zoomed')
try:
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform')

frame = Frame(root, bd = 10,bg = "#326273")
frame.place(x = 813, y = 260)
root.resizable(False,False)

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()

dango=Frame(root,bd = 5, bg= "white", height= 650, width= 620)
dango.place(x=0, y=0)

Label(root,text="Admin Login",bg = "#326273", fg = "WHITE",font=("Times New Roman",25)).place(x = 878, y = 113)
Label(root,text="English (US)",bg = "#326273", fg = "WHITE",font=("Times New Roman",12)).place(x = 935, y = 155)
Label(root,text="Sign in",bg = "#326273", fg = "WHITE",font=("Times New Roman",18)).place(x = 935, y = 245)

image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
resize = image.resize((240,240),Image.Resampling.LANCZOS)
new = ImageTk.PhotoImage(resize)
label = ttk.Label(root,image=new).place(x = 180, y = 230)

E = Label(root,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 210, y = 100)
D = Label(root,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 315, y = 100)
A = Label(root,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 165, y = 150)
S = Label(root,text = "System", font = "ar 24 bold", fg = "orange").place(x = 335, y = 150)

def click(event):
    usernameentry.config(state=NORMAL)
    usernameentry.delete(0,END)
    
def clicks(events):
    passwordentry.config(state=NORMAL)
    passwordentry.delete(0,END)

usernamevalue = StringVar
passwordvalue = StringVar

usernameentry = Entry(frame, bd = 10, width = 40)
passwordentry = Entry(frame, bd = 10 ,  width=40, show = "*")

usernameentry.insert(0,"Username")
usernameentry.config(state=DISABLED)
usernameentry.bind('<Button-1>',click)

passwordentry.insert(1,"Password")
passwordentry.config(state=DISABLED)
passwordentry.bind('<Button-1>',clicks)

usernameentry.grid(row=2, column=3,padx = 20, pady = 20)
passwordentry.grid(row=3, column=3,padx = 20, pady = 20)

def login():
    username = usernameentry.get()
    password = passwordentry.get()
    if (username == "") or (password == ""):
        messagebox.showerror("Empty","Please Enter username and password!!")
    else:
    # Check if the username and password are correct
        log = cursor.execute("SELECT * FROM log_in WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        con.commit()

        if result:
            root.destroy()
            home()
        else:
        # Login failed
            Label(root, text = "Please enter valid username and password",font = ("Times new Roman",11),fg = "Red",bg = "#326273").place(x = 840,y = 410)

Button(frame, text="Login",overrelief=SUNKEN,width = 28, height = 1,bg = "BLUE",font=("Times New Roman",13), command = login).grid(row=5, column=3, pady = 20)

images = Image.open("C:\\Users\\user\\py\\Examples\\Admin.png")
resize = images.resize((55,55),Image.Resampling.LANCZOS)
news = ImageTk.PhotoImage(resize)
label = ttk.Label(root,image=news).place(x = 945, y = 50)

Label(root,text="Don't have an account? ",bg = "#326273", fg = "GREY",font=("Times New Roman",12)).place(x = 910, y = 503)

def ano():
    root.destroy()
    from GuessLogin import guesslogin
    guesslogin()

Button(root,text="Sign up ",overrelief=SUNKEN,bg = "#326273",border = 0, fg = "GREY",font=("Times New Roman",12),command= ano).place(x = 1056, y = 501)

root.mainloop()
