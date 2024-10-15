from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox 
from GuessHomePage import *
def guesslogin():
    root = Tk()
    root.title("Login")
    root.geometry("1250x650+30+15")
    root.configure(bg = "#326273")

    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    image1 = Image.open("C:\\Users\\user\\py\\Examples\\user.png")
    resizes = image1.resize((80,80),Image.Resampling.LANCZOS)
    new1 = ImageTk.PhotoImage(resizes)
    label = ttk.Label(root,image=new1).place(x = 900, y = 280)

    dango=Frame(root,bd = 5, bg= "white", height= 660, width= 640)
    dango.place(x=0, y=0)

    image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = image.resize((240,240),Image.Resampling.LANCZOS)
    new = ImageTk.PhotoImage(resize)
    label = ttk.Label(root,image=new).place(x = 180, y = 230)

    E = Label(root,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 210, y = 100)
    D = Label(root,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 315, y = 100)
    A = Label(root,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 165, y = 150)
    S = Label(root,text = "System", font = "ar 24 bold", fg = "orange").place(x = 335, y = 150)


    frame = Frame(root, bd = 10,bg = "#326273")
    frame.place(x = 889, y = 380)

    Label(root, text = "Only domain can create new account!",font=("Times New Roman",22),fg = "RED",bg = "#326273").place(x = 750, y = 200)
    Label(frame,text = "Login as",font=("Times New Roman",18),fg = "white",bg = "#326273").grid(row = 1, column = 0)

    def home():
        root.destroy()
        guesshome()
    Button(frame,text=" Guess ",bg = "#326273",border = 0, fg = "Yellow",font=("Times New Roman",12),command= home).grid(row =2, column = 0)
    root.resizable(False,False)

    Label(root,text="I have an account! ",bg = "#326273", fg = "White",font=("Times New Roman",12)).place(x = 710, y = 600)
    def login():
        root.destroy()
        import login
    Button(root,text="Sign up ",bg = "#326273",border = 0, fg = "GREY",font=("Times New Roman",12),command= login).place(x = 830, y = 598)
    root.mainloop()
