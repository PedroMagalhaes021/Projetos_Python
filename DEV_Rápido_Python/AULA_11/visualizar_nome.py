import tkinter as tk
from tkinter import messagebox


def mostrar_nome():
    nome = entrada.get().strip()
    if nome:
        messagebox.showinfo("Cadastro", f"Olá, {nome}!")
    else:
        messagebox.showwarning("Atenção", "Informe seu nome: ")

janela = tk.Tk()
tk.Label(janela, text="Nome: ", width=40).pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(padx=100)
tk.Button(janela, text="Enviar", command=mostrar_nome).pack(pady=10)
janela.mainloop()
