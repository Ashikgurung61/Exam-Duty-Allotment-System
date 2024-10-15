from tkinter import * 
from tkinter import ttk 
import mysql.connector  
from tkinter import messagebox 
from PIL import Image, ImageTk
from subprocess import call


con = mysql.connector.connect(host = 'localhost', user='root',passwd='2020Bca01',database='t_detail')
cursor = con.cursor()
def show():
    global tree, rows
    
   #---------------------------Connection --------------------------------------------
    cursor.execute("Select * from ehall")
    tree = ttk.Treeview(root0,column = (1,2,3), height = "15") 
    tree['show']='headings' 
    
    #Changing the heading style of a treeview 
    s= ttk.Style(root0)  
    s.theme_use("winnative")  
    
    #Define number of columns  
    tree['columns'] = ("id","hNo","t_No")

    #assign the width, minwidth 
    tree.column("hNo", width = 50, minwidth=50) 
    tree.column("id",width = 30, minwidth = 80)
    tree.column("hNo",width = 208, minwidth = 80)
    tree.column("t_No",width = 208, minwidth = 80)
                        
    #Assign the headingnames to the respective columns
    tree.heading("id", text = "ID")
    tree.heading("hNo", text = "Hall_No")
    tree.heading("t_No", text = "Total Invigilator")
                    
    rows = cursor.fetchall()
    #def update(rows):     
        #tree.delete(*tree.get_children())
    for j in rows:     
        tree.insert('', 'end',values = j)
    #update(rows)
    tree.place(x=758,y=60) 

def insert():
    global root0,tree, hall, entry2, right, examduty, E, D,A,S,SPACE,D,U,T,Y,design, btn,E
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
    examduty.place(x = 850, y = 5)

    E = Label(examduty,text="E",font = ("Times New Roman", 24),fg = "RED",bg = "#326273").grid(row = 0, column = 0)
    X = Label(examduty,text="X",font = ("Times New Roman", 24),fg = "Green",bg = "#326273").grid(row = 0, column = 1)
    A = Label(examduty,text="A",font = ("Times New Roman", 24),fg = "BLue",bg = "#326273").grid(row = 0, column = 2)
    M = Label(examduty,text="M",font = ("Times New Roman", 24),fg = "Black",bg = "#326273").grid(row = 0, column = 3)
    SPACE = Label(examduty,text=" ",font = ("Times New Roman", 24),fg = "Black",bg = "#326273").grid(row = 0, column = 4)
    D = Label(examduty,text="D",font = ("Times New Roman", 24),fg = "Black",bg = "#326273").grid(row = 0, column = 5)
    U = Label(examduty,text="U",font = ("Times New Roman", 24),fg = "red",bg = "#326273").grid(row = 0, column = 6)
    T = Label(examduty,text="T",font = ("Times New Roman", 24),fg = "Orange",bg = "#326273").grid(row = 0, column = 7)
    Y = Label(examduty,text="Y",font = ("Times New Roman", 24),bg = "#326273").grid(row = 0, column = 8)

    global design
    design = Frame(root0,bg="#326273")
    design.place(x = 835, y = 450)
    global label2
    label2 = Label(design,text = "Teacher required:",bg="#326273")
    label2.grid(row = 0, column = 1)
    global entry2
    entry2 = ttk.Combobox(design,values = ["","1","2","3","4"],width = 18)
    entry2.grid(row = 1, column = 1)

    #-----------------------------------------------Inserting Data to the database-----------------------------------------------
    global btn
    btn = Button(design,text = "Insert",border = 0, fg = "Blue", command = lambda:InsertData(tree))
    btn.grid(row = 2, column = 1,pady = 10, padx = 10)
    global idLad
    idLad = Label(design,text = "Enter Hall Number:",bg="#326273")
    idLad.grid(row = 0, column = 2,pady = 10, padx = 10)

    hall = Entry(design, border = 5)
    hall.grid(row = 1, column = 2,pady = 10, padx = 10)

    Delete = Button(design,text = "Delete",fg = "Blue",bd = 0, height = 1,command = delete1)
    Delete.grid(row=2, column=2,pady = 10, padx = 10)

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

    Next = Button(root0,text = "Done",fg = "Blue",bd = 5,bg = "PINK", width = 18, height = 1,command = info)
    Next.place(x = 920, y = 615)

    #--------------------------------------------------------Information------------------------------------------------------
        
    lab = LabelFrame(root0, text="NOTES",bd = 3,font=("Times New Roman",14), fg ="Red", background="White")
    lab.place(x = 30, y = 480, width = "560",height="135")

    note = Label(lab, text = " a. Enter the sequence correctly \n b. Provide the number of teacher invigilating \n c. Enter the numbers of hall-number for exam depending on the teacher required. \n For example: The number of teacher invigilating is 2, then enter the same hall number twice",font=("Times New Roman",11),justify="left", bg = "white")
    note.grid(row = 0, column = 0)

    Button(root0, text = "x",font = ("Times new roman",8),command=root0.destroy).place(x = 0, y = 0)
    line = Frame(root0,bd = 15,width= 450, bg = "WHite").place(x = 743, y = 600)

    show()

    

