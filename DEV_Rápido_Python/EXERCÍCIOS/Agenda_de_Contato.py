class Contato:
    def __init__(self, nome="", sobrenome="", email="", telefone=""):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

class ControleContatos:
    def __init__(self):
        self.dicionario={}

    def adicionar(self):
        nome=input("Digite o nome Do contato a adicionar:")
        sobrenome=input("Digite seu sobrenome:")
        email=input("Digite seu email:")
        telefone=input("Digite seu telefone:")

        if self.dicionario.get(email):
             print("Esse contato ja existe")
        else:
            novo_contato = Contato(nome, sobrenome, email, telefone)

            self.dicionario[email]=novo_contato

        



    def buscar(self):
        achou=False
        print("Essa a lista de contatos: ")
        for emails,nomes in self.dicionario.items():
             print(nomes.nome)
        
        escolhido=input("Digite o nome do contato :").strip().lower()
        for emails,objeto_contato in self.dicionario.items():
             if escolhido == objeto_contato.nome.lower():
                  print(objeto_contato.nome,objeto_contato.telefone)
                  achou=True
        if achou == False:
            print(f"Nao foi possivel achar {escolhido}")

    def printar(self):
         for i,j in self.dicionario.items():
              print(f"Lista de contatos : ", j.nome, j.sobrenome ,j.telefone)

    def remover(self):
         achou=False
         chave_remover=""
         print("Lista de contatos para remover : ")
         for chave,contato in self.dicionario.items():
              print(contato.nome)
         retirar=input("Digite o nome do contato que deseja retirar:").strip().lower()
         for cara,excluido in self.dicionario.items():
              if retirar == excluido.nome.lower():
                   chave_remover=cara
                   achou=True
                   break
              
                 
         if achou ==False:
            print(f"Nao achamos {retirar} na lista de contatos")  

         if chave_remover != "":
            del self.dicionario[chave_remover]
            print(f"{retirar} retirado da lista de contatos com sucesso")
                      
        
             
        
        
             
        
if __name__ =="__main__":
    agenda=ControleContatos()
    while True:
            opcao = input("""
                  MENU CONTATOS
                1 - Ver Contatos
                2 - Adicionar Contato
                3 - Buscar Contato
                4 - Remover Contato
                5 - Sair
                
    
            Digite uma opção: """)
    
            match opcao:
            
                case "1":
                      agenda.printar()
                case "2":

                    agenda.adicionar()
                    for chave_email,objeto_contato in agenda.dicionario.items():
                            print(f"Chave {chave_email}")
                            print(f"Nome do contato guardado {objeto_contato.nome} {objeto_contato.sobrenome}")
                case "3":
                      agenda.buscar()
                case "4":
                      agenda.remover()
                case "5":
                      break
    
    
            input("\nPressione Enter para continuar...")
        
  


    
    
