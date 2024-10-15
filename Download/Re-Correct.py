import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
  host="localhost", 
  user="root", 
  passwd="2020Bca01", 
  database = "t_detail" 
) 

mycursor = mydb.cursor()
root = Tk()

# Create a label for the username
username_label = Label(root, text="Username")
username_label.grid(row=0, column=0)

# Create an entry for the username
username_entry = Entry(root)
username_entry.grid(row=0, column=1)

# Create a label for the password
password_label = Label(root, text="Password")
password_label.grid(row=1, column=0)

# Create an entry for the password
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Create a login button
login_button = Button(root, text="Login")
login_button.grid(row=2, column=1)
def check_credentials():
    # Get the username and password
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    mycursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
    result = mycursor.fetchone()
    mydb.commit()
    if result:
        # Login successful
        print("Success")
    else:
        # Login failed
        print("fail")
       
login_button.configure(command=check_credentials)
root.mainloop()