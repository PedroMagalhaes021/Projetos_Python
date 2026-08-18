# Calculadora Iniciante  
print("Calculadora Amadora")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

# Operações 
operacao = input("Escolha a operação (+, -, *, /): ")

# Inicializando a variável
resultado = None

# Escolhendo a operação
if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    if b != 0:
        resultado = a / b
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")

# Exibindo o resultado
if resultado is not None:
    print("O resultado é:", resultado)
