import tkinter as tk
from datetime import datetime

class RelogioApp:
    def __init__(self,raiz):
        self.raiz = raiz
        self.relogio = tk.Label(raiz, font = ("consolas",32))
        self.relogio.pack(padx=20, pady=20)
        self.atualizar()

    def atualizar(self):
        agora = datetime.now().strftime("%H:%M:%S")
        self.relogio.config(text=agora)
        self.raiz.after(1000, self.atualizar)

if __name__ == "__main__":
    raiz = tk.Tk()
    RelogioApp(raiz)
    raiz.mainloop()
