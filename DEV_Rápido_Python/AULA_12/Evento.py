import tkinter as tk 
from tkinter as tk

class EventoApp:
    def __init__(self,raiz):
       raiz.title("Evento")
       self.label= tk.Label(raiz, text ="olá, Tkinter!")
       self.label.pack(pady=10)
       botao = tk.Button(raiz,text="clique aqui",
                          command=self.clicado)
       botao.pack(pady=10)

    def clicado(self):
        self.label.config(text = "Botão clicado!")

if __name__ == "__main__":
    raiz = tk.Tk()
    EventoApp(raiz)
    raiz.mainloop()
