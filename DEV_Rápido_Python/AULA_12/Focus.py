import tkinter as tk

class FocoApp:
    def __init__(self, raiz):
        self.texto_padrao = "Digite seu nome aqui!"
        self.entrada = tk.Entry(raiz, fg="gray", width=30)
        self.entrada.insert(0, self.texto_padrao)
        self.entrada.pack(pady=20)
        self.entrada.bind("<FocusIn>", self.limpar)
        self.entrada.bind("<FocusOut>", self.restaurar)
      
if __name__ == "__main__":
    raiz = tk.Tk()
    FocoApp(raiz)
    raiz.mainloop()
