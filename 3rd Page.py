from tkinter import * 
from tkinter import ttk 
import mysql.connector  
from tkinter import messagebox 
from PIL import Image, ImageTk
#from FInal import *



con = mysql.connector.connect(host = 'localhost', user='root',passwd='2020Bca01',database='t_detail')
cursor = con.cursor()

def show():
    global tree, rows
    
   #---------------------------Connection --------------------------------------------
    cursor.execute("Select * from ehall")
    tree = ttk.Treeview(root0,column = (1,2,3), height = "18") 
    tree['show']='headings' 
    
    #Changing the heading style of a treeview 
    s= ttk.Style(root0)  
    s.theme_use("winnative")  
    
    #Define number of columns  
    tree['columns'] = ("id","hNo","t_No")

    #assign the width, minwidth 
    #tree.column("hNo", width = 50, minwidth=50) 
    tree.column("id",width = 30, minwidth = 80)
    tree.column("hNo",width = 208, minwidth = 80)
    tree.column("t_No",width = 208, minwidth = 80)
                        
    #Assign the headingnames to the respective columns
    tree.heading("id", text = "ID")
    tree.heading("hNo", text = "Hall_No")
    tree.heading("t_No", text = "Total Invigilator")
                    
    rows = cursor.fetchall()
    for j in rows:     
        tree.insert('', 'end',values = j)
    #update(rows) 
    tree.place(x=715,y=20)
    tree.bind("<<TreeviewSelect>>",select)

def select(e):
    selection=tree.focus()
    data=tree.item(selection,"values")
    hall.delete(0,END)
    hall.insert(0,data[0])

def DeleteRow():
    try:
        e1 = hall.get()
        delete1 = "Delete from ehall where id = "+e1
        cursor.execute(delete1)
        con.commit()
        show()
    except:
        print("Error")
    
def insert():
    global root0,tree, hall, entry2, right, examduty, E, D,A,S,SPACE,D,U,T,Y,design, btn
    root0 = Tk()
    root0.title("Hall Detail")
    root0.geometry("1250x650+30+15")
    root0.configure(bg = "#326273")
    try:
        # windows only (remove the minimize/maximize button)
        root0.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')
    
    root0.resizable(0,0)
    examduty = Frame(root0, bd = 5, bg="#326273")
    examduty.place(x = 850, y = 0)

    #underline = Frame(root0, bd = 1,width = 25,bg = "Black").place(x = 850, y = 25)
#-----------------------------------------------Inserting Data to the database-----------------------------------------------

    global design
    design = Frame(root0,bg="#326273")
    design.place(x = 750, y = 460)
    global label2
    label2 = Label(design,text = "Teacher required:",fg= "White",font = ("Times new roman",15),bg="#326273")
    label2.grid(row = 0, column = 0)
    global entry2
    entry2 = ttk.Combobox(design,values = ["","1","2","3","4"],width = 18 ,font = ("Times new roman",12))
    entry2.grid(row = 0, column = 1)
    
    global idLad
    idLad = Label(design,text = "Enter Hall Number:",fg = "white",bg="#326273",font = ("Times new roman",14))
    idLad.grid(row = 1, column = 0,pady = 10, padx = 10)

    hall = Entry(design, border = 5,font = ("Times new roman",12))
    hall.grid(row = 1, column = 1,pady = 10, padx = 10)

#---------------------------------------------Buttons-----------------------------------------------------------------
    btn = Button(root0,text = "INSERT",overrelief=SUNKEN,border = 2,width = 12, fg = "Black", command = lambda:InsertData(tree))
    btn.place(x = 980, y = 559)
   
