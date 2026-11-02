import tkinter as tk
from tkinter import ttk, messagebox

class Cadastro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cadastro de Clientes")
        self.janela.geometry("400x300")

        ttk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_nome = ttk.Entry(janela,width=20)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(janela, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_email = ttk.Entry(janela,width=20)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)


        ttk.Label(janela, text="Telefone:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_telefone = ttk.Entry(janela,width=20)
        self.entry_telefone.grid(row=2, column=1, padx=10, pady=10)

        self.btn_cadastrar = ttk.Button(janela, text="Cadastrar", command=self.cadastrar)
        self.btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=20)

        self.lisbox_clientes = tk.Listbox(janela, width=50, height=10)
        self.lisbox_clientes.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def cadastrar(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()

        if not nome or not email or not telefone:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
            return

        if "@" not in email or "." not in email:
            messagebox.showwarning("Aviso", "Email inválido!")
            return

        if not telefone.isdigit():
            messagebox.showwarning("Aviso", "Telefone deve conter apenas números!")
            return

        self.lisbox_clientes.insert(tk.END, f"{nome} | {email} | {telefone}")
        self.limpar_formulario()

    def limpar_formulario(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_nome.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = Cadastro(root)
    root.mainloop()
