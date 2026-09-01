from collections import deque


fila=deque(["Aluno1","Aluno2","Aluno3"])


print(fila[0])
print(fila[-1])

fila.append("Aluno4")
print(fila[-1])


fila.appendleft("Aluno5")
print(fila[0])

fila.extend(["Aluno10","Aluno20"])
print(fila)

fila.extendleft(["Aluno11","Aluno12"])
print(fila)

fila.remove("Aluno12")
print(fila)
fila.pop()
print(fila)

print(len(fila))

fila.clear()
print(fila)
