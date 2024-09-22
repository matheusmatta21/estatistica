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
    return correlation, p_value

def find_spearman_correlation(x, y):
    correlation, p_value = scp.spearmanr(x, y)
    return correlation, p_value

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


# Coeficiente de correlação, saber o quanto uma variável está relacionada uma com a outra
# print(scp.spearmanr(x, y)) # assimétrico, não paramétrico
# scp.pearsonr(x,y) -> teste paramétrico (dentro de certo parâmetro), todas as variáveis precisam ter distribuição normal


iris = pd.read_csv('Iris.csv')

x = iris['SepalLengthCm']
y = iris['PetalLengthCm']


#dados numericos da correlação

print('general spearman coefficient: ', find_spearman_correlation(x, y)) # coeficiente de correlacao: (np.float64(0.8813863932886515), valor de prova: np.float64(4.64951031453217e-50))
print('general pearson coefficient: ', find_pearson_correlation(x, y)) # coeficiente de correlacao: (np.float64(0.871754157304871),valor de prova: np.float64(1.0384540627942323e-47))
# Correlação de Pearson entre SepalLengthCm e PetalLengthCm para Iris-setosa: 0.2638740929186869 (p-value: 0.06407651344005683)
# Correlação de Pearson entre SepalLengthCm e PetalLengthCm para Iris-versicolor: 0.7540489585920163 (p-value: 2.586189505280907e-10)
# Correlação de Pearson entre SepalLengthCm e PetalLengthCm para Iris-virginica: 0.8642247329355763 (p-value: 6.297785758903822e-16)

#graficos de dispersão da correlacao:

show_scatterplot(iris, x, y)

process_iris_data(iris, 'Iris-setosa', 'SepalLengthCm', 'PetalLengthCm')
process_iris_data(iris, 'Iris-versicolor', 'SepalLengthCm', 'PetalLengthCm')
process_iris_data(iris, 'Iris-virginica', 'SepalLengthCm', 'PetalLengthCm')
