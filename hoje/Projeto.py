import tkinter as tk

janela = tk.Tk()
janela.title("Projeto Demonstrativo - Tkinter e Custom Tkinter")
janela.geometry("800x600")

capa = tk.PhotoImage(file="hoje/image/tela.png")
imagem1 = tk.PhotoImage(file="hoje/image/tkinter.png") 
imagem2 = tk.PhotoImage(file="hoje/image/custom_tkinter.png") 

logo = capa.subsample(3,3)
logo1 = imagem1.subsample(2,2)
logo2 = imagem2.subsample(2,2)


exibir_imagem = tk.Label(janela, image=logo)
exibir_imagem.pack(pady=10)



texto1 = tk.Label(janela, text="")
texto1.pack(pady=10)

texto2 = tk.Label(janela, text="CALCULADORA")
texto2.pack(pady=10)


janela.estado_imagem = 1 


def mudar_imagem():
    if janela.estado_imagem == 1:
        exibir_imagem.config(image=logo1)  
        texto1.config(text="Tkinter")  
        botao_trocar.config(text="Trocar para Custom Tkinter")  
        janela.estado_imagem = 2 
    else:
        exibir_imagem.config(image=logo2)  
        texto1.config(text="Custom Tkinter")  
        botao_trocar.config(text="Trocar para Tkinter")  
        janela.estado_imagem = 1


botao_trocar = tk.Button(janela, text="MOSTRAR", command=mudar_imagem)
botao_trocar.pack(pady=5)

janela.mainloop()
