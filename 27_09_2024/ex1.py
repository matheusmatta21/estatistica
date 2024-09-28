from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd
import math

dados = np.array([41.60, 41.48, 42.34, 41.95, 41.86, 42.18, 41.72, 42.26, 41.81, 42.04]) #lista de condutividade de aços

desvio_padrao = dados.std(ddof=1)

erro_padrao =  desvio_padrao / math.sqrt(len(dados))

media_amostral_dados = dados.mean()

intervalo_media_populacional = [media_amostral_dados - (3 * erro_padrao), media_amostral_dados + (3 * erro_padrao)]


print('desvio padrão:', dados.std(ddof=1))
print('erro comum:', erro_padrao)
print('media dados:', media_amostral_dados)
print('intervalo para media populacional:', intervalo_media_populacional)

#bootstrap

# boot_sample = np.random.choice(dados, size=10, replace=2) #size = tamanho da simulacao (simula 10 dados) quantidade de dados que vc quer que apareça na simu
# print('boot sample:', boot_sample)

lista_media = []

for i in range (0,200):
    boot_sample = np.random.choice(dados, size=10, replace=True) #simulacao de dados baseados na variavel dados
    media = boot_sample.mean()
    lista_media.append(media)
# print('lista media dos boot sample: ', lista_media)
boot_means = np.array(lista_media).mean()
print('media das medias:', boot_means)
print('desvio padrao//erro comum das medias: ', np.std(lista_media)) #dp e ec tem a mesma forumla 