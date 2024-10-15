from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

# The given below code is used for connecting to mysql database
con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()

def add():
    global e1, e2, e3, e4, e5, e6

    e1 = name.get()
    e2 = ph.get()
    e3 = address.get()
    e4 = gender.get()
    e5 = department.get()
    e6 = status.get()
    e7 = 0
    if e1 == "" or e2 == "" or e3 == "" or e4 == "" or e5 == "" or e6 == "":
        empty = Label(root20,text="*Don't leave the fill blank",bg = "#326273", fg = "Red",font=("Times New Roman",14)).place(x = 840, y = 210)
    else:
        try:
            value = e1, e2, e3, e4, e5, e6, e7
            sql = "INSERT INTO t_register(t_name, ph_no, address, gender, department, status,cnt) values (%s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(sql, value)
            con.commit()
            if (con):
                #empty.destroy()
                naya = Label(root20,text="*Successfully Submitted*",bg = "#326273",fg = "Black", font = ("Times new Roman",20)).place(x =790, y = 550)
        except:
            messagebox.showwarning("Fail",">Error<")
    
def clear():
    name.delete(0,END)
    ph.delete(0,END)
    address.delete(0,END)
    gender.delete(0,END)
    department.delete(0,END)
    status.delete(0,END)

def back():
    root20.destroy()
def register():
    
    global root20, name, ph, address, gender, department, status
    root20= Tk()
    root20.geometry("1250x650+30+15")
    root20.title("Registration")
    root20.configure(bg = "#326273")
    root20.resizable(0,0)

    try:
        root20.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    doggo = Frame(root20,bd = 5, bg= "WHite", height= 650, width= 620)   
    doggo.place(x=0, y=0)   
    
    E = Label(root20,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 210, y = 100)
    D = Label(root20,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 315, y = 100)
    A = Label(root20,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 165, y = 150)
    S = Label(root20,text = "System", font = "ar 24 bold", fg = "orange").place(x = 335, y = 150)

    Label(root20,text="REGISTRATION",bg = "#326273",fg = "Grey", font = ("Times new Roman",34)).place(x =780, y = 30)

    frame = Frame(root20, bg = "#326273")
    frame.place(x = 780, y = 230)

    name = Label(root20, text="Name:",bg = "#326273",font = ("Times New Roman", 14),fg = "WHite", anchor="e")
    address = Label(root20, text="Address:",bg = "#326273",font = ("Times New Roman", 14),fg = "WHite",anchor="e")
    phone = Label(root20, text="Phone No:",bg = "#326273",font = ("Times New Roman", 14),fg = "WHite",anchor="e")
    gender = Label(root20, text="Gender:",bg = "#326273", font = ("Times New Roman", 14),fg = "WHite",anchor="e")
    dept = Label(root20, text="Department:",bg = "#326273",font = ("Times New Roman", 14),fg = "WHite",anchor="e")
    sta = Label(root20, text="Status:",bg = "#326273",font = ("Times New Roman", 14),fg = "WHite",anchor="e")

    name.place(x = 680,y = 240)
    phone.place(x = 680,y = 293)
    address.place(x = 680,y = 346)
    gender.place(x = 680,y = 399)
    dept.place(x = 680,y = 452)
    sta.place(x = 680,y = 505)
    #--------------------------Entry---------------------------------
    name = Entry(frame, bd = 1,width=60,bg = "white")
    #nameline = Frame(root20, bd = 8, width = 370, bg = "Black").place(x = 790, y = 265)
    name.grid(row = 1, column = 0, padx = 10, pady = 16)

    ph = Entry(frame, bd = 1,width=60,bg = "white")
    #phline = Frame(root20, bd = 8, width = 370, bg = "Black").place(x = 790, y = 315)
    ph.grid(row = 2, column = 0, padx = 10, pady = 16)

    address = Entry(frame,bd = 1,width=60,bg = "White")
    #addressline= Frame(root20, bd = 8, width = 370, bg = "Black").place(x = 790, y = 365)
    address.grid(row = 3, column = 0, padx = 10, pady = 16)

    gender = ttk.Combobox(root20,values = ["","Male","Female","Other"], width = 57)
    #genderline= Frame(root20, bd = 8, width = 388, bg = "Black").place(x = 786, y = 424)
    gender.place(x =790, y = 399 )

    department = ttk.Combobox(root20,values = ["","BCA","PHY","CHM","ZOO","BOT","BTT","HIS","BCOM","SOC","POL","EDU","BSW","ENG"], width = 57)
    #departmentline= Frame(root20, bd = 8, width = 388, bg = "Black").place(x = 786, y = 477)
    department.place(x = 790,y = 452)

    status = ttk.Combobox(root20, value = ["", "0","1"], width = 57)
    #statusline= Frame(root20, bd = 8, width = 388, bg = "Black").place(x = 786, y = 530)
    status.place(x = 790,y = 505)

    #---------------------------------------------------------------
    btn20 = Button(root20, text="Submit",overrelief=SUNKEN, width = 10,height= 1,bg = "violet", command = add).place(x = 860, y = 595)
    btn2020 = Button(root20, text="Clear", overrelief=SUNKEN,width = 10,height= 1,bg = "Pink", command = clear).place(x = 980, y = 595)

    back = Button(root20, bd = 0, width = 10,bg = "#326273", text = "Home", fg = "White",overrelief=SUNKEN, command= root20.destroy).place(x = 0, y = 0)
    #Label(root20, text = "0 = Un-Available \n 1  = Available", fg = "Red", bg = "#326273").place(x = 1100, y = 550)
    labs = LabelFrame(root20, text="Information",bd = 3,font=("Times New Roman",14), fg ="Red", background="White")
    labs.place(x = 30, y = 480, width = "560",height="135")

    notes = Label(labs, text = " a. Don't leave any fill blank \n b. Provide correct information for future references\n c. Status: It tells whether the invigilator is avialable or Unavailable \n     0 = Unavailable, 1 = Available",font=("Times New Roman",11),justify="left", bg = "white")
    notes.grid(row = 0, column = 0)

    
    #new = ImageTk.PhotoImage(resize)
    #label = ttk.Label(root20,image=new).place(x = 180, y = 230)

    news1 = ImageTk.PhotoImage(file = "Logo1.png")
    labe = ttk.Label(root20,image=news1)
    labe.place(x = 208, y = 230)

    root20.mainloop()

