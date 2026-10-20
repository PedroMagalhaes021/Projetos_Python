import tkinter as tk


def constroi_label(texto: str = "Padrão"):
    ola = tk.Label(
        text= texto,
        foreground="red",
        background="black",
        width=40,
        height=20)
    botao = tk.Button(
            text="botão",
            width=25,
            height=5,
            bg="blue",
            fg="yellow")
    ola.pack()
    botao.pack()

if __name__ == "__main__":
    janela = tk.Tk()
    constroi_label("QUEM SABE PYTHON É VIADO!!!")
    janela.mainloop()
