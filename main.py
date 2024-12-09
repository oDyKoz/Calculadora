import tkinter as tk
from tkinter import messagebox

# Função para realizar as operações matemáticas
def inserir_texto(valor):
    entrada.insert(tk.END, valor)

def limpar_entrada():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Entrada de texto
entrada = tk.Entry(janela, font=("Arial", 24), bd=5, insertwidth=4, width=14, justify="right")
entrada.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for (texto, linha, coluna, *span) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 18), bg="lightblue", command=calcular)
        botao.grid(row=linha, column=coluna, columnspan=span[0] if span else 1, sticky="nsew")
    elif texto == 'C':
        botao = tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 18), bg="lightcoral", command=limpar_entrada)
        botao.grid(row=linha, column=coluna)
    else:
        botao = tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 18), command=lambda t=texto: inserir_texto(t))
        botao.grid(row=linha, column=coluna)

# Configurar tamanhos das colunas e linhas para se ajustar
for i in range(5):
    janela.rowconfigure(i, weight=1)
    janela.columnconfigure(i, weight=1)

# Loop da interface gráfica
janela.mainloop()
