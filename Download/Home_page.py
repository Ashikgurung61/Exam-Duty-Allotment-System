from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from Insert import *
from Registration import *
from Show import *

def home():
    global root1
    root1= Tk()
    root1.geometry("1250x650+30+15")
    root1.configure(bg = "#326273")
    root1.title("Home")
    root1.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        root1.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    dangos=Frame(root1,bd = 5, bg= "White", height= 650, width= 620)
    dangos.place(x=0, y=0)

    image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = image.resize((240,240),Image.Resampling.LANCZOS)
    new = ImageTk.PhotoImage(resize)
    label = ttk.Label(root1,image=new).place(x = 170, y = 230)

    E = Label(root1,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 210, y = 100)
    D = Label(root1,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 315, y = 100)
    A = Label(root1,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 165, y = 150)
    S = Label(root1,text = "System", font = "ar 24 bold", fg = "orange").place(x = 335, y = 150)

    Label(root1,text="Home Page",bg = "#326273", fg = "BLack", font = ("Times new roman",32)).place(x = 830, y = 140)
    
    Button(root1, text="Generate",height=4,width=65, command = insert).place(x = 710, y = 390)
    Button(root1, text="Register",height=4,width=65, command=register).place(x = 710, y = 310)
    Button(root1, text="Records",height=4,width=65, command= show).place(x = 710, y = 470)
    Button(root1, text ="Logout", height=4, width= 10).place(x = 50, y = 700)
    def closed():
        root1.destroy()
        finale()

    Button(root1, text="Exit",height=4,width=65, command= closed).place(x = 710, y = 550)

    image1 = Image.open("C:\\Users\\user\\py\\Examples\\images.png")
    resizes = image1.resize((80,80),Image.Resampling.LANCZOS)
    new1 = ImageTk.PhotoImage(resizes)
    label = ttk.Label(root1,image=new1).place(x = 890, y = 40)

    root1.mainloop()
home()