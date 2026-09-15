from pathlib import Path
import shutil
import tkinter as tk
from tkinter import messagebox


pasta_origem = Path(r"C:\Users\dev\Downloads")

regras = {
    Path(r"C:\\Users\\dev\\Pictures"): [".png", ".jpg", ".jpeg", ".gif"],
    Path(r"C:\\Users\\dev\\Downloads\\Executaveis"): [".exe", ".msi"],
    Path(r"C:\\Users\\dev\\Documents\\documentos"): [".pdf", ".docx", ".txt",".py",".cpp",".c"]
}

def organizar():
    try:
        if not pasta_origem.exists():
            messagebox.showerror("Erro", "A pasta de origem não foi encontrada.")
            return

        
        arquivos_na_pasta = []
        for f in pasta_origem.iterdir():
             if f.is_file():
                  arquivos_na_pasta.append(f)
        print(arquivos_na_pasta)
        if not arquivos_na_pasta:
            messagebox.showwarning("Erro", "A pasta de Origem está vazia.")
            return
        arquivos_movidos = 0
        for arquivo in arquivos_na_pasta:
                extensao = arquivo.suffix.lower()
            
          
                for pasta_destino, extensoes in regras.items():
                    if extensao in extensoes:
                    
                  
                        pasta_destino.mkdir(parents=True, exist_ok=True)
                        shutil.move(arquivo, pasta_destino / arquivo.name)
                        arquivos_movidos+=1
                        break
                       
        if arquivos_movidos > 0 :
            messagebox.showinfo("Sucesso", "A operação foi concluída com êxito!")
        else:
            messagebox.showwarning("Aviso", "Existem arquivos na pasta, mas nenhum corresponde às regras de extensão.")
                     
    except Exception as e:
         messagebox.showerror("Erro", f"Ocorreu um problema: {e}")



janela = tk.Tk()
janela.title("Organizador Python")
janela.geometry("400x300")


rotulo = tk.Label(janela, text="Olá! Clique abaixo para organizar seus arquivos.")
rotulo.pack(pady=20)  

botao = tk.Button(janela, text="Organizar", command=organizar, width=15, height=2)
botao.pack(pady=10)

janela.mainloop()
