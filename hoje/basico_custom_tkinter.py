import customtkinter as ctk

def click():
    print("Botão clicado!")


janela = ctk.CTk()
janela.title("Exemplo de CustomTkinter")
janela.geometry("400x200")


botao = ctk.CTkButton(janela, text="Clique aqui", command=click)
botao.pack()


janela.mainloop()