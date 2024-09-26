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
columns_list = ['SepalLengthCm', 'PetalLengthCm']

#Essa função cria e mostra gráficos de dispersão

def show_scatterplot(data, x_col, y_col):
    sns.scatterplot(data=data, x=x_col, y=y_col)
    plt.show()

#Essa função calcula e imprime valores de correlação de Pearson

def find_pearson_correlation(x, y):
    correlation, p_value = scp.pearsonr(x, y)
    print(f'Coeficiente de correlação de Pearson: ', correlation)
    print('Valor de prova: ', p_value)

#Essa função calcula e imprime valores de correlação de Spearman

def find_spearman_correlation(x, y):
    correlation, p_value = scp.spearmanr(x, y)
    print(f'Coeficiente de correlação de Spearman: ', correlation)
    print('Valor de prova: ', p_value)

#Essa função processa dados de uma determinada espécie de iris e exibe gráficos de dispersão e correlações de Pearson e Spearman.

def process_iris_data(iris, species, x_col, y_col):
    # Filtra os dados pela espécie
    iris_species = iris[iris['Species'] == species]
    
    # Extrai os valores de x e y
    x = iris_species[x_col]
    y = iris_species[y_col]
    
    # Calcula a correlação de Pearson
    find_pearson_correlation(x, y)

    # Calcula a correlação de Spearman
    find_spearman_correlation(x, y)

    # Cria e mostra o gráfico de dispersão
    show_scatterplot(iris_species, x_col, y_col)

#Execução principal do programa, onde columns_list[0] corresponde ao comprimento da sépala e columns_list[1] corresponde ao comprimento da pétala. 

for specie in species_list:
    print(f'\nCorrelação entre {columns_list[0]} e {columns_list[1]} em relação à especie {specie}: \n')
    process_iris_data(iris, specie, columns_list[0], columns_list[1])