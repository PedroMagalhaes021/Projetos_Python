import sqlite3
from pathlib import Path
from typing import Any,ClassVar

from logger_config import logger
from marca import Marca
from pessoa import Pessoa
from veiculo import Veiculo

class BancoDeDados:
    CAMPOS_PESSOA_PERMITIDOS:ClassVar[frozenset[str]]=frozenset(
        {"nome","nascimento","oculos"}
    )

    def __init__(self,nome_banco:str="banco.sqlite")-> None:
        self.caminho_banco=Path(__file__).resolve().parent / nome_banco
        self.conn:sqlite3.Connection | None=None

    def conectar(self)->None:
        try:
            self.conn=sqlite3.Connection(self.caminho_banco)
            self.conn.row_factory=sqlite3.Row


            self.conn.execute("PRAGMA foreign_keys=ON")
            logger.info("Conexão com banco realizada com sucesso")
        except sqlite3.Error:
            logger.exception("Erro ao conectar ao banco de dados")
            raise
    def _obter_conexao(self)->sqlite3.Connection:
        if self.conn is None:
            raise RuntimeError(
                "Banco de dados nao encontrado"
                "Execute conectar() antes de realizar operacoes"
            )
        return self.conn
    def criar_tabelas(self)->None:
        conn=self._obter_conexao()

        try:
            with conn:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Pessoa(
                    cpf TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    nascimento TEXT NOT NULL,
                    oculos INTEGER NOT NULL
                            CHECK(oculos IN(0,1))
                    )
                    """
                )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Marca(
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    sigla TEXT NOT NULL 
                    )
                    """
                )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Veiculo(
                    placa TEXT PRIMARY KEY,
                    cor TEXT NOT NULL,
                    cpf_proprietario TEXT NOT NULL,
                    id_marca INTEGER NOT NULL,
                    
                    FOREIGN KEY(cpf_proprietario)
                    REFERENCES Pessoa(cpf)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                    
                    FOREIGN KEY(id_marca)
                    REFERENCES Marca(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT
                    )"""
            
                )
            logger.info("Tabelas criadas com sucesso")
        except sqlite3.IntegrityError:
            logger.exception("Erro de integridade durante a criacao da tabelas")
            raise
        except sqlite3.OperationalError:
            logger.exception("Erro geral do sqlite durante a criacao da tabelas")
            raise
        except sqlite3.DatabaseError:
            logger.exception("Erro de banco durante a criacao das tabelas")
            raise
        except sqlite3.Error:
            logger.exception("Erro geral do sqlite durante a criacao das tabelas")
            raise
            
