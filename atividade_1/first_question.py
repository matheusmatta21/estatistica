import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

iris = pd.read_csv('Iris.csv')

def get_specie(specie : str): return iris[iris['Species'] == specie]

def get_petal_lenght_specie(specie : str): return iris[iris['Species'] == specie]['PetalLengthCm']

def get_mean_petal_length(specie : str): return get_petal_lenght_specie(specie).mean()

def do_boxplot(data):
    sns.boxplot(data)
    plt.show()

# print('mean: ', iris_setosa_petal_length_mean) #mean:  1.464
print('mean iris-setosa: ', get_mean_petal_length('Iris-setosa'))
do_boxplot(get_petal_lenght_specie('Iris-setosa'))

# print('mean: ', iris_versicolor_petal_length_mean) #mean:  4.26
print('mean iris-versicolor: ', get_mean_petal_length('Iris-versicolor'))
do_boxplot(get_petal_lenght_specie('Iris-versicolor'))

# print('mean: ', iris_virginica_petal_length_mean) #mean:  5.5520000000000005
print('mean iris-virginica: ', get_mean_petal_length('Iris-virginica'))
do_boxplot(get_petal_lenght_specie('Iris-virginica'))
