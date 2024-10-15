#from date import *
from tkinter import *
from tkinter import filedialog


root = Tk()
def open_file():
    file = filedialog.askopenfilename()
    if file:
        txtar.delete('1.0',END)
        fh = open(file,'r')
        read = fh.read()
        txtar.insert(END, read)
        fh.close()

def save_open():
    global open_root, txtar
    open_root = Tk()
    open_root.title("Login")
    open_root.geometry("1250x650+30+15")
    open_root.configure(bg = "#326273")
    
try:
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform')

    press = Button(open_root,text = "Open",command=open_file).pack()
    txtar = Text(open_root)
    txtar.pack()
    open_root.mainloop()
presshwew = Button(root,text = "Open",command=save_open).pack()
root.mainloop()