from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
con = mysql.connector.connect(host = "localhost",user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()
sql = "Select t_name, status from t_register where status = 1"
cursor.execute(sql)
result = cursor.fetchall()
#print(result)
tree = ttk.Treeview(root,column = (1,2), height = "15")
tree.heading(0,text = "Status")
for row in result:
        tree.insert('',"end",values=row)
#if result == 0:
    #my = "Select t_name from t_reg"
    #cursor.execute(my)
    #show = cursor.fetchall()
    #for row in show:
        #tree.insert('',"end",values=row)



   # if row[0] == "Available":
       # my = "Select t_name from t_reg"
        #cursor.execute(my)
       # tis = cursor.fetchall()
        #print(tis)
   # elif row[0] == "Un-Available":
       # mys = "Select t_name from t_reg"
        #cursor.execute(mys)
        #tish = cursor.fetchall()
        #for j in tis:
        #print(tish)
    #else:
        #print("Wrong")
 

#tree['show']='headings' 
#tree.heading("t_name", text = "Status")
tree.pack()
root.mainloop()