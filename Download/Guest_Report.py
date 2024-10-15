from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
from reportlab.pdfgen import canvas
import os
import time

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()
def export_treeview_to_pdf():
        save_directory = ""
        save_directory = filedialog.askdirectory()
        try:
            print(0)
            if not save_directory:
                return

            # Create a PDF canvas
            pdf = canvas.Canvas(os.path.join(save_directory, f"Manual_T_Duty_.pdf"))
           
            # Set the font and font size for the heading
            pdf.setFont("Helvetica-Bold", 14)

            # Add a heading to the PDF
            pdf.drawString(200, 800, "Don Bosco College, Maram ")
                       
            pdf.setFont("Helvetica", 11)
            # Set the font and font size for the columns
            
            column_widths = {
                "#0": 0,
                "Hall" : 100,
                "Teacher" : 200
            }
            columns = tree["columns"]
            
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
            messagebox.showinfo("Success","Duty Saved Successfully")
        except:
            messagebox.showerror("ERROR")

def shows():
        global tree
        tree = ttk.Treeview(root2ss,column = (1,2,3), height = "21") 
        tree.place(x=450,y=170)
        tree['show']='headings' 
            
        #Changing the heading style of a treeview 
        s= ttk.Style(root2ss)  
        s.theme_use("winnative")  
            
        #Define number of columns  
        tree['columns'] = ("Hall Number","Invigilator Names")

        #assign the width, minwidth 
        
        tree.column("Hall Number",width = 208, minwidth = 80,anchor='center')
        tree.column("Invigilator Names",width = 208, minwidth = 80)
                                

        tree.heading("Hall Number", text = "Hall_No")
        tree.heading("Invigilator Names", text = "Invigilator")

        sql1 = "Select hall,teacher from duty"
        cursor.execute(sql1)

        sol = cursor.fetchall() 
        #tree.insert('','end',values="")
        for rows in sol:
                tree.insert('', 'end', values=rows)

def Reports1():
    global root2ss, here
    root2ss= Tk()
    root2ss.geometry("1250x650+30+15")
    root2ss.title("Report page")
    root2ss.configure(bg = "#326273")
    root2ss.resizable(0,0)

    try:
        # windows only (remove the minimize/maximize button)
        root2ss.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')


    frame = Frame(root2ss, bd = 10, width = 1200, height= 120, bg = "White")
    frame.place(x = 25, y = 20)

    fr = Frame(root2ss,bg = "white")

    E = Label(fr,text="Exam",fg = "Navy BLue", font="ar 32 bold",bg = "white").grid(row = 0, column=0,padx = 8)
    D = Label(fr,text = "Duty", font = "ar 32 bold", fg = "RED",bg = "white").grid(row = 0, column=1,padx = 8)
    A = Label(fr,text = "Allotment", font = "ar 32 bold", fg = "green",bg = "white").grid(row = 0, column=2,padx = 8)
    S = Label(fr,text = "System", font = "ar 32 bold", fg = "orange",bg = "white").grid(row = 0, column=3,padx = 8)

    fr.place(x = 330, y = 20)

    CollegeName = Label(root2ss, bg = "white",text = "Invigilator Duty Report",fg = "Black",font=("Times New Roman",24))
    CollegeName.place(x = 500, y = 79)

    
    #-------------------------------Heading------------------------------------
    def goback():
        from FInal import finale
        finale()
    #here = Label(root2s, text = "Unavailable Teacher",fg = "white",font = ("Times New Roman",16),bg = "#326273").place(x = 325, y =  165)
    #Label(root2s, text = "Available Teacher",fg = "white",font = ("Times New Roman",16),bg = "#326273").place(x = 780, y =  165)
    def takeout():
        btn10.destroy()
        btn2 = Button(root2ss, text = "Save",font = ("Times new roman",12),fg = "White",bd = 0,bg = "#326273", command=export_treeview_to_pdf,underline = 5)
        btn2.place(x = 105, y = 140)

        def notes():
            btn3.destroy()
            note = LabelFrame(root2ss, text = "Step to save:",border=1, height= 100, width= 100)
            note.place(x = 20, y = 450)

            info = Label(note, text = "a. Click the file button on the left corner \n b. Click the save button again \n c. Save the file in date formate \n d. CLose the Exam Duty Allotment System application \n e. Open the file which you save earlier in MS-Words \n f. Enter detail about the exam (Duration, Date, Shift) and save \n g. Finally, the report is ready for printing. ",font=("Times New Roman",11),justify="left")
            info.pack()

        btn3 = Button(root2ss, text = "Help",font = ("Times new roman",12),fg = "White",bd = 0,bg = "#326273", command=notes,underline = 5)
        btn3.place(x = 190, y = 140)

    btn10 = Button(root2ss, text = "File",font = ("Times new roman",12),fg = "Black",bd = 0,bg = "#326273", command=takeout,underline = 5)
    btn10.place(x = 25, y = 140)
    
    Label(root2ss, text = "Guest", font = ("Times new roman",10), bg = "White", fg = "RED").place(x = 1170, y = 110)

    shows()

    images = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = images.resize((100,100),Image.Resampling.LANCZOS)
    news = ImageTk.PhotoImage(resize)
    label = ttk.Label(root2ss,image=news).place(x = 80, y = 30)

    root2ss.mainloop()
