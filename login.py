from tkinter import *
import tkinter.messagebox as message_box
import sqlite3
import main as main_window
from functools import partial


def login():
    username = username_entry.get()
    password = password_entry.get()

    with sqlite3.connect("Authenticate.db") as db:
        cursor = db.cursor()

    find_user = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(find_user, [username, password])
    results = cursor.fetchall()

    if results:
        login_window.destroy()
        main_window.controller_window()
    else:
        message_box.showinfo("Error", "Invalid Login")


# login window
login_window = Tk()
login_window.geometry('400x300')
login_window.title('Login - Rover Controller')

username_label = Label(login_window, text='Username', font=('bold', 14))
username_label.place(x=20, y=30)

password_label = Label(login_window, text='Password', font=('bold', 14))
password_label.place(x=20, y=60)

username_entry = Entry()
username_entry.place(x=150, y=30)

password_entry = Entry(login_window, show='*')
password_entry.place(x=150, y=60)

login_button = Button(login_window, text="Login", font=('bold', 14), command=login)
login_button.place(x=200, y=100)

login_window.mainloop()
