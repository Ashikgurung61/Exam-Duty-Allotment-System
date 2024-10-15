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
    tree = ttk.Treeview(root88, columns = (1,2,3,4,5,6),show = "headings", height = "15")
    tree.place(x = 25, y = 200)

    tree.heading(1, text = "Name")
    tree.heading(2, text = "Phone Number")
    tree.heading(3, text = "Address")
    tree.heading(4,text = "Gender")
    tree.heading(5,text = "Department")
    tree.heading(6, text = "ID")

    s= ttk.Style(root88)  
    s.theme_use("winnative")    

    query = "SELECT t_name, ph_no, address, gender, department, id from t_register "
    cursor.execute(query)  
    rows = cursor.fetchall()   
    #tree.delete(*tree.get_children())
    for i in rows:
        tree.insert("","end",values=i)

def select_record():
    global selected, vale
    nameentry.delete(0,END)
    phonenoentry.delete(0,END)
    addressentry.delete(0,END)
    genderentry.delete(0,END)
    deptentry.delete(0,END)
    id1.delete(0,END)

    selected = tree.focus()
    vale = tree.item(selected,"values")
  
    nameentry.insert(0,vale[0])
    phonenoentry.insert(0,vale[1])
    addressentry.insert(0,vale[2])
    genderentry.insert(0,vale[3])
    deptentry.insert(0,vale[4])
    id1.insert(0,vale[5])
    updateT()

def get_new():
    global ids, t_name, ph_no, address, gender
    ids = id1.get()
    t_name = nameentry.get()
    ph_no = phonenoentry.get()
    address = addressentry.get()
    gender = genderentry.get()
    department = deptentry.get()
    
    value = (t_name, ph_no, address, gender, department, ids)
    try:
        query = "Update t_register set t_name = %s, ph_no = %s, address = %s, gender = %s, department = %s  where id = %s"
        cursor.execute(query, value)
        con.commit()
        #clear()
    except:
        messagebox.showerror("Fail","Error!!")
    updateT()
def deleteshow():
    try:
        global e1
        e1 = id1.get()
        sql = "Delete from t_register where id ="+e1
        cursor.execute(sql)
        con.commit()
        messagebox.showinfo("Success","The Selected data was delete successfully")
    except:
        messagebox.showerror("Erro","Please console the domain for the problem")

