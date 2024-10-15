from tkinter import * 
from tkinter import ttk
import mysql.connector
root = Tk()

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01", database = "t_detail")
cursor = con.cursor()

tree = ttk.Treeview(root, columns = (1,2,3),show = "headings", height = "21")
s= ttk.Style(root)  
s.theme_use("winnative")
sql = "Select id,t_name from t_register where status = 0"
cursor.execute(sql)
result = cursor.fetchall()
tree['columns'] = ("Id","Invigilator Name","Seriel_No")

tree.heading("Id", text = "Id")
tree.heading("Invigilator Name", text = "Invigilator Name")
tree.heading("Seriel_No", text = "Sl_No")


#assign the width, minwidth 

tree.column("Id", width = 50, minwidth=50,anchor='center') 
tree.column("Invigilator Name",width = 200, minwidth = 80,anchor='center')
tree.column("Seriel_No", width = 50, minwidth=50,anchor='center') 

#tree.insert('',"0","Sl.No")
for row in result:
    tree.insert('',"end",values=row)
    
   
tree.place(x = 50, y = 165)
tree = ttk.Treeview(root)
tree.insert(" ",'0',text = "0")
tree.insert(" ",'1',text = "1")
tree.insert(" ",'2',"subitem2",text = "2")

tree.pack()
root.mainloop()
