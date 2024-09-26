import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

iris = pd.read_csv('Iris.csv')

species_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

#Essa função retorna a espécie desejada 

def get_specie(specie : str): return iris[iris['Species'] == specie]

#Essa função retorna os comprimentos da pétala da espécie desejada

def get_petal_lenght_specie(specie : str): return iris[iris['Species'] == specie]['PetalLengthCm']

#Essa função retorna a média dos comprimentos da pétala da espécie desejada

def get_mean_petal_length(specie : str): return get_petal_lenght_specie(specie).mean()

#Essa função cria e mostra um gráfico boxplot com os dados desejados

def do_boxplot(data):
    sns.boxplot(data)
    plt.show()

#Execução principal do programa, que percorre todas as espécies e imprime a média dos comprimentos da pétala e o gráfico para cada espécie

for specie in species_list:
    print(f'média dos comprimentos da pétala para a espécie {specie}: {get_mean_petal_length(specie)}')
    do_boxplot(get_petal_lenght_specie(specie))
