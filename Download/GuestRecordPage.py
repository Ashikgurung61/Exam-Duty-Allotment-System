from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from Home_page import *

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()

def updateT():
    global tree
    tree = ttk.Treeview(rt01, columns = (1,2,3,4,5,6),show = "headings", height = "20")
    tree.place(x = 25, y = 200)

    tree.heading(1, text = "Name")
    tree.heading(2, text = "Phone Number")
    tree.heading(3, text = "Address")
    tree.heading(4,text = "Gender")
    tree.heading(5,text = "Department")
    tree.heading(6, text = "ID")

    s= ttk.Style(rt01)  
    s.theme_use("winnative")    

    query = "SELECT t_name, ph_no, address, gender, department, id from t_register "
    cursor.execute(query)  
    rows = cursor.fetchall()   
    #tree.delete(*tree.get_children())
    for i in rows:
        tree.insert("","end",values=i)

def Taoko():
    global searche, tree, rt01
    rt01 = Tk()
    rt01.geometry("1250x650+30+15")
    rt01.title("Invigilator Details")
    rt01.configure(bg = "#326273")
    rt01.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        rt01.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')
    

    frame = Frame(rt01, bd = 10, width = 1200, height= 120, bg = "White")
    frame.place(x = 25, y = 30)

    frame1 = Frame (rt01,  height = 121,width=3, background="#326273")
    frame1.place(x = 500, y = 30)

    searchl = Label(rt01,text = "Name",font =("Times New Roman",14))
    searchl.place(x = 870, y = 160)

    searchbt = Button(rt01, text = "Search", command=search)
    searchbt.place(x = 1130, y = 160)

    searche = StringVar
    searche = Entry(rt01,bd = 4,width= 30)
    searche.place(x = 930, y = 160)
      
    E = Label(rt01,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 190, y = 30)
    D = Label(rt01,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 285, y = 30)
    A = Label(rt01,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 190, y = 80)
    S = Label(rt01,text = "System", font = "ar 24 bold", fg = "orange").place(x = 350, y = 80)

    updateT()

    heading = Label(rt01,text = "I N V I G I L A T O R \n R E C O R D S",bg = "White", font =("Times New Roman",28))
    heading.place(x = 720, y = 40)

    image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = image.resize((90,90),Image.Resampling.LANCZOS)
    new = ImageTk.PhotoImage(resize)
    label = ttk.Label(rt01,image=new).place(x = 80, y = 30)

def search():
    value = searche.get()
    query = "Select id, t_name, ph_no, address, gender, department from t_register where t_name LIKE '%"+value+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    updateT()