def show():
    global id1,delt, nameentry, addressentry, genderentry, deptentry, phonenoentry, searche, tree, root88
    root88= Tk()
    root88.geometry("1250x650+30+15")
    root88.title("Invigilator Details")
    root88.configure(bg = "#326273")
    root88.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        root88.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    #updateT()
    frame = Frame(root88, bd = 10, width = 1200, height= 120, bg = "White")
    frame.place(x = 25, y = 30)

    #hay = Label(root88, text = "I N V I G I L E L A T O R \n RECORD", font = ("TImes new roman, 18"))
    #hay.place(x = 700, y = 70)
    frame1 = Frame (root88,  height = 121,width=3, background="violet")
    frame1.place(x = 500, y = 30)

    slt = Button(root88,overrelief=SUNKEN,text ="Select",width = 14, height = 1, background="Grey",command = select_record)
    slt.place(x = 580, y = 620)

    searchl = Label(root88,text = "Select Department",font =("Times New Roman",14),bg = "#326273")
    searchl.place(x = 820, y = 160)

    searchbt = Button(root88, overrelief=SUNKEN,text = "Search", command=search)
    searchbt.place(x = 1130, y = 160)

    back = Button(root88, bd = 0, overrelief=SUNKEN,width = 10,bg = "#326273", text = "Home", fg = "White", command= root88.destroy).place(x = 0, y = 0)

    
    searche =ttk.Combobox(root88,values =["","BCA","PHY","CHM","ZOO","BOT","BTT","HIS","BCOM","SOC","POL","EDU","BSW","ENG"])
    searche.place(x = 980, y = 160)
    #updateT()
    fra = Frame(root88,border = 3)
    fra.place(x = 145, y = 530)
    
    id = Label(fra, text ="ID", background="Grey")
    name = Label(fra, text="Name",background="Grey")
    address = Label(fra, text="Address",background="Grey")
    phone = Label(fra, text="Phone No:",background="Grey")
    gender = Label(fra, text="Gender",background="Grey")
    dept = Label(fra, text="Department",background="Grey")

    name.grid(row = 1, column = 0, padx = 5, pady = 5)
    address.grid(row = 1, column = 2, padx = 5, pady = 5)
    phone.grid(row = 1, column = 1, padx = 5, pady = 5)
    gender.grid(row = 1, column = 3, padx = 5, pady = 5)
    dept.grid(row = 1, column = 4, padx = 5, pady = 5)
    id.grid(row = 1, column = 5, padx = 5, pady = 5 )

    id1 = Entry(fra, bd = 3)
    nameentry = Entry(fra, bd = 3)
    phonenoentry = Entry(fra, bd = 3)
    addressentry = Entry(fra, bd = 3)
    genderentry = Entry(fra, bd = 3)
    deptentry = Entry(fra, bd = 3)
    #updateT()
    nameentry.grid(row = 0, column = 0, padx = 10, pady = 10)
    addressentry.grid(row = 0, column = 2, padx = 10, pady = 10)
    phonenoentry.grid(row = 0, column = 1, padx = 10, pady = 10)
    genderentry.grid(row = 0, column = 3, padx = 10, pady = 10)
    deptentry.grid(row = 0, column = 4, padx = 10, pady = 10)
    id1.grid(row = 0, column = 5, padx = 10, pady = 10)

    upd = Button(root88,text = "Update", width = 14,height = 1, background="Green", command=get_new)
    upd.place(x = 420, y = 620)

    delt = Button(root88,overrelief=SUNKEN, text = "Delete", width = 14,height = 1, background="Red", command= deleteshow)
    delt.place(x = 740, y = 620)

    tree = ttk.Treeview(root88, columns = (1,2,3,4,5,6),show = "headings", height = "15")
    tree.place(x = 25, y = 200)

    tree.heading(1, text = "Name")
    tree.heading(2, text = "Phone Number")
    tree.heading(3, text = "Address")
    tree.heading(4,text = "Gender")
    tree.heading(5,text = "Department")
    tree.heading(6, text = "ID")

    s= ttk.Style(root88)  
    s.theme_use("winnative")    

    query = "SELECT t_name, ph_no, address, gender, department, id from t_register "
    cursor.execute(query)  
    rows = cursor.fetchall()   
    #tree.delete(*tree.get_children())
    for i in rows:
        tree.insert("","end",values=i) 
    
    E = Label(root88,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 190, y = 30)
    D = Label(root88,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 285, y = 30)
    A = Label(root88,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 190, y = 80)
    S = Label(root88,text = "System", font = "ar 24 bold", fg = "orange").place(x = 350, y = 80)

    """image = Image.open("C:\\Users\\user\\py\\Examples\\logo1.png")
    resize = image.resize((90,90),Image.Resampling.LANCZOS)
    new = ImageTk.PhotoImage(resize)
    label = ttk.Label(root88,image=new).place(x = 80, y = 30)
"""
def search():
    value = searche.get()
    query = "Select t_name, ph_no, address, gender, department, id from t_register where t_name LIKE +'%value%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    updateT()

def delete():
    ids = id1.get()
    selected = tree.selection()[0]
    try:
        query = "Delete from t_register where id = %s"#+id1.get()
        c = cursor.execute(query,selected)
        if(c.rowcount==1):
            tree.delete(selected)
            messagebox.showwarning("Warning","Deleted")
        else:
            messagebox.showinfo("failed","Try Again Later")
        
    except:
        messagebox.showinfo("failed","Try Again Later")
    root88.mainloop()
