from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()
def treeview1():
    tree = ttk.Treeview(root2, columns = (1),show = "headings", height = "21")

    s= ttk.Style(root2)  

    s.theme_use("winnative")
    
    tree['columns'] = ("Invigilator")

    #assign the width, minwidth 
        
    tree.column("Invigilator",width = 208, minwidth = 80,anchor='center')

    tree.heading("Invigilator", text = "Invigilator Names")

    sql = "Select t_name from t_register where status = -1"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row1 in result:
            tree.insert('',"end",values=row1)

    tree.place(x = 300, y = 200)

def treeview2():
    trv = ttk.Treeview(root2, columns = (1),show = "headings", height = "21")

    s= ttk.Style(root2)  
    s.theme_use("winnative")
    
    trv['columns'] = ("Invigilator")

    #assign the width, minwidth 
    trv.column("Invigilator",width = 208, minwidth = 80,anchor='center')

    trv.heading("Invigilator", text = "Invigilator Names")

    mydb = "Select t_name from t_register where status = 0 AND 1"
    cursor.execute(mydb)
    results = cursor.fetchall()

    for row11 in results:
            trv.insert('',"end",values=row11)
    trv.place(x = 750, y = 200)

def guess_status():
    global root2
    root2= Tk()
    root2.geometry("1250x650+30+15")
    root2.title("Report page")
    root2.configure(bg = "#326273")
    root2.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        root2.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    
    frame = Frame(root2, bd = 10, width = 1200, height= 120, bg = "White")
    frame.place(x = 25, y = 20)

    fr = Frame(root2,bg = "white")

    E = Label(fr,text="Exam",fg = "Navy BLue", font="ar 32 bold",bg = "white").grid(row = 0, column=0,padx = 8)
    D = Label(fr,text = "Duty", font = "ar 32 bold", fg = "RED",bg = "white").grid(row = 0, column=1,padx = 8)
    A = Label(fr,text = "Allotment", font = "ar 32 bold", fg = "green",bg = "white").grid(row = 0, column=2,padx = 8)
    S = Label(fr,text = "System", font = "ar 32 bold", fg = "orange",bg = "white").grid(row = 0, column=3,padx = 8)

    fr.place(x = 330, y = 20)
    CollegeName = Label(root2, bg = "white",text = "Invigilator Status",fg = "Black",font=("Times New Roman",24))
    CollegeName.place(x = 510, y = 85)

    Label(root2, text = "Unavailable Teacher",fg = "white",font = ("Times New Roman",16),bg = "#326273").place(x = 325, y =  165)
    Label(root2, text = "Available Teacher",fg = "white",font = ("Times New Roman",16),bg = "#326273").place(x = 780, y =  165)
    
    btn10 = Button(root2, text = "Back",font = ("Times new roman",12),fg = "Red",bd = 0,bg = "#326273")
    btn10.place(x = 0, y = 620)
    
    treeview1()
    treeview2()

    images = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = images.resize((100,100),Image.Resampling.LANCZOS)
    news = ImageTk.PhotoImage(resize)
    label = ttk.Label(root2,image=news).place(x = 80, y = 30)

    root2.mainloop()
