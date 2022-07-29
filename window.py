from tkinter import *

class main:
        def __init__(self):
            window = Tk()

            window.title("System")
            text = Label(window, text="Hello World")
            text.grid(column=0, row=0, padx=190, pady=70)

            button = Button(window, text="Register")
            button.grid(column=0, row=1, padx=10, pady=10)

            window.mainloop()

main()