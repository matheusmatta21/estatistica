from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd
import math

dados = np.array([24.1514, 27.4145, 20.4, 22.5151, 28.5152, 28.5611, 21.2459, 20.9983, 24.9840, 22.6245]) #tempo para processar pedidos de emprestimos (em h)

media_amostral_dados = dados.mean()

desvio_padrao = dados.std(ddof=1)

erro_padrao =  desvio_padrao / math.sqrt(len(dados))

intervalo_media_populacional = [media_amostral_dados - (3 * erro_padrao), media_amostral_dados + (3 * erro_padrao)]

print('desvio padrão', dados.std(ddof=1))
print('erro comum:', erro_padrao)
print('media dados:', media_amostral_dados)
print('intervalo para media populacional:', intervalo_media_populacional)


lista_media = []

for i in range (0,200):
    boot_sample = np.random.choice(dados, size=10, replace=True) #simulacao de dados baseados na variavel dados
    media = boot_sample.mean()
    lista_media.append(media)
# print('lista media dos boot sample: ', lista_media)
boot_means = np.array(lista_media).mean()
print('media das medias:', boot_means)
print('desvio padrao//erro comum das medias: ', np.std(lista_media)) #dp e ep tem a mesma forumla para o bootstrap