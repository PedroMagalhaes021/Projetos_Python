# Calculadora Intermediária

import math

while True:
    print("\n== CALCULADORA INTERMEDIÁRIA ==")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Sair")

    op = input("Escolha uma operação de 1 a 7: ")

    if op == '7':
        print("Encerrando...")
        break

    elif op in ['1', '2', '3', '4', '5']:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if op == '1':
            print("Resultado:", a + b)

        elif op == '2':
            print("Resultado:", a - b)

        elif op == '3':
            print("Resultado:", a * b)

        elif op == '4':
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Erro: divisão por zero")

        elif op == '5':
            print("Resultado:", a ** b)

    elif op == '6':
        a = float(input("Digite o número: "))
        if a >= 0:
            print("Resultado:", math.sqrt(a))
        else:
            print("Erro: número negativo")

    else:
        print("Opção inválida! Escolha de 1 a 7.")
