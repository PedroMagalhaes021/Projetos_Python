import os
from sqlalchemy import create_engine,select
from sqlalchemy.orm import sessionmaker,DeclarativeBase,Mapped,mapped_column


DIRETORIO_ATUAL=os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO=os.path.join(DIRETORIO_ATUAL,'banco_dados.db')
engine=create_engine(f'sqlite:///{CAMINHO_BANCO}',echo=True)


#criaca da tabela declarativa atualizada
class Base(DeclarativeBase):
    pass


#definicao da classe modelo utilizando Type Hints atuais(Mapped e mapped_column)
class Usuario(Base):
    __tablename__='usuarios'


    id:Mapped[int]=mapped_column(primary_key=True)
    nome:Mapped[str]=mapped_column()
    idade:Mapped[int]=mapped_column()



    def __repr__(self):
        return f"Usuario(id={self.id},nome={self.nome},idade={self.idade})"

#criacao da tabela banco
Base.metadata.create_all(engine)
#criacao do gestor de sessoes
Session=sessionmaker(bind=engine)

#utilizacao do bloco 'with' (context manager) para garantir o fecho seguro da ligacao
with Session() as session:
    usuario1=Usuario(nome='kaua',idade=20)
    usuario2=Usuario(nome='fodase',idade=90)
    session.add_all([usuario1,usuario2])
    #efetivar alteracoes
    session.commit()
    #Consulta de banco com sintaxe atual(select em vez de query)
    stmt=select(Usuario)
    usuarios=session.scalars(stmt).all()


    for usuario in usuarios:
        print(usuario)
