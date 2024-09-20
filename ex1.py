from array import array
import numpy as np
import statistics
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import scipy.stats as scp
import seaborn as sns
import pandas as pd

sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 80.6])

asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

#media (x) s -> sync | as -> Async:

xs = sync.mean() #calcula a media
xas = asyncr.mean() #calcula a media

print("media sync:", xs)
print("media asyncr:", xas)

#mediana (me), S -> sync | As -> Async:

me_s = np.median(sync) #quartil 2
me_as = np.median(asyncr) #quartil 2

print("mediana sync:", me_s)
print("mediana asyncr:", me_as)

#media e mediana do sync estao mais proximas (distribuicao normal) do que as do async r

#percentil s -> sync | as -> Async:

#Pn (percentil, p1 ate p10) ou Qn (quartil, q1 ate q4) (n -> posicao do quartil)

#por norma, o percentil divide sempre de 10% em 10%

#quartil sao percentis de 25% em 25%

P3s = np.percentile(sync, 30) #terceiro percentil (10 + 10 + 10)
Q1s = np.percentile(sync, 25) #primeiro quartil esta exatamente em 25%
Q3s = np.percentile(sync, 75) #tereceiro quartil esta exatamente em 75%

Q1as = np.percentile(asyncr, 25) #primeiro quartil esta exatamente em 25%
Q3as = np.percentile(asyncr, 75) #tereceiro quartil esta exatamente em 75%

IQR = Q3s - Q1s #Interquartile Range, é uma métrica robusta para avaliar a dispersão central dos dados, subtraindo o 1º quartil do 3º quartil.

print("primeiro quartil sync:", Q1s)
print("terceiro quartil sync:", Q3s)
print("primeiro quartil asyncr:", Q1as)
print("terceiro quartil asyncr:", Q3as)

#obs: para encontrar o tamanho do conjunto de dados:
# print(len(sync)) -> 22 | len(dados)
# print(len(asyncr)) ->14| len(dados)

#moda (mode):

mode_s = statistics.multimode(sync)
mode_as = statistics.multimode(asyncr)

print("moda sync:", mode_s)
print("moda asyncr:", mode_as) #se apagar o 71.7, a moda vira o primeiro elemento da lista (distribuicao amodal), se adicionar o 78.2, fica com duas modas (bimodal, trimodal ou polimodal) e retorna a primeira moda da lista (usar statistics.multimode())

# se len(dados) == len(statistics.multimode(dados)) -> distribuicao amodal

print('amplitude: ', np.ptp(sync)) #amplitude: diferenca entre o valor max e o valor min 
print('amplitude2: ', np.ptp(asyncr))

# desvio padrao

dp1 = sync.std(ddof=1)
dp2 = asyncr.std(ddof=1)


print('variancia data: ', sync.var(ddof=1)) # amostra, ddof=1 indica que está lidando com uma amostra (amostral) e não com a população.
print('variancia data_2: ', sync.var(ddof=0))

print('variancia2 data_2: ', asyncr.var(ddof=1)) # população (?)
print('variancia2 data_2: ', asyncr.var(ddof=0))

# coeficiente de variacao sincrono e assincrono

cvs = dp1 / me_s
print("CVS:", cvs)
cva = dp2 / me_as
print("CVA:", cva)

#histograma
#evitar range sync.min e . max, arredondar os valores e colocar manualmente
plt.hist(asyncr, 5, (65, 95)) #(dados , beans//divisoes -> tem que ser multiplo da diferenca do range para que o grafico seja bem plotado, range)
plt.show()

#boxplot
sns.boxplot(asyncr)
plt.show()

sns.boxplot([sync, asyncr])
plt.xticks([0,1], ['sync', 'asyncr'])
plt.xlabel('work type')
plt.ylabel('hours')
plt.title('grafico')
plt.show()

stock = pd.read_csv("stock_data.csv") #dataset que mostra um conjunto de dados de ações
iris = pd.read_csv("Iris.csv") # O conjunto de dados Íris contém informações sobre 150 flores de íris, divididas em três espécies diferentes: Iris setosa, Iris versicolor e Iris virginica.

print(iris.head())
sns.boxplot(stock['Open'])
plt.show()

dados = stock
x = dados['Open'].mean()
ponto_corte = dados['Open'].std(ddof=1) * 3
inf, sup = x - ponto_corte, x + ponto_corte
outliers = dados['Open'][(dados['Open'] < inf) | (dados['Open'] > sup)]
print(outliers) #Aqui você calcula outliers com base na regra de 3 desvios padrão da média



stock['Date'] = pd.to_datetime(stock['Date'])
sns.lineplot(data=stock, x='Date', y='High') #Plotam-se séries temporais com sns.lineplot() usando o preço mais alto (High) e o mais baixo (Low), com base nas datas.
sns.lineplot(data=stock, x='Date', y='Low')
plt.show()
print(stock.head())

x = iris['SepalLengthCm']
y = iris['SepalWidthCm']
# Coeficiente de correlação, saber o quanto uma variável está relacionada uma com a outra
print(scp.spearmanr(x, y)) # assimétrico, não paramétrico
# scp.pearsonr(x,y) -> teste paramétrico (dentro de certo parâmetro), todas as variáveis precisam ter distribuição normal

sns.scatterplot(data=iris, x='SepalLengthCm', y='SepalWidthCm') #Gera-se um gráfico de dispersão entre comprimento e largura das sépalas.
plt.show()
sns.boxplot([x,y])
plt.show()


tipo_e_tamanho = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

# Filtra pelo nome da espécie
iris_setosa = iris[iris['Species'] == 'Iris-setosa']

def process_iris_data(iris, species, x_col, y_col): #Essa função processa dados de uma determinada espécie de iris e exibe gráficos de dispersão e correlações de Pearson.
    # Filtra os dados pela espécie
    iris_species = iris[iris['Species'] == species]
    
    # Extrai os valores de x e y
    x = iris_species[x_col]
    y = iris_species[y_col]
    
    # Cria o gráfico de dispersão
    sns.scatterplot(data=iris_species, x=x_col, y=y_col)
    
    # Calcula a correlação de Pearson
    correlation, p_value = scp.pearsonr(x, y)
    print(f"Correlação de Pearson entre {x_col} e {y_col} para {species}: {correlation} (p-value: {p_value})")
    
    # Exibe o gráfico
    plt.show()

    # Usando a função para vários pares de colunas e espécies
columns_pairs = [
    ('SepalLengthCm', 'SepalWidthCm'),
    ('PetalLengthCm', 'PetalWidthCm'),
    ('SepalLengthCm', 'PetalLengthCm'),
    ('SepalLengthCm', 'PetalWidthCm'),
    ('SepalWidthCm', 'PetalLengthCm'),
    ('SepalWidthCm', 'PetalWidthCm')
]

species_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Loop para processar todas as combinações de espécies e pares de colunas
for species in species_list:
    for x_col, y_col in columns_pairs:
        process_iris_data(iris, species, x_col, y_col)

def heat_map(species):
    name_specie = iris[iris['Species'] == species]
    iris_specie = name_specie.drop(columns=['Id', 'Species'])
    iris_specie.head()
    cormax = iris_specie.corr()
    print(cormax)
    sns.heatmap(cormax, annot=True)
    plt.show()

for specie in species_list:
    heat_map(specie)