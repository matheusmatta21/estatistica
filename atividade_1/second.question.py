from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd

def show_scatterplot(data, x_col, y_col):
    sns.scatterplot(data=data, x=x_col, y=y_col)
    plt.show()

def find_pearson_correlation(x, y):
    correlation, p_value = scp.pearsonr(x, y)
    print(f'spearman correlation coefficient for {x} and {y} : ', correlation)
    print('proof value: ', p_value)

def find_spearman_correlation(x, y):
    correlation, p_value = scp.spearmanr(x, y)
    print(f'spearman correlation coefficient for {x} and {y} : ', correlation)
    print('proof value: ', p_value)

def process_iris_data(iris, species, x_col, y_col): #Essa função processa dados de uma determinada espécie de iris e exibe gráficos de dispersão e correlações de Pearson.
    # Filtra os dados pela espécie
    iris_species = iris[iris['Species'] == species]
    
    # Extrai os valores de x e y
    x = iris_species[x_col]
    y = iris_species[y_col]
    
    # Cria o gráfico de dispersão
    show_scatterplot(iris_species, x_col, y_col)
    
    # Calcula a correlação de Pearson
    correlation, p_value = scp.pearsonr(x, y)
    print(f"Correlação de Pearson entre {x_col} e {y_col} para {species}: {correlation} (p-value: {p_value})")
    correlation, p_value = scp.spearmanr(x, y)
    print(f"Correlação de Spearman entre {x_col} e {y_col} para {species}: {correlation} (p-value: {p_value})")