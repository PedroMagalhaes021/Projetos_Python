import sympy as sp

x = sp.symbols("x")

grau = int(input("Grau do polinômio: "))

funcao = 0

for expoente in range (grau, -1, -1):
    coef = float(input(f"coeficiente de x^{expoente}"))
    funcao += coef * x**expoente

print("\nFunção: ")
sp.pprint(funcao)

a = float(input("\nLimite Inferior: "))
b = float(input("Limite superior: "))

resultado = sp.integrate(funcao, (x, a, b))
sp.pprint(resultado)

print("\nValor Decimal: ",float(resultado))
