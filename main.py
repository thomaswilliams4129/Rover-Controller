from tkinter import *
import functions as functionsClass
mainWindow = Tk() 

# Window Design
mainWindow.title('Rover Controller') 
mainWindow.geometry('1500x800') # Size 200, 200
# mainWindow.iconbitmap('nasa.ico')

button_frame = Frame(mainWindow)

# Define Buttons
forwardButton = Button(mainWindow, text='Forward', width=25, command = lambda: functionsClass.printButtonPress('Forward'))
backwardButton = Button(mainWindow, text='Backward', width=25, command = lambda: functionsClass.printButtonPress('Backward')) 
leftButton = Button(button_frame, text='Left', width=25, command = lambda: functionsClass.printButtonPress('Left'))  
rightButton = Button(button_frame, text='Right', width=25, command = lambda: functionsClass.printButtonPress('Right'))

# Layout
backwardButton.pack(side=BOTTOM, fill=BOTH)
button_frame.pack(fill=X, side=BOTTOM)
forwardButton.pack(side=BOTTOM,fill=BOTH)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

leftButton.grid(row=1, column=0, sticky=W+E)
rightButton.grid(row=1, column=1, sticky=W+E)

mainWindow.bind('w', lambda event: functionsClass.printButtonPress('Forward'))
mainWindow.bind('s', lambda event: functionsClass.printButtonPress('Backward'))
mainWindow.bind('a', lambda event: functionsClass.printButtonPress('Left'))
mainWindow.bind('d', lambda event: functionsClass.printButtonPress('Right'))

mainWindow.mainloop() 
