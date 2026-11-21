import sympy as sp 
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application,convert_xor

print("=" * 55)
print(" CALCULADORA DE GRADIENTE")
print(" DERIVADAS PARCIAIS")
print("=" * 55)
print("\nORIENTAÇÕES PARA DIGITAR A FUNÇÃO")
print("-" * 55)
print("Utilize as variáveis x, y e/ou z.")
print("Use ^ para potências; * para multiplicação; / par a divisão.")
print("Utilize parênteses para organizar expressões.")
print("Funções disponíveis: sin, cos, tan, exp, log, sqrt.")
print("-" * 55)

transformacoes = standard_transformations + (implicit_multiplication_application, convert_xor)
variaveis_permitidas = {
 "x": sp.Symbol("x"), "y": sp.Symbol("y"), "z": sp.Symbol("z"),
 "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
 "exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,
 "pi": sp.pi, "E": sp.E
}

while True:
    try:
        entrada = input("\nDigite sua função: ").strip()
        if not entrada:
            print("Digite uma função válida.")
            continue
        funcao = parse_expr(entrada, local_dict=variaveis_permitidas,transformations=transformacoes)
        variaveis = sorted(funcao.free_symbols, key=str)
        if not variaveis:
            print("a função deve possuir pelo menos uma variável.")
            continue
        if not set(variaveis).issubset({sp.Symbol("x"),sp.Symbol("y"), sp.Symbol("z")}):
            print("Utilize apenas as variáveis x, y, z.")
            continue

        print("\n" + "=" * 55)
        print("FUNÇÃO INFORMADA: ")
        sp.pprint(funcao)
        print("\nDERIVADAS PARCIAIS: ")
        gradiente = []
        for v in variaveis:
            derivada = sp.simplify(sp.diff(funcao, v))
            gradiente.append(derivada)
            print(f"\nDerivada parcial em relação a {v}: ")
            sp.pprint(derivada)

        print("\n" + "=" * 55)
        print("VETOR GRADIENTE: ")
        sp.pprint(sp.Matrix(gradiente))
        print("\nGradiente em notação Matemática: ")
        print("∇f =", tuple(gradiente))

        resposta = input("\nDeseja calcular o gradiente em um ponto? (s/n): ").strip().lower()
        if resposta == "s":
            valores = {}
            for v in variaveis:
                while True:
                    try:
                        valor = input(f"Informe {v}: ")
                        valores[v] = float(valor.replace(",","."))
                        break
                    except ValueError:
                        print("Digite um número válido.")
                    resultado = [sp.N(d.subs(valores)) for d in gradiente]
                    print("\nGradiente no Ponto Informado: ") 
                    sp.pprint(sp.Matrix(resultado))

                print("\n" + "=" * 55)
                continuar = input ("Deseja calcular outra função? (s/n): ").strip().lower()
                if continuar!= "s":
                    print ("\n programa encerrado.")
                    break
    except Exception as erro:
        print("\nNão foi  possivel interpretar a função.")
        print("verifique a expressão digitada.")
        print("detalhes:",erro)
           
