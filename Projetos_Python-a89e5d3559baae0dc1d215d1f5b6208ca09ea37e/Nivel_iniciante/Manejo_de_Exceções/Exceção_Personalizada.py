#“Se algo der errado, eu mesmo vou criar o erro e avisar”
def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
      #O raise cria o erro manualmente
        raise Exception("Descrição do erro")

try:
    funcao()
  #'e' guarda o erro 
except Exception as e:
  #{str(e)} mostra a mensagem
    print(f"Erro: {str(e)}")
