import mysql.connector
from tkinter import *

root = Tk()

con = mysql.connector.connect(host = "localhost", user = "root", passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()

cursor.execute ("Select count(*) from ehall")

result = cursor.fetchone()[0]

add = cursor.execute("Select sum(t_No) from ehall")
add = cursor.fetchone()

#int_result = int(result)
add = Label(root, text = add )#"Sum of the row: {0}".format(add)
add.pack()
#result = cursor.rowcount()
#print("Number of rows in the table is : ", result[0][0])
Label(root, text = "Numbers of rows: {}".format(result)).pack()
root.mainloop()