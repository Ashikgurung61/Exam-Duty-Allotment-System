from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from com import *

root = Tk()
root.title("Routine")
root.geometry("1250x650+20+15")
root.configure(bg = "#326273")

try:
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform') 
#----------------------------------------Widget-----------------------------------
#-------------------------------Heading---------------------------------------------

heading = Label(root,text = "E x a m - D e t a i l", font = ('Times New Roman',30), bg = "#326273")
heading.place(x = 800, y = 120)
#------------------------------Enter data----------------------------------------------
#def hr():
    
data = Frame(root,border = 3, background= "#326273")
data.place( x = 765, y = 340)
    
shift = Label(data,text="Shift:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
shift.grid(row = 5, column = 0,padx = 10, pady = 10)
    
time = Label(data,text ="Duration",fg = "White", bg = "#326273",font = ("Times New Roman",14))
time.grid(row = 4, column= 0, padx = 10, pady = 10)
     
Etimes = ttk.Combobox(data,values = ["","1 hour","2 hour","3 hour"],width = 28)
Etimes.grid(row = 4, column = 1, padx = 10, pady=10)

shiftVs = ttk.Combobox(data,values = ["","M o r n i n g","E v e n i n g"],width = 28)
shiftVs.grid(row = 5, column = 1, padx = 10, pady=10)
     
exam = Label(data,text = "Examination:", fg = "White", bg = "#326273",font = ("Times New Roman",14))
exam.grid(row = 6, column = 0, padx = 10, pady = 10)
    
Exa = Entry(data, border = 3,width = 30)
Exa.grid( row = 6, column = 1, padx = 10, pady = 10)
     
date = Label(data, text = "Date:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
date.grid(row = 7, column = 0, padx = 10, pady = 10)
     
showdate = Entry(data, bd = 3,width = 30)
showdate.grid(row = 7, column = 1, padx = 10, pady = 10)
      
#-----------------------------Right side of the frame-------------------------
     
right = Frame(root,bd = 2, bg = "white",height = 650,width = 600 )
right.place(x = 0, y = 0)

E = Label(root,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 210, y = 100)
D = Label(root,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 315, y = 100)
A = Label(root,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 165, y = 150)
S = Label(root,text = "System", font = "ar 24 bold", fg = "orange").place(x = 335, y = 150)

#-----------------------------Put Picture---------------------------------------
     
image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
resize = image.resize((200,200),Image.LANCZOS)
new = ImageTk.PhotoImage(resize)
label = ttk.Label(root,image=new)
label.place(x = 190, y = 250)
        
#-----------------------------------Another one--------------------------------------   
line = Frame(root,bd = 15,width= 400, bg = "WHite").place(x = 743, y = 310)

def back():
    root.destroy()
    import Home_page

back = Button(root, bd = 3, width = 10,bg = "Black", text = "Back", fg = "White", command= "back").place(x = 0, y = 0)

line = Frame(root,bd = 15,width= 400, bg = "WHite").place(x = 743, y = 570)

def next():
    if (Exa == "") or (showdate == "") or (shiftVs == "") or (Etimes == ""):
        messagebox.showerror("Empty","Please Enter username and password!!") 
    else:
        root.destroy()
        #Invigi
        #import Insert

generate = Button(root, text = "Generate",bg = "pink", border = 3,width = 15, command = Invigi)
generate.place(x = 900, y = 600)

#------------------------Another picture--------------------------------

images = Image.open("C:\\Users\\user\\py\\Examples\\invi.png")
resize = images.resize((80,80),Image.LANCZOS)
news = ImageTk.PhotoImage(resize)
label1 = ttk.Label(root,image=news)
label1.place(x = 920, y = 30)
       
root.mainloop()