"""Execute com: python -m unittest discover -s tests -v"""

import sqlite3
import tempfile
import unittest
from pathlib import Path

from database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.pasta = tempfile.TemporaryDirectory()
        self.banco = Database(Path(self.pasta.name) / "teste.db")

    def tearDown(self) -> None:
        self.banco.fechar()
        self.pasta.cleanup()

    def test_criar_e_listar(self) -> None:
        self.banco.inserir("Ana", "ana@example.com")
        usuarios = self.banco.listar()
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0][1:], ("Ana", "ana@example.com"))

    def test_atualizar(self) -> None:
        self.banco.inserir("Ana", "ana@example.com")
        usuario_id = self.banco.listar()[0][0]
        self.banco.atualizar(usuario_id, "Ana Maria", "maria@example.com")
        self.assertEqual(self.banco.listar()[0][1:], ("Ana Maria", "maria@example.com"))

    def test_excluir(self) -> None:
        self.banco.inserir("Ana", "ana@example.com")
        usuario_id = self.banco.listar()[0][0]
        self.banco.excluir(usuario_id)
        self.assertEqual(self.banco.listar(), [])

    def test_email_unico(self) -> None:
        self.banco.inserir("Ana", "ana@example.com")
        with self.assertRaises(sqlite3.IntegrityError):
            self.banco.inserir("Bia", "ana@example.com")
        self.assertEqual(len(self.banco.listar()), 1)


if __name__ == "__main__":
    unittest.main()
