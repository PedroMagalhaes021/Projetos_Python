from pathlib import Path
from tkinter import Tk


janela = Tk ()
janela.title("Nos ❤️ Python 🐍")
icone = Path(__file__).with_name("icon.ico")

if icone.exists():
    janela.iconbitmap(str(icone))

janela.geometry("600x250")
janela.eval('tk::PlaceWindow . center')
janela.mainloop()
