from tkinter import *

class main:
        def __init__(self):
            window = Tk()

            window.title("System")
            texto = Label(window, text="Hello World")
            texto.grid(column=0, row=0, padx=190, pady=100)

            botao = Button(window, text="Register")
            botao.grid(column=0, row=1, padx=10, pady=10)

            texto_resposta = Label(window, text="")
            texto_resposta.grid(column=0, row=2, padx=10, pady=10)


            window.mainloop()

main()