import tkinter as tk

class PackApp:
    def __init__(self, raiz):
        tamanhos = [(200,"red"), (100,"green"),
                    (50, "blue")]
        for tamanho, cor in tamanhos:
            frame = tk.Frame(
                raiz, width=tamanho, height=tamanho, bg=cor
            )
            frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

if __name__== "__main__":
    raiz = tk.Tk()
    PackApp(raiz)
    raiz.mainloop()