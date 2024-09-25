from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd

iris = pd.read_csv('Iris.csv')

species_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
columns_list = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

for specie in species_list:
    for column in columns_list:
        var_atual = iris[iris["Species"] == specie][column]
        
        #media

        media_atual = var_atual.mean()
        print(f'\na média da coluna {column} da especie {specie} é {media_atual}\n')

        # desvio padrao

        desvio_padrao_atual = var_atual.std(ddof=1)
        print(f'o desvio padrao da coluna {column} da especie {specie} é {desvio_padrao_atual}\n')
        # coeficiente de variacao

        coeficiente_variacao_atual = desvio_padrao_atual / media_atual
        print(f'o coeficiente de variacao da coluna {column} da especie {specie} é {coeficiente_variacao_atual}\n')

        #variancia
        variancia_atual = var_atual.var(ddof=1)
        print(f'a variância da coluna {column} da especie {specie} é {variancia_atual}\n')

        #distancia interquartil

        Q1 = np.percentile(var_atual, 25) #primeiro quartil esta exatamente em 25%
        Q3 = np.percentile(var_atual, 75) #tereceiro quartil esta exatamente em 75%

        IQR = Q3 - Q1
        print(f'a distancia interquartil da coluna {column} da especie {specie} é {IQR}\n')

        #grafico
        sns.boxplot(var_atual)
        plt.show()
        



# Na interpretação do desvio padrão, lembre-se de que ele é a medida de quanto uma entrada
# típica se desvia da média. Quanto mais espalhadas estiverem as entradas, maior será o desvio
# padrão.

# coeficiente de variacao

# cvs = dp1 / me_s
# print("CVS:", cvs)
# cva = dp2 / me_as
# print("CVA:", cva)

# desvio padrao

# dp1 = sync.std(ddof=1)
# dp2 = asyncr.std(ddof=1)

# IQR = Q3s - Q1s #Interquartile Range, é uma métrica robusta para avaliar a dispersão central dos dados, subtraindo o 1º quartil do 3º quartil.

# print('variancia data: ', sync.var(ddof=1)) # amostra, ddof=1 indica que está lidando com uma amostra (amostral) e não com a população.
# print('variancia data_2: ', sync.var(ddof=0))

# print('variancia2 data_2: ', asyncr.var(ddof=1)) # população (?)
# print('variancia2 data_2: ', asyncr.var(ddof=0))