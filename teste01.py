from tkinter import *

def buttonConfirm():
    txt05 = Label(janela, text="Login foi um sucesso")
    txt05.grid(column=0, row=4)



janela = Tk()
janela.title("Escolinha Isaac")

txt01 = Label(janela, text="Bem-vindo ao Login da Escolinha !!")
txt01.grid(column=0, row=0)

txt02 = Label(janela, text="Nome: ")
txt02.grid(column=0, row=1)

txt03 = Label(janela, text="Idade: " )
txt03.grid(column=0, row=2)

txt04 = Button(janela, text="Confirmar", command=buttonConfirm)
txt04.grid(column=0, row=3)


janela.mainloop()
