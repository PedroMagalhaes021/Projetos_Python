math -> Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.
Random -> Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.
Datetime -> Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.

#exemplo utilizando o random e o Datetime
  import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual
