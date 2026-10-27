import tkinter as tk

class PackApp:
    def __init__(self, raiz):
        area = tk.Frame(raiz,width=260, height=210)
        area.pack()
        a = tk.Label(area, text = "X: 0 / Y: 0", bg="red")
        b = tk.Label(area, text="X: 75 / Y: 75", bg= "lightblue")
        a.place(x=0, y=0)
        b.place(x=75, y=75)

if __name__== "__main__":
    raiz = tk.Tk()
    PackApp(raiz)
    raiz.mainloop()
