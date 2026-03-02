from modelo import regressao_polinomial
from graficos import g_real_vs_predito, g_residuos, histograma_residuos
from dados import limpeza

import pandas as pd

#importando e limpando o DataFrame

df_residencias = pd.read_excel('/home/davi-dos-santos-freire/VSCode/RP_imóveis/residencias.xlsx')
df_residencias = limpeza(df_residencias)

#Definindo variáveis e executando função de regessão polinomial

X = df_residencias.drop('preco', axis=1)
y = df_residencias['preco']

y_teste, previsoes = regressao_polinomial(X, y)

#Baixando gráficos

# g_residuos(y_teste, previsoes)                      
# g_real_vs_predito(y_teste, previsoes)               
# histograma_residuos(y_teste, previsoes)             

#Descomente os códigos acima para baixar os gráficos (resíduos, histograma de resíduos e comparação dos valores preditos com os reais)