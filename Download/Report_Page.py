from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01", database = "t_detail")
cursor = con.cursor()
def table1():#Morning shift table
    global tree
    tree = ttk.Treeview(root3, columns = (1,2),show = "headings", height = "21")
    s= ttk.Style(root3)  
    s.theme_use("winnative")
    sql = "Select id,t_name from t_register where status = 0"
    cursor.execute(sql)
    result = cursor.fetchall()
    tree['columns'] = ("Id","Invigilator Name")

    tree.heading("Id", text = "Id")
    tree.heading("Invigilator Name", text = "Invigilator Name")

    #assign the width, minwidth 
    tree.column("Id", width = 50, minwidth=50) 
    tree.column("Invigilator Name",width = 200, minwidth = 80)

    for row in result:
        tree.insert('',"end",values=row)
   
    tree.place(x = 50, y = 165)
    tree.bind("<<TreeviewSelect>>",selecttree1)

def table2():#Evening Shift Table
    global trees, results
    trees = ttk.Treeview(root3, columns = (1,2),show = "headings", height = "21")
    s= ttk.Style(root3)  
    s.theme_use("winnative")

    mydb = "Select id,t_name from t_register where status = 1"
    cursor.execute(mydb)
    results = cursor.fetchall()

    trees['columns'] = ("Id","Invigilator Name")

    trees.heading("Id", text = "Id")
    trees.heading("Invigilator Name", text = "Invigilator Name")

    #assign the width, minwidth 
    trees.column("Id", width = 50, minwidth=50) 
    trees.column("Invigilator Name",width = 200, minwidth = 80)

    for row in results:
        trees.insert('',"end",values=row)
    trees.place(x = 950, y = 165)
    
    trees.bind("<<TreeviewSelect>>",selecttree2)

def table3():#Unavailable table
    global ruk, solution,ruk
    ruk = ttk.Treeview(root3, columns = (1,2),show = "headings", height = "21")
    s= ttk.Style(root3)  
    s.theme_use("winnative")

    mydatabase = "Select id,t_name from t_register where status = -1"
    cursor.execute(mydatabase)
    solution = cursor.fetchall()

    ruk['columns'] = ("Id","Invigilator Name")

    ruk.heading("Id", text = "Id")
    ruk.heading("Invigilator Name", text = "Invigilator Name")

    #assign the width, minwidth 
    ruk.column("Id", width = 50, minwidth=50) 
    ruk.column("Invigilator Name",width = 200, minwidth = 80)

    for i in solution:
        ruk.insert('',"end",values=i)

    ruk.place(x = 502, y = 165)
   
    ruk.bind("<<TreeviewSelect>>",selecttree3)
    
#-----------------------------------------1nd Treeview-----------------------------------------
def left():
    global e1
    try:
        con.connect()
        e1 = ai.get()
        toleft = "Update t_register set status = 0 where id = "+e1
        cursor.execute(toleft)
        con.commit()
        table2()
        table1()
        table3()
    except:
        print("error")
#-----------------------------------------2nd Treeview-------------------------------------------

def right():
    global e2
    try:
        e2 = ai.get()
        toright = "Update t_register set status = 1 where id = "+e2
        cursor.execute(toright)
        con.commit()
        table2()
        table1()
        table3()
    except:
        print("error")
        
def unavailable():
    global e3
    try:
        e3 = ai.get()
        tomiddle = "Update t_register set status = -1 where id = "+e3
        cursor.execute(tomiddle)
        con.commit()
        table2()
        table1()
        table3()
    except:
        print("error")

#def select_invigilator():

    #ai.delete(0,END)
    #selected = ruk.focus()
    ##valir = ruk.item(selected,"values")
    #ai.insert(0,valir[0])

    
def search_invigilator():
    e1 = khoj.get()
    query = "select t_name from t_register where department like '%+e1+%'"
    cursor.execute(query)
    read = cursor.fetchall()
    for j in read:
        ruk.insert("","end",values= j)
    table3()

def NewEntry():
    if messagebox.askokcancel("Are you Sure!","Create a new Sheet?"):
        sql = "Update t_register set status = -1 where id < 10000;"
        cursor.execute(sql)
        con.commit()
        table1()
        table2()
        table3()
    else:
        return True
    
def selecttree1(event1):
    selection=tree.focus()
    data=tree.item(selection,"values")
    ai.delete(0,END)
    ai.insert(0,data[0])

def selecttree2(event2):
    selection=trees.focus()
    data1=trees.item(selection,"values")
    ai.delete(0,END)
    ai.insert(0,data1[0])

