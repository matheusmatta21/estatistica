from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd

iris = pd.read_csv('Iris.csv')

species_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
columns_list = ['SepalLengthCm','SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

#(dados , beans//divisoes -> tem que ser multiplo da diferenca do range para que o grafico seja bem plotado, range)

# x = max(iris['PetalLengthCm']) - min(iris['PetalLengthCm'])
# print(max(iris['PetalLengthCm']))


def teste_hipotese(p_value): return f"Reiejtar H0 (Anormal) : {p_value}" if p_value < 0.05 else f"Nao rejeitar H0 : {p_value}"

def show_histogram(data, bins, _range_):
    plt.hist(data, bins, _range_)
    plt.show()

# print('Práticamente simétrico (-0.2 é muito próximo de 0): ', scp.skew(iris['PetalLengthCm']))

# print('Histograma: ')
# show_histogram(iris['PetalLengthCm'], 3, (1 ,7))

for specie in species_list:
    for column in columns_list:
        var_atual = iris[iris['Species'] == specie][column]
        p_value = scp.shapiro(var_atual).pvalue
        bins = (((int(max(var_atual)) + 1 ) - (int(min(var_atual)) - 1)) // 2 ) + 3

        print(f'Valor de prova para a espécie {specie} em relação a coluna {column}: ', p_value, '\n')
        print(f'Teste de hipótese para a espécie {specie} em relação a coluna {column}: ', teste_hipotese(p_value), '\n')

        if teste_hipotese(p_value) == f"Reiejtar H0 (Anormal) : {p_value}":
            print(f'Simetria para a espécie {specie} em relação a coluna {column}:  ', scp.skew(iris[iris['Species'] == specie][column]), '\n')
        else:
            print(f'Curtose para a espécie {specie} em relação a coluna {column}:  ', scp.kurtosis(iris[iris['Species'] == specie][column]), '\n')
            print(f'Simetria para a espécie {specie} em relação a coluna {column}:  ', scp.skew(iris[iris['Species'] == specie][column]), '\n')

        print('Histograma: \n')
        show_histogram(iris[iris['Species'] == specie][column], bins, (min(var_atual) ,max(var_atual)))

