import tkinter as tk

def click():
    print("Botão clicado!")


janela = tk.Tk()
janela.title("Exemplo de Tkinter")
janela.geometry("400x200")


botao = tk.Button(janela, text="Clique aqui", command=click)
botao.pack()


janela.mainloop()