from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd
import math

GRUPO_A = np.array([80, 85, 90, 78, 82, 88, 84])
GRUPO_B = np.array([78, 80, 85, 88, 82, 86, 90])

def teste_hipotese(p_value): return "Reiejtar H0" if p_value < 0.05 else "Nao rejeitar h0"

p_value_A_shapiro = scp.shapiro(GRUPO_A).pvalue
print(p_value_A_shapiro)
p_value_B_shapiro = scp.shapiro(GRUPO_B).pvalue
print(p_value_B_shapiro)

print(teste_hipotese(p_value_A_shapiro))
print(teste_hipotese(p_value_B_shapiro))

#ambos tem distribuição normal

test_stat_var, p_value_levene = scp.levene(GRUPO_A, GRUPO_B)
print(p_value_levene)
print(teste_hipotese(p_value_levene))

#variancia é a mesma

ttest,p_value_tteste = scp.ttest_ind(GRUPO_A, GRUPO_B)
print(p_value_tteste)
print(teste_hipotese(p_value_tteste / 2))


