from array import array
import numpy as np
import statistics

sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])

asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2, 78.2])

#media (x) s -> sync | as -> Async:

xs = sync.mean() #calcula a media
xas = asyncr.mean() #calcula a media

print("media sync:", xs)
print("media asyncr:", xas)

#mediana (me), S -> sync | As -> Async:

me_s = np.median(sync) #quartil 2
me_as = np.median(asyncr) #quartil 2

print("mediana sync:", me_s)
print("mediana asyncr:", me_as)

#media e mediana do sync estao mais proximas (distribuicao normal) do que as do async r

#percentil s -> sync | as -> Async:

#Pn (percentil, p1 ate p10) ou Qn (quartil, q1 ate q4) (n -> posicao do quartil)

#por norma, o percentil divide sempre de 10% em 10%

#quartil sao percentis de 25% em 25%

P3s = np.percentile(sync, 30) #terceiro percentil (10 + 10 + 10)
Q1s = np.percentile(sync, 25) #primeiro quartil esta exatamente em 25%
Q3s = np.percentile(sync, 75) #tereceiro quartil esta exatamente em 75%

Q1as = np.percentile(asyncr, 25) #primeiro quartil esta exatamente em 25%
Q3as = np.percentile(asyncr, 75) #tereceiro quartil esta exatamente em 75%

print("primeiro quartil sync:", Q1s)
print("terceiro quartil sync:", Q3s)
print("primeiro quartil asyncr:", Q1as)
print("terceiro quartil asyncr:", Q3as)

#obs: para encontrar o tamanho do conjunto de dados:
# print(len(sync)) -> 22 | len(dados)
# print(len(asyncr)) ->14| len(dados)

#moda (mode):

mode_s = statistics.multimode(sync)
mode_as = statistics.multimode(asyncr)

print("moda sync:", mode_s)
print("moda asyncr:", mode_as) #se apagar o 71.7, a moda vira o primeiro elemento da lista (distribuicao amodal), se adicionar o 78.2, fica com duas modas (bimodal, trimodal ou polimodal) e retorna a primeira moda da lista (usar statistics.multimode())

# se len(dados) == len(statistics.multimode(dados)) -> distribuicao amodal



