import tkinter as tk 
from tkinter import messagebox

def __init__(self,raiz):
        self.raiz = raiz
        raiz.title("Menu de aplicação")
        raiz.geometry("360x220")
        barra = tk.Menu(raiz)
        arquivo = tk.Menu(barra, tearoff = False)
        arquivo.add_command(label="Novo",command=self.novo)
        arquivo.add_separator()
        arquivo.add_command(label="Sair",command=raiz.destroy)
        barra.add_cascade(label="Arquivo",menu=arquivo)
        ajuda = tk.Menu(barra, tearoff=False)
        ajuda.add_command(label="Sobre", command=self.sobre)
        barra.add_cascade(label="Ajuda", menu=ajuda)
        raiz.config(menu=barra)

def novo(self):
        messagebox.showinfo("Novo", "Novo cadastro")

    def sobre(self):
        janela_sobre = tk. Toplevel(self.raiz)
        janela_sobre.title("Sobre")
        tk.Label(janela_sobre,
                 text="Aplicação didática de RAD").pack(
                     padx=20, pady=20
                    )

if __name__ == "__main__":
    raiz = tk.Tk()
    MenuApp(raiz)
    raiz.mainloop()
