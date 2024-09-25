import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

iris = pd.read_csv('Iris.csv')

species_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
columns_list = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

def show_boxplot(data):
    sns.boxplot(data)
    plt.show()

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

        show_boxplot(var_atual)