#execept = Se der erro 
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
