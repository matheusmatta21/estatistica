import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

iris = pd.read_csv("Iris.csv")
iris_setosa= iris[iris.Species == 'Iris-setosa']
iris_sepal_length_cm = iris['SepalLengthCm']
# print(type(iris))

#histograma
#evitar range sync.min e . max, arredondar os valores e colocar manualmente
# plt.hist(iris, 5, (min(iris), max(iris)))
# plt.show() #(dados , beans//divisoes -> tem que ser multiplo da diferenca do range para que o grafico seja bem plotado, range)

#boxplot

print(iris_setosa['SepalLengthCm'])

# sns.boxplot(iris_setosa['SepalLengthCm'])
# plt.show()

# Filtra pelo nome da espécie
# iris_setosa = iris[iris['Species'] == 'Iris-setosa']

# def calculate_iqr_outliers_iqr(data):
#     # Calcula o primeiro e terceiro quartis
#     Q1 = data.quantile(0.25)
#     Q3 = data.quantile(0.75)
    
#     # Calcula o intervalo interquartil (IQR)
#     IQR = Q3 - Q1
    
#     # Define os limites inferior e superior para outliers
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
    
#     # Encontra os outliers
#     outliers = data[(data < lower_bound) | (data > upper_bound)]
    
#     return outliers, lower_bound, upper_bound

# # Usando a função para Iris-setosa
# # outliers, lower_bound, upper_bound = calculate_iqr_outliers_iqr(iris_setosa_petal_length_data)

# def remove_outliers(data):
#     # Calcula o primeiro e terceiro quartis
#     Q1 = data.quantile(0.25)
#     Q3 = data.quantile(0.75)
    
#     # Calcula o intervalo interquartil (IQR)
#     IQR = Q3 - Q1
    
#     # Define os limites inferior e superior para outliers
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
    
#     # Filtra os dados que estão dentro dos limites (ou seja, sem outliers)
#     filtered_data = data[(data >= lower_bound) & (data <= upper_bound)]
    
#     return filtered_data

# iris_setosa_petal_length_data = iris[iris['Species'] == 'Iris-setosa']['PetalLengthCm']
# iris_versicolor_petal_length_data = iris[iris['Species'] == 'Iris-versicolor']['PetalLengthCm']
# iris_virginica_petal_length_data = iris[iris['Species'] == 'Iris-virginica']['PetalLengthCm']

# # Usando a função para remover os outliers de Iris-setosa
# filtered_setosa_data = remove_outliers(iris_setosa_petal_length_data)
# filtered_versicolor_data = remove_outliers(iris_versicolor_petal_length_data)
# filtered_virginica_data = remove_outliers(iris_virginica_petal_length_data)

# Exibindo o resultado
# print(f'Dados filtrados sem outliers:\n{filtered_setosa_data}')
# print(f'Nº de valores sem outliers: {filtered_setosa_data.size}')
# print('mean filtered_setosa_petal_length_data: ', filtered_setosa_data.mean())#1.46304347826087
# print('mean filtered_setosa_petal_length_data: ', filtered_versicolor_data.mean())#4.28571428571428
# print('mean filtered_setosa_petal_length_data: ', filtered_virginica_data.mean())#5.5520000000000005


# Exibindo os resultados
# print(f'Outliers: {outliers}')
# print(f'Limite inferior: {lower_bound}')
# print(f'Limite superior: {upper_bound}')

# iris_setosa = get_petal_lenght_specie('Iris-setosa')
# iris_versicolor = get_petal_lenght_specie('Iris-versicolor')
# iris_virginica = get_petal_lenght_specie('Iris-virginica')

# x = iris['PetalLengthCm'].mean()
# ponto_corte = iris['PetalLengthCm'].std(ddof=1) * 3
# inf, sup = x - ponto_corte, x + ponto_corte
# outliers = iris['PetalLengthCm'][(iris['PetalLengthCm'] < inf) | (iris['PetalLengthCm'] > sup)]
# outliers = iris['PetalLengthCm'][(iris['PetalLengthCm'] < inf) | (iris['PetalLengthCm'] > sup)]
# print(outliers)         


# Aplicando ao comprimento das pétalas

# outliers, lower_bound, upper_bound = calculate_std_outliers(iris[iris['Species'] == 'Iris-setosa']['PetalLengthCm'])
# print(f'Outliers: {outliers}')
# print(f'Limite inferior: {lower_bound}')
# print(f'Limite superior: {upper_bound}')
