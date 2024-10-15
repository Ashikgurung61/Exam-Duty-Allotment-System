from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from Report_Page import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
import os
import time
import tkcalendar.dateentry

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()
def put():
    label1.configure(text=Exa.get())
    label4.configure(text=Etimes.get())
    label6.configure(text=shiftVs.get())
    label8.configure(text=showdate.get())
    label2.configure(text = showyear.get())

def finale():
    global root33, label1, label2,choice, label4, label4, label8, Etimes, Exa,shiftVs,showdate, showyear, label6,tree, data
    root33= Tk()
    root33.geometry("1250x680+30+15")
    root33.title("Duty Chart")
    root33.configure(bg = "#326273")
    root33.resizable(0,0)
    try:
        # windows only (remove the minimize/maximize button)
        root33.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')
    
    frame = Frame(root33, bd = 10, width = 1230, height= 120, bg = "White")
    frame.place(x = 10, y = 20)

    Headinglines = Frame (root33,  height = 121,width=3, background="violet")
    Headinglines.place(x = 500, y = 20)

    bodyline = Frame(root33, height = 600,width=3, background="Black")
    bodyline.place(x = 500, y = 140)


    data = Frame(root33,border = 3, background= "#326273")
    data.place( x = 33, y = 200)

    E = Label(root33,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 190, y = 30)
    D = Label(root33,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 285, y = 30)
    A = Label(root33,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 190, y = 80)
    S = Label(root33,text = "System", font = "ar 24 bold", fg = "orange").place(x = 350, y = 80)

    CollegeName = Label(root33, text = "Don Bosco College, Maram",font=("Times New Roman",26))
    CollegeName.place(x = 660, y = 35)

    subheading = Frame(root33, bg = "White")
    subheading.place(x = 720,  y = 95)

    label0 = Label(subheading,text = "Examination,",font=("Times New Roman",16))
    label0.grid(row = 0, column = 1,padx = 6)

    label1 = Label(subheading,text = "       ",font=("Times New Roman",16))
    label1.grid(row = 0, column = 0,padx = 6)

    label2 = Label(subheading,text = "Year",font=("Times New Roman",16))
    label2.grid(row = 0, column = 2, padx = 6)

    frame = Frame(root33, bd = 5, width = 800, height= 90, bg = "#326273")
    frame.place(x = 600, y = 150)

    label3 = Label(frame,text = "Duration:",font = ("Gabriola",14), bg = "#326273", fg = "Red")
    label3.grid(row = 0, column=0)

    label4 = Label(frame, text = "             ",font = ("Times New Roman",14), bg = "#326273")
    label4.grid(row = 0, column=1, padx= 20)

    label5 = Label(frame,text = "Shift:",font = ("Gabriola",14), fg = "Red",bg = "#326273")
    label5.grid(row = 0, column=2, padx = 20)

    label6 = Label(frame, text = "            ",font = ("Times New Roman",14), bg = "#326273")
    label6.grid(row = 0, column=3)

    label7 = Label(frame,text = "Date:",font = ("Gabriola",14), fg = "Red",bg = "#326273")
    label7.grid(row = 0, column=4, padx = 20)

    label8 = Label(frame, text = "             ",font = ("Times New Roman",14), bg = "#326273")
    label8.grid(row = 0, column=5)    

    shift = Label(data,text="Shift:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    shift.grid(row = 5, column = 0,padx = 10, pady = 10)
        
    time = Label(data,text ="Duration",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    time.grid(row = 4, column= 0, padx = 10, pady = 10)
        
    Etimes = ttk.Combobox(data,values = ["","1 hour","2 hour","3 hour"],width = 28)
    Etimes.grid(row = 4, column = 1, padx = 10, pady=10)

    shiftVs = ttk.Combobox(data,values = ["","M o r n i n g","E v e n i n g"],width = 28)
    shiftVs.grid(row = 5, column = 1, padx = 10, pady=10)

    choicelab = Label(data, text = "Confimr Shift",font = ("Times New Roman",14),fg = "White", bg = "#326273")
    choicelab.grid(row = 6, column = 0)

    choice = int()
    t = Radiobutton(data, text = "Morning",value = "0", variable = choice, bg = "#326273")
    t.grid(row = 6, column = 1, padx = 10, pady = 10)
    t1 = Radiobutton(data, text = "Evening",value = "1", variable= choice, bg = "#326273")
    t1.grid(row = 6, column = 2, padx = 10, pady = 10)
   
#------------------------------------------------Menu----------------------------------------------------------------

    back1 = Button(root33, bd = 0, width = 10,bg = "white", text = "Home", fg = "Black", command= root33.destroy)
    back1.place(x = 10, y = 141)
    
    def rep():
        report()

    check = Button(root33, bd = 0, width = 10,bg = "white", text = "Status", fg = "Black", command= rep)
    check.place(x = 88, y = 141)

#-----------------------------------------------is here--------------------------------------------------------------
    exam = Label(data,text = "Examination:", fg = "White", bg = "#326273",font = ("Times New Roman",14))
    exam.grid(row = 7, column = 0, padx = 10, pady = 10)
        
    Exa = Entry(data, border = 5,width = 30)
    Exa.grid( row = 7, column = 1, padx = 10, pady = 10)

    date = Label(data, text = "Date:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    date.grid(row = 8, column = 0, padx = 10, pady = 10)
        
    showdate = Entry(data, bd = 5,width = 30)
    showdate.grid(row = 8, column = 1, padx = 10, pady = 10)

    year = Label(data, text = "Year:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    year.grid(row = 9, column = 0, padx = 10, pady = 10)

    showyear = ttk.Combobox(data, values=["","2022","2023","2024","2025","2026"] ,width = 28)
    showyear.grid(row = 9, column = 1, padx = 10, pady = 10)

    generate = Button(root33, text = "Insert",bg = "pink", border = 3,width = 25, command = put)
    generate.place(x = 167, y = 485)

    def show():
        tree = ttk.Treeview(root33,column = (1,2,3), height = "18") 
        tree.place(x=650,y=200)
        tree['show']='headings' 
            
        #Changing the heading style of a treeview 
        s= ttk.Style(root33)  
        s.theme_use("winnative")  
            
        #Define number of columns  
        tree['columns'] = ("Hall","Teacher")

        #assign the width, minwidth 
        
        tree.column("Hall",width = 208, minwidth = 80)
        tree.column("Teacher",width = 208, minwidth = 80)
                                

        tree.heading("Hall", text = "Hall_No")
        tree.heading("Teacher", text = "Invigilator")

        sql1 = "Select hall,teacher from duty"
        cursor.execute(sql1)

        sol = cursor.fetchall()

        for rows in sol:
                tree.insert('', 'end', values=rows)

    def newidea():
        try:
            cursor.execute("delete from invigilator")
            cursor.execute("delete from duty")
            cursor.execute("update t_register set cnt=0 where id<10000")

            cursor.execute("select count(*) from ehall")
            result = cursor.fetchone()[0]
            if shiftVs.get()=="M o r n i n g":
                va=0
            else:
                va=1

            j=0
            while j<result:
            
                query="select t_name from t_register where cnt=0  and status=%s order by rand() limit 1"
                print(11)
                cursor.execute(query,(va,))
                print(22)
                for i in cursor:
                    myquery="select t_name from t_register where t_name=%s"
                    myvalue1=(i[0],)
                    cursor.execute(myquery,myvalue1)
                    print(33)
                    if cursor.fetchone():
                        cursor.execute(query,(va))
                        print(35)
                        for i in cursor:
                            query6="insert into invigilator(teacher) values(%s)"
                            value6=(i[0],)
                            cursor.execute(query6,value6)
                            print(44)
                            query7="update t_register set cnt=1 where t_name=%s"
                            cursor.execute(query7,value6)
                    else:
                        query1="insert into invigilator(teacher) values(%s)"
                        value1=(i[0],)
                        cursor.execute(query1,value1)
                        print(55)
                        query8="update t_register set cnt=1 where t_name=%s"
                        cursor.execute(query8,value1)
                    con.commit()
                j=j+1

            k=0
            while k<result:
                value3=(k,)
                query2="select hNo from ehall limit 1 offset %s"
                query3="select teacher from invigilator limit 1 offset %s"
                cursor.execute(query2,value3)
                for i in cursor:
                    hall=i[0]
                cursor.execute(query3,value3)
                for i in cursor:
                    teacher=i[0]

                query4="insert into duty(hall,teacher) values(%s,%s)"
                value4=(hall,teacher)
                cursor.execute(query4,value4)
                con.commit()
                k=k+1
            show()
        except:
            messagebox.showerror("error")





        #----------------------------------The Tree is here----------------------------------------
    
        

    def export_treeview_to_pdf():
        save_directory = ""
        save_directory = filedialog.askdirectory()
        try:
            print(0)
            if not save_directory:
                return

            # Create a PDF canvas
            pdf = canvas.Canvas(os.path.join(save_directory, f"Manual_T_Duty_.pdf"))
            print(1)
            # Set the font and font size for the heading
            pdf.setFont("Helvetica-Bold", 16)

            # Add a heading to the PDF
            pdf.drawString(200, 800, "Teacher's Exam Duty")
            pdf.setFont("Helvetica-Bold", 12)
            # Set the font and font size for the columns
            print(2)
            column_widths = {
                "#0": 0,
                "Hall" : 100,
                "Teacher" : 200
            }
            columns = tree["columns"]
            print(3)
            column_x = 150  # Adjust the starting x-coordinate value
            for column in columns:
                column_name = column
                column_width = column_widths.get(column_name, 100)  # Default width: 100
                pdf.drawString(column_x, 760, column_name)
                column_x += column_width

            data = []
            for item in tree.get_children():
                values = []
                for column in columns:
                    values.append(tree.item(item, "values")[columns.index(column)])
                data.append(values)
            pdf.setFont("Helvetica", 8)
            y = 730
            for row in data:
                x = 150  # Adjust the starting x-coordinate value
                for value in row:
                    pdf.drawString(x, y, value)
                    x += column_widths.get(columns[row.index(value)], 100)
                y -= 20

            # Save the PDF
            pdf.save()
            messagebox.showinfo("Success","Duty Saved")
        except:
            messagebox.showerror("ERROR")
    

        
    cont = Button(root33, text = "Continue",bg = "Green", border = 3,width = 25, command = newidea)
    cont.place(x = 167, y = 585)


    #######################################SELECTING THE FOLDER FOR PDF###########################################################


    #trees.place(x = 647, y = 200)

    new1 = ImageTk.PhotoImage(file = "Logo2.png")
    showima = ttk.Label(root33,image=new1)
    showima.place(x = 80, y = 30)

    root33.mainloop()
#-------------------------------Random Name---------------------------------------

def go():
    try:    
        global tree
        e1 = enter.get()
        e2 = choice.get()
        lancelot = e2
        query = "SELECT t_name FROM t_register where status = %s ORDER BY RAND() LIMIT "+e1
        cursor.execute(query,(lancelot,))
    # get the results
        results = cursor.fetchall()
        for row in results:
            tree.insert('', 'end', values=row)
    except: 
        print("error")

#------------------------------------------------------------------------------------------------------------------
finale()
##########
def put():
    label1.configure(text=Exa.get())
    #label4.configure(text=Etimes.get())
    label6.configure(text=shiftVs.get())
    label2.configure(text = showyear.get())


def finale():
    global root33, label1, label2, label4, label4, label8, Etimes, Exa,shiftVs,showdate, showyear, label6,tree, data
    root33= Tk()
    root33.geometry("1250x680+30+15")
    root33.title("Duty Chart")
    root33.configure(bg = "#326273")
    root33.resizable(0,0)
    try:
        # windows only (remove the minimize/maximize button)
        root33.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')
    
    frame = Frame(root33, bd = 10, width = 1230, height= 120, bg = "White")
    frame.place(x = 10, y = 20)

    Headinglines = Frame (root33,  height = 121,width=3, background="violet")
    Headinglines.place(x = 500, y = 20)

    bodyline = Frame(root33, height = 600,width=3, background="Black")
    bodyline.place(x = 500, y = 140)


    data = Frame(root33,border = 3, background= "#326273")
    data.place( x = 33, y = 200)

    E = Label(root33,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 190, y = 30)
    D = Label(root33,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 285, y = 30)
    A = Label(root33,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 190, y = 80)
    S = Label(root33,text = "System", font = "ar 24 bold", fg = "orange").place(x = 350, y = 80)

    CollegeName = Label(root33, text = "Don Bosco College, Maram",font=("Times New Roman",26))
    CollegeName.place(x = 660, y = 35)

    subheading = Frame(root33, bg = "White")
    subheading.place(x = 720,  y = 95)

    label0 = Label(subheading,text = "Examination,",font=("Times New Roman",16))
    label0.grid(row = 0, column = 1,padx = 6)

    label1 = Label(subheading,text = "       ",font=("Times New Roman",16))
    label1.grid(row = 0, column = 0,padx = 6)

    label2 = Label(subheading,text = "Year",font=("Times New Roman",16))
    label2.grid(row = 0, column = 2, padx = 6)

    shift12 = Label(data,text="Shift:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    shift12.place(x = 750, y = 150)

    label6 = Label(data,text="Shift:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    label6.place(x = 920, y = 150)

    shift = Label(data,text="Shift:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    shift.grid(row = 5, column = 0,padx = 10, pady = 10)
        
    time = Label(data,text ="Duration",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    time.grid(row = 4, column= 0, padx = 10, pady = 10)
        
    Etimes = ttk.Combobox(data,values = ["","1 hour","2 hour","3 hour"],width = 28)
    Etimes.grid(row = 4, column = 1, padx = 10, pady=10)

    shiftVs = ttk.Combobox(data,values = ["","M o r n i n g","E v e n i n g"],width = 28)
    shiftVs.grid(row = 5, column = 1, padx = 10, pady=10)
    
    date = Label(data, text = "Date:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    date.grid(row = 6, column = 0, padx = 10, pady = 10)
    
    showdate = Entry(data, bd = 5,width = 30)
    showdate.grid(row = 6, column = 1, padx = 10, pady = 10)

#------------------------------------------------Menu----------------------------------------------------------------

    back1 = Button(root33, bd = 0, width = 10,bg = "white", text = "Home", fg = "Black", command= root33.destroy)
    back1.place(x = 10, y = 141)
    
    def rep():
        report()

    check = Button(root33, bd = 0, width = 10,bg = "white", text = "Status", fg = "Black", command= rep)
    check.place(x = 88, y = 141)

#-----------------------------------------------is here--------------------------------------------------------------
    exam = Label(data,text = "Examination:", fg = "White", bg = "#326273",font = ("Times New Roman",14))
    exam.grid(row = 7, column = 0, padx = 10, pady = 10)
        
    Exa = ttk.Combobox(data,values = ["","Weekly","CIA-I","CIA-II","CIA-III","Semester"],width = 28)
    Exa.grid( row = 7, column = 1, padx = 10, pady = 10)

    year = Label(data, text = "Year:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    year.grid(row = 9, column = 0, padx = 10, pady = 10)

    showyear = ttk.Combobox(data, values=["","2022","2023","2024","2025","2026"] ,width = 28)
    showyear.grid(row = 9, column = 1, padx = 10, pady = 10)

    generate = Button(root33, text = "Insert",bg = "pink", border = 3,width = 25, command = put)
    generate.place(x = 167, y = 450)