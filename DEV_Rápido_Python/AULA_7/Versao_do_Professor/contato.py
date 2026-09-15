import re

class Contato:
    def __init__(
        self,
        nome: str,
        sobrenome: str,
        email: str,
        telefone: str
    ):
        self.nome = self._normalizar_nome(nome, "nome")
        self.sobrenome = self._normalizar_nome(sobrenome, "sobrenome")
        self.email = self._normalizar_email(email)
        self.telefone = self._normalizar_telefone(telefone)

    @staticmethod
    def _normalizar_nome(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise TypeError(f"{campo.capitalize()} deve ser uma string.")

        # Remove espaços no início/fim e espaços duplicados
        valor = " ".join(valor.strip().split())

        if not valor:
            raise ValueError(f"{campo.capitalize()} não pode ficar vazio.")

        # Como usaremos ; como separador no TXT
        if ";" in valor:
            raise ValueError(
                f"{campo.capitalize()} não pode conter ';'."
            )

        return valor.title()

    @staticmethod
    def _normalizar_email(email: str) -> str:
        if not isinstance(email, str):
            raise TypeError("E-mail deve ser uma string.")

        email = email.strip().lower()

        if not email:
            raise ValueError("E-mail não pode ficar vazio.")

        padrao = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not re.fullmatch(padrao, email):
            raise ValueError("E-mail inválido.")

        return email

    @staticmethod
    def _normalizar_telefone(telefone: str) -> str:
        if not isinstance(telefone, str):
            raise TypeError("Telefone deve ser uma string.")

        # Mantém apenas números
        telefone = re.sub(r"\D", "", telefone)

        if len(telefone) not in (10, 11):
            raise ValueError(
                "Telefone deve possuir 10 ou 11 dígitos."
            )

        return telefone

    @property
    def nome_completo(self) -> str:
        return f"{self.nome} {self.sobrenome}"

    @property
    def telefone_formatado(self) -> str:
        if len(self.telefone) == 11:
            return (
                f"({self.telefone[:2]}) "
                f"{self.telefone[2:7]}-"
                f"{self.telefone[7:]}"
            )

        return (
            f"({self.telefone[:2]}) "
            f"{self.telefone[2:6]}-"
            f"{self.telefone[6:]}"
        )

    def para_dicionario(self) -> dict:
        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "telefone": self.telefone,
        }

    @classmethod
    def de_dicionario(cls, dados: dict):
        return cls(
            dados["nome"],
            dados["sobrenome"],
            dados["email"],
            dados["telefone"],
        )

    def __str__(self) -> str:
        return (
            f"{self.nome_completo} | "
            f"{self.email} | "
            f"{self.telefone_formatado}"
        )
