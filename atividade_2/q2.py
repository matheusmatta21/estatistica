from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd
import math

GRUPO_X = np.array([150, 155, 160, 158, 152, 162])
GRUPO_Y = np.array([145, 148, 150, 149, 151, 147])

def teste_hipotese(p_value): return "Reiejtar H0" if p_value < 0.05 else "Nao rejeitar h0"

p_value_A_shapiro = scp.shapiro(GRUPO_X).pvalue #0.8263285160064697
print(p_value_A_shapiro)
p_value_B_shapiro = scp.shapiro(GRUPO_Y).pvalue #0.9636706709861755
print(p_value_B_shapiro)

print(teste_hipotese(p_value_A_shapiro)) #n reiejta
print(teste_hipotese(p_value_B_shapiro)) #n rejeita

#ambos tem distribuição normal

test_stat_var, p_value_levene = scp.levene(GRUPO_X, GRUPO_Y) #0.049332195639921764
print(p_value_levene)
print(teste_hipotese(p_value_levene)) #reiejta

#variancia é DIFERENTE

ttest,p_value_tteste = scp.ttest_ind(GRUPO_X, GRUPO_Y, equal_var=False) #0.9030937836205886
print(p_value_tteste)
print(teste_hipotese(p_value_tteste / 2)) # n rejeita

#as medias sao diferentes


