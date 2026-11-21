import sympy as sp
#variável simbólica 
x = sp.symbols("x")
print("=" * 50)
print(" CALCULADORA DE DERIVADAS ")
print("=" * 50)
#Grau da Função
grau = int(input("\nDigite o grau do polinômio: "))

#Montagem da função
funcao = 0

print("\nDigite os coeficientes: ")
for expoente in range (grau, -1, -1):
    coeficiente = float(input(f"coeficiente de x^(expoente)"))
    funcao += coeficiente * x**expoente

#Calcula a Derivada
derivada = sp.diff(funcao, x)

#exibe os resultados
print("\n========================")
print("FUNÇÃO INFORMADA")
print("==========================")
sp.pprint(funcao)

print("\n==========================")
print("DERIVADA")
print("==========================")
sp.pprint(derivada)

#Cálculo para um valor específico de x

valor_x = float(input("\nDigite o valor de x: "))

resultado_funcao = funcao.subs(x, valor_x)
resultado_derivad = derivada.subs(x, valor_x)

print("\n================================")
print(f"RESULTADOS PARA X = (VALOR_X)")
print("================================")
print(f"f({valor_x}) = {resultado_funcao:.2f}")
