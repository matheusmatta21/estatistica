import matplotlib.pyplot as plt
import scipy.stats as scp
import pandas as pd

iris = pd.read_csv("Iris.csv")

species_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
columns_list = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]


def teste_hipotese(p_value):
    return (
        f"Reiejtar H0 (Anormal) : {p_value}"
        if p_value < 0.05
        else f"Nao rejeitar H0 : {p_value}"
    )


def show_histogram(data, bins, _range_):
    plt.hist(data, bins, _range_)
    plt.show()


for specie in species_list:
    for column in columns_list:
        var_atual = iris[iris["Species"] == specie][column]
        p_value = scp.shapiro(var_atual).pvalue
        bins = (((int(max(var_atual)) + 1) - (int(min(var_atual)) - 1)) // 2) + 3

        print(
            f"Valor de prova para a espécie {specie} em relação a coluna {column}: ",
            p_value,
            "\n",
        )
        print(
            f"Teste de hipótese para a espécie {specie} em relação a coluna {column}: ",
            teste_hipotese(p_value),
            "\n",
        )

        if teste_hipotese(p_value) == f"Reiejtar H0 (Anormal) : {p_value}":
            print(
                f"Simetria para a espécie {specie} em relação a coluna {column}:  ",
                scp.skew(var_atual),
                "\n",
            )
        else:
            print(
                f"Curtose para a espécie {specie} em relação a coluna {column}:  ",
                scp.kurtosis(var_atual),
                "\n",
            )
            print(
                f"Simetria para a espécie {specie} em relação a coluna {column}:  ",
                scp.skew(var_atual),
                "\n",
            )

        print("Histograma: \n")
        show_histogram(
            var_atual,
            bins,
            (min(var_atual), max(var_atual)),
        )
