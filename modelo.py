from sklearn.preprocessing import PolynomialFeatures  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

#Criando função do modelo de regressão polinomial

def regressao_polinomial(X, y):
    conversor_polinomial = PolynomialFeatures(degree=2, include_bias=False)
    X_poli = conversor_polinomial.fit_transform(X)

    X_treino, X_teste, y_treino, y_teste = train_test_split(X_poli, y, test_size=0.3, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_treino,y_treino)
    previsoes = modelo.predict(X_teste)

    erro_medio_absoluto = mean_absolute_error(previsoes, y_teste)
    raiz_do_erro_medio_quadratico = root_mean_squared_error(previsoes, y_teste)

    #Fazendo estimativas de acordo com os dados informados pelo usuário
    def ler_float(mensagem):
        while True:
            valor = input(mensagem).strip().replace(",", ".")
            try:
                return float(valor)
            except ValueError:
                print("Entrada inválida. Digite apenas números (ex.: 120.5).")

    area = ler_float('Digite aqui a área da casa: ')
    quartos = ler_float('Digite aqui quantos quartos tem na casa: ')
    idade = ler_float('Digite aqui quantos anos a casa tem: ')
    dados_usuario = [area, quartos, idade]

    #Calculando preço baseado nos dados fornecidos pelo usuário
    dados_transformados = conversor_polinomial.transform([dados_usuario])
    previsao = modelo.predict(dados_transformados).round(2)

    print('=' * 60)
    print(f'Sua casa tem o preço de mercado de aproximadamente R${previsao[0]}')
    print('=' * 60)

    # print(f"As taxas médias de erro do modelo são: \n\nMAE: {erro_medio_absoluto}; \nRMSE: {raiz_do_erro_medio_quadratico}")
    return y_teste, previsoes
