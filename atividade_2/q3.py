from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd
import math

from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd
import math

GRUPO_A = np.array([5, 7, 6, 8, 5])
GRUPO_B = np.array([4, 6, 5, 7, 6])
GRUPO_C = np.array([6, 8, 7, 9, 7])

def teste_hipotese(p_value): return "Reiejtar H0" if p_value < 0.05 else "Nao rejeitar h0"

p_value_A_shapiro = scp.shapiro(GRUPO_A).pvalue #0.4211485683917999
print(p_value_A_shapiro)
p_value_B_shapiro = scp.shapiro(GRUPO_B).pvalue #0.8139519691467285
print(p_value_B_shapiro)
p_value_C_shapiro = scp.shapiro(GRUPO_C).pvalue #0.8139519691467285
print(p_value_C_shapiro)

print(teste_hipotese(p_value_A_shapiro)) #n reiejta
print(teste_hipotese(p_value_B_shapiro)) #n rejeita
print(teste_hipotese(p_value_C_shapiro)) #n rejeita

#ambos tem distribuição normal

test_stat_var, p_value_levene = scp.levene(GRUPO_A, GRUPO_B, GRUPO_C) #0.049332195639921764
print(p_value_levene)
print(teste_hipotese(p_value_levene)) #reiejta

#variancia é igual 

F, p_value = scp.f_oneway(GRUPO_A,GRUPO_B,GRUPO_C)
print("p value:%.6f" % p_value)
if p_value <0.05:
 print("Reject null hypothesis")
else:
 print("Fail to reject null hypothesis")


#as medias sao iguais