def selecttree3(event3):
    selection=ruk.focus()
    data2=ruk.item(selection,"values")
    ai.delete(0,END)
    ai.insert(0,data2[0])


def swap():
    try:
        cursor.execute("Update t_register set status = 2 where status = 0")
        con.commit()
        cursor.execute("Update t_register set status = 0 where status = 1")
        con.commit()
        cursor.execute("Update t_register set status = 1 where status = 2")
        con.commit()
        table1()
        table2()
        #messagebox.showinfo("0k","Oa")
    except:
        print("error")
def close_Report_Page():
    root3.destroy()
        
def report():
    global ai, root3, khoj, ai1
    root3= Tk()
    root3.geometry("1250x680+30+15")
    root3.title("Status")
    root3.configure(bg = "#326273")
    root3.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        root3.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    frame = Frame(root3, bd = 10, width = 1200, height= 120, bg = "White")
    frame.place(x = 25, y = 5)

    fr = Frame(root3,bg = "white")

    E = Label(fr,text="Exam",fg = "Navy BLue", font="ar 32 bold",bg = "white").grid(row = 0, column=0,padx = 8)
    D = Label(fr,text = "Duty", font = "ar 32 bold", fg = "RED",bg = "white").grid(row = 0, column=1,padx = 8)
    A = Label(fr,text = "Allotment", font = "ar 32 bold", fg = "green",bg = "white").grid(row = 0, column=2,padx = 8)
    S = Label(fr,text = "System", font = "ar 32 bold", fg = "orange",bg = "white").grid(row = 0, column=3,padx = 8)

    fr.place(x = 330, y = 5)

    CollegeName = Label(root3, bg = "white",text = "Invigilator Status",fg = "Black",font=("Times New Roman",24))
    CollegeName.place(x = 510, y = 65)
    #---------------------------------------------Selected Entry is made invinsible----------------------------------------

    ai = Entry(root3,font = ("Times New Roman",14),border = 1,bg = "White")#326273
    ai.place(x = 1400, y = 620)
    ai1 = Entry(root3,font = ("Times New Roman",14),border = 1,bg = "White")#326273
    ai1.place(x = 1400, y = 620)

    Button(root3, text = "< - Left -",width=10,command = left).place(x = 315, y = 300)
    Button(root3, text = "- Right - >",width=10,command = right).place(x = 860, y = 300)
    
    Button(root3, text = "return",width=10,command = unavailable).place(x = 415, y = 300)
    Button(root3, text = "return",width=10,command = unavailable).place(x = 760, y = 300)

    #------------------------------------------------------Heading---------------------------------------------------------------
    Label(root3, text = "Morning Shift",fg = "white",font = ("Times New Roman",16),bg = "#326273").place(x = 105, y =  125)
    Label(root3, text = "Evening Shift",fg = "white",font = ("Times New Roman",16),bg = "#326273").place(x = 1020, y =  125)
    
    khoj = ttk.Combobox(root3,values = ["","BCA","PHY","CHM","ZOO","BOT","BTT","HIS","BCOM","SOC","POL","EDU","BSW","ENG"], width = 22)
    khoj.place(x = 504, y =  620)
    #Label(root3, text = "",fg = "white",font = ("Times New Roman",14),bg = "#326273").place(x = 504, y =  125)
    Button(root3, text = "Search",font = ("Times New Roman",8), width = 10, command = search_invigilator).place(x = 692, y = 620)

    table1()
    table2()
    table3()

    #select = Button(root3, text = "Select",font = ("Times New Roman",9), width = 30, command= select_invigilator)
    #select.place(x = 520, y = 650)

    Mknew = Button(root3, text = "New",width = 10, command = NewEntry)
    Mknew.place(x = 20, y = 650)

    swaps = Button(root3, text = "Swap",width = 10, command = swap)
    swaps.place(x = 100, y = 650)

    done = Button(root3, bd = 0, width = 10,bg = "white", text = "Done", fg = "Black", command= close_Report_Page)
    done.place(x = 1080, y = 650)

    
    cursor.execute("Select sum(t_No) from ehall")
    result = cursor.fetchone()[0]

    fanny = Label(root3, text = "Total Teacher Required: {}".format(result),bg = "#326273",font = ("Times New Roman",14))
    fanny.place(x = 510, y = 130)

    images = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = images.resize((100,100),Image.Resampling.LANCZOS)
    news = ImageTk.PhotoImage(resize)
    label = ttk.Label(root3,image=news).place(x = 60, y = 17)

    root3.mainloop()
