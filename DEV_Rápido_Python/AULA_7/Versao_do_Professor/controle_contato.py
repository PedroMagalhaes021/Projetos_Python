import json
from pathlib import Path

from contato import Contato


class ControleContatos:
    def __init__(self):
        self._contatos: list[Contato] = []

    @property
    def contatos(self) -> tuple[Contato, ...]:
        """
        Retorna uma cópia imutável da coleção.
        Evita alteração direta da lista interna.
        """
        return tuple(self._contatos)

    def adicionar(self, contato: Contato) -> None:
        if not isinstance(contato, Contato):
            raise TypeError(
                "Somente objetos da classe Contato podem ser adicionados."
            )

        if self._email_existe(contato.email):
            raise ValueError(
                f"Já existe um contato com o e-mail {contato.email}."
            )

        self._contatos.append(contato)

    def buscar(self, termo: str) -> list[Contato]:
        termo = " ".join(termo.strip().split()).casefold()

        if not termo:
            return []

        encontrados = []

        for contato in self._contatos:
            if (
                termo in contato.nome_completo.casefold()
                or termo in contato.email.casefold()
                or termo in contato.telefone
            ):
                encontrados.append(contato)

        return encontrados

    def remover(self, email: str) -> Contato:
        email = email.strip().lower()

        for indice, contato in enumerate(self._contatos):
            if contato.email == email:
                return self._contatos.pop(indice)

        raise LookupError(
            f"Contato com e-mail '{email}' não encontrado."
        )

    def listar(self) -> list[Contato]:
        return sorted(
            self._contatos,
            key=lambda contato: contato.nome_completo.casefold()
        )

    def _email_existe(self, email: str) -> bool:
        return any(
            contato.email == email
            for contato in self._contatos
        )

    def salvar_json(self, arquivo: str = "contatos.json") -> None:
        caminho = Path(arquivo)

        dados = [
            contato.para_dicionario()
            for contato in self._contatos
        ]

        with caminho.open(
            "w",
            encoding="utf-8"
        ) as arquivo_json:
            json.dump(
                dados,
                arquivo_json,
                ensure_ascii=False,
                indent=4
            )

    def carregar_json(
        self,
        arquivo: str = "contatos.json"
    ) -> list[str]:

        caminho = Path(arquivo)

        with caminho.open(
            "r",
            encoding="utf-8"
        ) as arquivo_json:
            dados = json.load(arquivo_json)

        if not isinstance(dados, list):
            raise ValueError(
                "O arquivo JSON deve conter uma lista de contatos."
            )

        novos_contatos = []
        emails = set()
        erros = []

        for numero, item in enumerate(dados, start=1):

            try:
                if not isinstance(item, dict):
                    raise TypeError(
                        "Registro deve ser um objeto JSON."
                    )

                contato = Contato.de_dicionario(item)

                if contato.email in emails:
                    raise ValueError(
                        f"E-mail duplicado: {contato.email}"
                    )

                novos_contatos.append(contato)
                emails.add(contato.email)

            except (
                KeyError,
                TypeError,
                ValueError
            ) as erro:
                erros.append(
                    f"Registro {numero}: {erro}"
                )

        self._contatos = novos_contatos

        return erros

    def salvar_txt(
        self,
        arquivo: str = "contatos.txt"
    ) -> None:

        caminho = Path(arquivo)

        with caminho.open(
            "w",
            encoding="utf-8"
        ) as arquivo_txt:

            arquivo_txt.write(
                "nome;sobrenome;email;telefone\n"
            )

            for contato in self._contatos:
                linha = (
                    f"{contato.nome};"
                    f"{contato.sobrenome};"
                    f"{contato.email};"
                    f"{contato.telefone}\n"
                )

                arquivo_txt.write(linha)

    def carregar_txt(
        self,
        arquivo: str = "contatos.txt"
    ) -> list[str]:

        caminho = Path(arquivo)

        novos_contatos = []
        emails = set()
        erros = []

        with caminho.open(
            "r",
            encoding="utf-8"
        ) as arquivo_txt:

            for numero_linha, linha in enumerate(
                arquivo_txt,
                start=1
            ):

                linha = linha.strip()

                # Ignora linhas vazias
                if not linha:
                    continue

                # Ignora cabeçalho
                if numero_linha == 1 and linha.casefold() == (
                    "nome;sobrenome;email;telefone"
                ):
                    continue

                partes = [
                    parte.strip()
                    for parte in linha.split(";")
                ]

                if len(partes) != 4:
                    erros.append(
                        f"Linha {numero_linha}: "
                        "quantidade incorreta de campos."
                    )
                    continue

                try:
                    nome, sobrenome, email, telefone = partes

                    contato = Contato(
                        nome,
                        sobrenome,
                        email,
                        telefone
                    )

                    if contato.email in emails:
                        raise ValueError(
                            f"E-mail duplicado: {contato.email}"
                        )

                    novos_contatos.append(contato)
                    emails.add(contato.email)

                except (
                    TypeError,
                    ValueError
                ) as erro:
                    erros.append(
                        f"Linha {numero_linha}: {erro}"
                    )

        self._contatos = novos_contatos

        return erros
