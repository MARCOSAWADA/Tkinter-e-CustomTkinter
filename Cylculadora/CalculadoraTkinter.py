import tkinter as tk
from tkinter import messagebox


def botao_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)


def botao_clear():
    entry.delete(0, tk.END)


def botao_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        messagebox.showinfo("Resultado", f"O resultado é: {result}")

    except Exception as erro:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERRRRRRROOO")
        messagebox.showerror("Erro", "Erro na expressão!")


calc = tk.Tk()
calc.title("Calculadora Simples")


entry = tk.Entry(calc, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4)


botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, col) in botoes:
    if text == '=':
        btn = tk.Button(calc, text=text, width=5, height=2, font=('Arial', 20), command=botao_equal)
    elif text == 'C':
        btn = tk.Button(calc, text=text, width=5, height=2, font=('Arial', 20), command=botao_clear)
    else:
        btn = tk.Button(calc, text=text, width=5, height=2, font=('Arial', 20), command=lambda value=text: botao_click(value))
    
    btn.grid(row=row, column=col, padx=5, pady=5)


calc.mainloop()