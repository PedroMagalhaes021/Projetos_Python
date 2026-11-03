"""Interface desktop orientada a objetos com Tkinter, ttk e SQLite."""

import sqlite3
import tkinter as tk
from collections.abc import Callable
from pathlib import Path
from tkinter import messagebox, ttk

from database import Database


class CadastroApp(ttk.Frame):
    """Tela principal: exibe o Treeview e coordena as ações CRUD."""
    def __init__(self, master: tk.Tk, db: Database) -> None:
        super().__init__(master, padding=20)
        self.db = db
        self.pack(fill="both", expand=True)
        master.title("Cadastro de usuários | Tkinter + SQLite")
        master.geometry("850x490")
        master.minsize(700, 350)

        ttk.Label(self, text="Cadastro de usuários", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(self, text="Selecione um registro para editar ou excluir.").pack(anchor="w", pady=(2, 14))

        botoes = ttk.Frame(self)
        botoes.pack(fill="x", pady=(0, 12))
        ttk.Button(botoes, text="Novo", command=self.novo).pack(side="left", padx=(0, 8))
        ttk.Button(botoes, text="Editar", command=self.editar).pack(side="left", padx=(0, 8))
        ttk.Button(botoes, text="Excluir", command=self.excluir).pack(side="left", padx=(0, 8))
        ttk.Button(botoes, text="Atualizar", command=self.atualizar_tabela).pack(side="left")

        area = ttk.Frame(self)
        area.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(
            area, columns=("id", "nome", "email"),
            show="headings", selectmode="browse"
        )
        for coluna, titulo, largura in (
            ("id", "ID", 60), ("nome", "Nome", 240), ("email", "E-mail", 390)
        ):
            self.tree.heading(coluna, text=titulo)
            self.tree.column(coluna, width=largura, anchor="w")
        self.tree.column("id", stretch=False)
        self.tree.pack(side="left", fill="both", expand=True)
        barra = ttk.Scrollbar(area, orient="vertical", command=self.tree.yview)
        barra.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=barra.set)
        self.atualizar_tabela()

    def atualizar_tabela(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)
        for usuario_id, nome, email in self.db.listar():
            self.tree.insert("", "end", iid=str(usuario_id), values=(usuario_id, nome, email))

    def selecionado(self) -> tuple[int, str, str] | None:
        itens = self.tree.selection()
        if not itens:
            messagebox.showwarning("Seleção", "Selecione um usuário primeiro.", parent=self)
            return None
        valores = self.tree.item(itens[0], "values")
        return int(valores[0]), str(valores[1]), str(valores[2])

    def novo(self) -> None:
        def salvar(nome: str, email: str) -> None:
            self.db.inserir(nome, email)
            self.atualizar_tabela()
        FormularioUsuario(self, "Novo usuário", salvar)

    def editar(self) -> None:
        usuario = self.selecionado()
        if usuario is None:
            return
        usuario_id, nome_atual, email_atual = usuario

        def salvar(nome: str, email: str) -> None:
            self.db.atualizar(usuario_id, nome, email)
            self.atualizar_tabela()
        FormularioUsuario(self, "Editar usuário", salvar, (nome_atual, email_atual))

    def excluir(self) -> None:
        usuario = self.selecionado()
        if usuario is None:
            return
        usuario_id, nome, _ = usuario
        confirmar = messagebox.askyesno(
            "Confirmar exclusão", f"Excluir o usuário {nome}?", parent=self
        )
        if confirmar:
            try:
                self.db.excluir(usuario_id)
            except sqlite3.Error as erro:
                messagebox.showerror("Erro de banco", str(erro), parent=self)
                return
            self.atualizar_tabela()


class FormularioUsuario(tk.Toplevel):
    """Janela para criar ou editar um usuário."""
    def __init__(
        self,
        master: tk.Misc,
        titulo: str,
        ao_salvar: Callable[[str, str], None],
        dados: tuple[str, str] = ("", ""),
    ) -> None:
        super().__init__(master)
        self.title(titulo)
        self.resizable(False, False)
        self.ao_salvar = ao_salvar

        quadro = ttk.Frame(self, padding=20)
        quadro.grid(row=0, column=0)
        ttk.Label(quadro, text="Nome:").grid(row=0, column=0, sticky="w", pady=6)
        self.nome = ttk.Entry(quadro, width=34)
        self.nome.grid(row=0, column=1, pady=6, padx=(12, 0))
        ttk.Label(quadro, text="E-mail:").grid(row=1, column=0, sticky="w", pady=6)
        self.email = ttk.Entry(quadro, width=34)
        self.email.grid(row=1, column=1, pady=6, padx=(12, 0))

        self.nome.insert(0, dados[0])
        self.email.insert(0, dados[1])
        botoes = ttk.Frame(quadro)
        botoes.grid(row=2, column=0, columnspan=2, pady=(15, 0))
        ttk.Button(botoes, text="Salvar", command=self.salvar).pack(side="left", padx=6)
        ttk.Button(botoes, text="Cancelar", command=self.destroy).pack(side="left", padx=6)

        self.transient(master)
        self.grab_set()
        self.nome.focus_set()

    def salvar(self) -> None:
        nome = self.nome.get().strip()
        email = self.email.get().strip()
        if not nome or not email:
            messagebox.showwarning("Campos obrigatórios", "Informe nome e e-mail.", parent=self)
            return
        try:
            self.ao_salvar(nome, email)
        except sqlite3.IntegrityError:
            messagebox.showerror("E-mail duplicado", "Este e-mail já está cadastrado.", parent=self)
            return
        except sqlite3.Error as erro:
            messagebox.showerror("Erro de banco", str(erro), parent=self)
            return
        self.destroy()
        

def main() -> None:
    banco = Database(Path(__file__).with_name("usuarios.db"))
    try:
        janela = tk.Tk()
        estilo = ttk.Style(janela)
        estilo.configure("Treeview", rowheight=28)
        CadastroApp(janela, banco)
        janela.mainloop()
    finally:
        banco.fechar()


if __name__ == "__main__":
    main()