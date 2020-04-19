from tkinter import *
import functions as functionsClass


def controller_window():
    main_window = Tk()

    # Window Design
    main_window.title('Rover Controller')
    main_window.geometry('1500x800')  # Size 200, 200
    # mainWindow.iconbitmap('nasa.ico')

    button_frame = Frame(main_window)

    # Define Buttons
    forward_button = Button(main_window, text='Forward', width=25,
                            command=lambda: functionsClass.printButtonPress('Forward'))
    backward_button = Button(main_window, text='Backward', width=25,
                             command=lambda: functionsClass.printButtonPress('Backward'))
    left_button = Button(button_frame, text='Left', width=25,
                         command=lambda: functionsClass.printButtonPress('Left'))
    right_button = Button(button_frame, text='Right', width=25,
                          command=lambda: functionsClass.printButtonPress('Right'))

    # Layout
    backward_button.pack(side=BOTTOM, fill=BOTH)
    button_frame.pack(fill=X, side=BOTTOM)
    forward_button.pack(side=BOTTOM, fill=BOTH)

    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    left_button.grid(row=1, column=0, sticky=W + E)
    right_button.grid(row=1, column=1, sticky=W + E)

    main_window.bind('<Up>', lambda event: functionsClass.printButtonPress('Forward'))
    main_window.bind('<Down>', lambda event: functionsClass.printButtonPress('Backward'))
    main_window.bind('<Left>', lambda event: functionsClass.printButtonPress('Left'))
    main_window.bind('<Right>', lambda event: functionsClass.printButtonPress('Right'))
    main_window.bind('w', lambda event: functionsClass.printButtonPress('Forward'))
    main_window.bind('s', lambda event: functionsClass.printButtonPress('Backward'))
    main_window.bind('a', lambda event: functionsClass.printButtonPress('Left'))
    main_window.bind('d', lambda event: functionsClass.printButtonPress('Right'))

    main_window.mainloop()
