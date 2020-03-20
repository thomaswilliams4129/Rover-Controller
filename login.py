from tkinter import *
import pyrebase
from getpass import getpass
from functools import partial

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyC0qEbhXcE7SQpQrku8vC__DtBNP3baV7w",
    "authDomain": "nasa-rover-d8ec5.firebaseapp.com",
    "databaseURL": "https://nasa-rover-d8ec5.firebaseio.com",
    "projectId": "nasa-rover-d8ec5",
    "storageBucket": "nasa-rover-d8ec5.appspot.com",
    "messagingSenderId": "669236128960",
    "appId": "1:669236128960:web:491a189289c2fbd7499125",
    "measurementId": "G-GK1CNYZ649"
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("Please Enter Your Email Address : \n")
password = getpass("Please Enter Your Password : \n")

user = auth.create_user_with_email_and_password(email, password)
print("Success .....")


# def validateLogin(username, password):
# 	print("username entered :", username.get())
# 	print("password entered :", password.get())
# 	return


# #window
# tkWindow = Tk()  
# tkWindow.geometry('400x150')  
# tkWindow.title('Login - Rover Controller')

# #username label and text entry box
# usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
# username = StringVar()
# usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# #password label and password entry box
# passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

# validateLogin = partial(validateLogin, username, password)

# #login button
# loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

# tkWindow.mainloop()