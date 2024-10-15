from tkinter import * 
import mysql.connector

root = Tk()
root.geometry("400x150") 


con = mysql.connector.connect(host = "LocalHost",user = "root", passwd ="2020Bca01",database = "t_detail")

q="SELECT t_name FROM t_register WHERE status=False ORDER BY RANDOM() LIMIT 0,1"


b1=Button(root,text='Show',command=lambda:my_display(),bg='lightgreen',width=18)
b1.grid(row=0,column=0,padx=5,pady=10,columnspan=2,sticky='w')

b2= Button(root,text='Reset',command=lambda:my_reset(),bg='lightyellow',width=18)
b2.grid(row=0,column=2,padx=5,pady=10,sticky='w')

def my_display(): # to show random record
    my_cursor=root.execute(q)
    data_row=my_cursor.fetchone()
    [w.grid_forget() for w in root.grid_slaves(2)] # remove all previous data
    if data_row: # Once the data is collected ( not None )
        con.execute('UPDATE t_register set status=1 WHERE id='+ str(data_row[0]))
        #print(data_row)
        i=0 # to increment column value         
        for student in data_row: 
            my_label=Label(root,text=str(student),font=20)
            my_label.grid(row=2,column=i,padx=5,pady=5)
            i=i+1 # Next column number 
    else: # No record is available to show 
        my_label=Label(root,text='No more record',font=20)
        my_label.grid(row=2,column=0,columnspan=4,padx=5,pady=5)
def my_reset():
    con.execute('UPDATE t_register set status=0' ) # for all records update status
    [w.grid_forget() for w in root.grid_slaves(2)] # remove all previous data
    my_label=Label(root,text='Records Resetted',font=20)
    my_label.grid(row=2,column=0,columnspan=4,padx=5,pady=5)
root.mainloop()