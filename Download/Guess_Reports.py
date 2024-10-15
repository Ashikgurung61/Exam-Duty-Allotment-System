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
    tree = ttk.Treeview(root00, columns = (1,2,3,4,5,6),show = "headings", height = "20")
    tree.place(x = 25, y = 200)

    tree.heading(1, text = "Name")
    tree.heading(2, text = "Phone Number")
    tree.heading(3, text = "Address")
    tree.heading(4,text = "Gender")
    tree.heading(5,text = "Department")
    tree.heading(6, text = "ID")

    s= ttk.Style(root00)  
    s.theme_use("winnative")    

    query = "SELECT t_name, ph_no, address, gender, department, id from t_register "
    cursor.execute(query)  
    rows = cursor.fetchall()   
    #tree.delete(*tree.get_children())
    for i in rows:
            tree.insert("","end",values=i)

def taoko():
    global root00, searche
    root00 = Tk()
    root00.geometry("1250x650+30+15")
    root00.configure(bg = "#326273")
    root00.title("Records")
    root00.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        root00.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    frame = Frame(root00, bd = 10, width = 1200, height= 120, bg = "White")
    frame.place(x = 25, y = 30)

    frame1 = Frame (root00,  height = 121,width=3, background="#326273")
    frame1.place(x = 500, y = 30)

    searchl = Label(root00,text = "Name",font =("Times New Roman",14))
    searchl.place(x = 870, y = 160)

    searchbt = Button(root00, text = "Search", command=search)
    searchbt.place(x = 1130, y = 160)

    searche = StringVar
    searche = Entry(root00,bd = 4,width= 30)
    searche.place(x = 930, y = 160)
      
    E = Label(root00,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 190, y = 30)
    D = Label(root00,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 285, y = 30)
    A = Label(root00,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 190, y = 80)
    S = Label(root00,text = "System", font = "ar 24 bold", fg = "orange").place(x = 350, y = 80)

    heading = Label(root00,text = "I N V I G I L A T O R \n R E C O R D S",bg = "White", font =("Times New Roman",28))
    heading.place(x = 720, y = 40)
    updateT()
    image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = image.resize((90,90),Image.Resampling.LANCZOS)
    new = ImageTk.PhotoImage(resize)
    label = ttk.Label(root00,image=new).place(x = 80, y = 30)

def search():
    value = searche.get()
    query = "Select id, t_name, ph_no, address, gender, department from t_register where t_name LIKE '%"+value+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()

    for j in rows:
         tree.insert("","end",values=j)

    updateT()