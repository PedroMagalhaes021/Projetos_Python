from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#conectando a um banco sqlite em memoria
engine=create_engine('sqlite:///:memory:',echo=True)

#criacao da base declarativa
Base=declarative_base()

#definicao da classe modelo usuario
class Usuario(Base):
    __tablename__='usuarios'

    id=Column(Integer,primary_key=True)
    nome=Column(String)
    idade=Column(Integer)


    def __repr__(self):
        return f"Usuario(id={self.id},nome={self.nome},idade={self.idade})"
#criacao da tabela no banco de dados
Base.metadata.create_all(engine)
#criacao da sessao
Session=sessionmaker(bind=engine)
session=Session()

#inserção de dados
usuario1=Usuario(nome='Kaua',idade=20)
usuario2=Usuario(nome='Gulherme',idade=90)
session.add(usuario1)
session.add(usuario2)
#commit das alterações
session.commit()

#consulta de dados
usuarios=session.query(Usuario).all()
for usuario in usuarios:
    print(usuario)
