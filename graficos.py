import seaborn as sns
import matplotlib.pyplot as plt


# Criando funcao de grafico de residuos
def g_residuos(y, y_previsto):
    residuos = y - y_previsto
    
    plt.figure(figsize=(8, 5), dpi=100)

    sns.scatterplot(x=y_previsto, y=residuos)
    plt.axhline(0, color="r", ls="--")

    plt.xlabel("Previsões")
    plt.ylabel("Resíduos")

    plt.title("Grafico de Residuos")
    plt.grid(True)

    plt.savefig("residuos.png", dpi=120, bbox_inches="tight")



# Criando funcao de real vs predito
def g_real_vs_predito(y, y_previsto):
    plt.figure(figsize=(8, 5))
    

    sns.scatterplot(x=y, y=y_previsto)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color="red", linestyle="--")

    plt.xlabel("Valor Real")
    plt.ylabel("Valor Predito")

    plt.title("Real vs Predito")
    plt.grid(True)

    plt.savefig("real vs predito.png", dpi=120, bbox_inches="tight")



# Criando funcao de histograma de residuos
def histograma_residuos(y, y_previsto):
    residuos = y - y_previsto

    plt.figure(figsize=(8, 5))
    sns.histplot(residuos, kde=True)

    plt.title("Distribuicao dos Residuos")
    plt.grid(True)

    plt.savefig("histograma de residuos.png", dpi=120, bbox_inches="tight")