def info():
        global add, result, response
        cursor.execute("select count(*) from ehall")
        result = cursor.fetchone()[0]
        add = IntVar  
        add = cursor.execute("Select sum(t_No) from ehall")
        add = cursor.fetchone() 
        response = messagebox.askokcancel("Information","Required {} teacher's for invigilation".format(result) )
        if response == 1:
    #---------------------------------------------------Final Page--------------------------------------------------------------        
            root0.destroy()
            import FInal
        else:
            return True

def InsertData(tree):
    global hNo, t_No
    t_No = hall.get()
    hNo = entry2.get()
                
    if (hNo == "") or (t_No == ""):
        messagebox.showerror("Empty","Fill the blank spack!!")
    else:       
        try:    
            con.connect()
            value =  (hNo, t_No)
            query = "INSERT INTO ehall (t_No,hNo) VALUES (%s,%s) "
            cursor.execute(query,value)
            con.commit()
            show()
            #tree.insert("","end",text = "", values=(con.lastrowid,hNo, t_No))
            hNo.delete(0,END)   
            t_No.delete(0,END)  
            messagebox.showinfo("error")

        except Exception as e:
            print(e)           
        finally:
            con.close()
        


def delete1():
    selected_item=tree.selection()[0]
    data=tree.item(selected_item)["values"]
    id=data[0]

    try:
        sql="delete from ehall where id=%s"
        val=(id,)
        cursor.execute(sql,val)
        con.commit()
        root0.destroy()
    except:
        messagebox.showinfo("error","can't delete form")
    
    #-----------------------------------Right Side of the screen------------------------------------
   
    #-----------------------------------Widget-------------------------------------------
    
    

        #for widget in design.winfo_children():
            #widget.grid_configure(padx = 5, pady = 5)
                                                                            
    
#show() 
def update():
    cursor.execute("Select * from ehall")
    con.commit()
    cursor.fetchall()
    #--------------------------------------------------------Update---------------------------------------------

def update():
    query = "Update ehall set hNo= %s, t_No = %s where id = %s"
    cursor.execute(query)
    cursor.fetchall()
    con.commit()
    if (update):
        messagebox.showinfo("Success","Updated")
    else:
        messagebox.showinfo("Failed","Try Again")

#------------------------------Delete database for new entry of fields------------------------------------------

def deleteRoom():
    response = messagebox.askokcancel("Message","Are you sure?")
    if response == 1:
        addRoom = "DELETE FROM ehall where id is not null"
        cursor.execute(addRoom)
        con.commit()
        if(addRoom):
            messagebox.showinfo("Success","Deleted")
            show()
        else:
            messagebox.showinfo("Failed","Please try again")
    else:
        return True
    
    del_db = Button(root0,text="Remove all",bg = "Red",command=deleteRoom)
    del_db.place(x=950, y = 400)

    #---------------------------Next Button--------------------------

    #-----------------------------------------------------Logo--------------------------------------------------------------

    root0.mainloop()