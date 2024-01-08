from tkinter import *
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk
from Guess_Status import *


def guesshome():

    root77= Tk()
    root77.geometry("1250x650+30+15")
    root77.configure(bg = "#326273")
    root77.title("Home")
    root77.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        root77.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    dangos=Frame(root77,bd = 5, bg= "White", height= 650, width= 620)
    dangos.place(x=0, y=0)

    Label(root77, text = "Welcome:",bg = "#326273", font = ("Times new roman",14)).place(x = 1100, y = 10)
    Label(root77, text = "Guest",bg = "#326273",fg = "red" ,font = ("Times new roman",20)).place(x = 1180, y = 5)
    image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = image.resize((240,240),Image.Resampling.LANCZOS)
    new = ImageTk.PhotoImage(resize)
    label = ttk.Label(root77,image=new).place(x = 170, y = 230)

    E = Label(root77,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 210, y = 100)
    D = Label(root77,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 315, y = 100)
    A = Label(root77,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 165, y = 150)
    S = Label(root77,text = "System", font = "ar 24 bold", fg = "orange").place(x = 335, y = 150)

    Label(root77,text="Home Page",bg = "#326273", fg = "BLack", font = ("Times new roman",32)).place(x = 830, y = 140)

    def open_py_file2():
        guess_status()

    def open_py_flie3():
        from Guest_Report import Reports1
        Reports1()

        
    def open_py_files4():
        from GuestRecordPage import Taoko
        Taoko()

    def open_py_flie1():
        root77.destroy()

    Button(root77, text="Status",height=4,width=65, command=open_py_file2).place(x = 710, y = 320)
    Button(root77, text="Report",height=4,width=65, command= open_py_flie3).place(x = 710, y = 400)
    Button(root77, text="Records",height=4,width=65, command= open_py_files4).place(x = 710, y = 480)
    Button(root77, text="Exit",height=4,width=65, command= open_py_flie1).place(x = 710, y = 560)


    image1 = Image.open("C:\\Users\\user\\py\\Examples\\images.png")
    resizes = image1.resize((80,80),Image.Resampling.LANCZOS)
    new1 = ImageTk.PhotoImage(resizes)
    label = ttk.Label(root77,image=new1).place(x = 890, y = 40)

    root77.mainloop()