#---------------------------------------------Buttons-----------------------------------------------------------------

    right = Canvas(root0,bd = 5, bg = "White",height = 650,width = 620 )
    right.place(x = 0, y = 0)

    E = Label(right,text="Exam",fg = "Navy BLue", font="ar 24 bold")
    E.place(x = 210, y = 100)
    D = Label(right,text = "Duty", font = "ar 24 bold", fg = "RED")
    D.place(x = 315, y = 100)
    A = Label(right,text = "Allotment", font = "ar 24 bold", fg = "green")
    A.place(x = 165, y = 150)
    S = Label(right,text = "System", font = "ar 24 bold", fg = "orange")
    S.place(x = 335, y = 150)

    Next = Button(root0,text = "Done",overrelief=SUNKEN, bd = 0, width = 10,bg = "white", fg ="Black",command = info)
    Next.place(x = 871, y = 408)

    #--------------------------------------------------------Information------------------------------------------------------
        
    lab = LabelFrame(root0, text="NOTES",bd = 3,font=("Times New Roman",14), fg ="Red", background="White")
    lab.place(x = 30, y = 480, width = "560",height="135")

    note = Label(lab, text = " a. Enter the exam-hall in numeric form only eg: 88 \n b. Provide the number of teacher invigilating \n c. To delete the row from a table insert the row id in the exam hall number textbox ",font=("Times New Roman",11),justify="left", bg = "white")
    note.grid(row = 0, column = 0)

    back = Button(root0, bd = 0,overrelief=SUNKEN, width = 10,bg = "#326273", text = "Home", fg = "White", command= root0.destroy).place(x = 0, y = 0)
    line = Frame(root0,bd = 15,width= 450, bg = "WHite").place(x = 743, y = 600)

    
    def edit():
        global save, Delete, del_db
        btn10.destroy()

        Delete = Button(root0,text = "delete",overrelief=SUNKEN,fg = "Black",bd = 0,width = 10,command = DeleteRow)
        Delete.place(x = 750, y = 408)

        del_db = Button(root0,text="New Page",overrelief=SUNKEN,bg = "white",command=deleteRoom)
        del_db.place(x=1000, y = 408)

    btn10 = Button(root0, bd = 0,overrelief=SUNKEN, width = 10, text = "Edit", fg = "Black", command = edit)
    btn10.place(x = 950, y = 408)
    show()

    """haine = PhotoImage(file = "Logo1.png")
    chair = Label(root0,image=haine)
    chair.place(x = 208, y = 230)"""
    img=PhotoImage(file='Logo1.png')
    Lab=Label(root0,image=img)
    Lab.place(x=0,y=0)
def info():
        #global result
        #try:
            #cursor.execute("select count(*) from ehall")
            #result = cursor.fetchone()[0]
            #response = messagebox.askokcancel("Information","Required {} teacher's for invigilation".format(result) )
            #if response == 1:
#---------------------------------------------------Final Page--------------------------------------------------------------        
        root0.destroy()
        finale()
            #else:
                #return True
        #except:
            #messagebox.showinfo("Error","There is a problem, console the domain for help")

def InsertData(tree):
    global hNo, t_No, value
    hNo = hall.get()
    t_No = entry2.get()
                
    if (hNo == "") or (t_No == ""):
        messagebox.showerror("Empty","Fill the blank spack!!")
    else:       
        try:    
            con.connect()
            value =  (t_No, hNo)
            query = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
            if int(t_No) == 2:
                query1 = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
                cursor.execute(query1,value)
            elif int(t_No) == 3:
                query2 = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
                query3 = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
                cursor.execute(query2,value)
                cursor.execute(query3,value)
            elif int(t_No) == 4:
                query4 = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
                query5 = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
                query6 = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
                cursor.execute(query4,value)
                cursor.execute(query5,value)
                cursor.execute(query6,value)

            cursor.execute(query,value)
            con.commit()
            show()
        except Exception as e:
            print(e)           
        finally:
            con.close()
    
#------------------------------Delete database for new entry of fields------------------------------------------

def deleteRoom():
    try:
        addRoom = "DELETE FROM ehall where id is not null"
        cursor.execute(addRoom)
        con.commit()
        show()
        insert()
        if(addRoom):
            
            insert()
            
        else:
            messagebox.showinfo("Failed","Please try again")
    except:
        return True
    #-----------------------------------------------------Logo--------------------------------------------------------------
    root0.mainloop()
insert()