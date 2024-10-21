import pandas as pd
import matplotlib.pyplot as plt

# carregar o arquivo CSV PETR4
data = pd.read_csv('../dados/PETR4.csv')

# carregar o arquivo TXT
data2 = pd.read_csv('../dados/PETR4.txt')

"""
Em muitos casos, o arquivo .txt pode apresentar uma formatação diferente do padrão usado no Python.

Por exemplo, separador decimal como vírgula (, padrão no português) e não ponto (.)

Nesses casos usamos diversos argumentos que auxiliam na leitura dos dados
"""

# Arquivo extraído do Profit
# sep = defini o separador de coluna
# decimal = defini o separador decimal

petr_profit = pd.read_csv('../dados/PETR4_PROFIT.txt', sep=';', decimal=',')




# Exibir as primeiras 5 linhas
print('Exibir as primeiras 5 linhas', '\n', data.head())

# Exibir as ultimas 5 linhas
print('\nExibir as ultimas 5 linhas', '\n', data2.tail())

# Exibir informações sobre o DataFrame
print('\nExibir informações sobre o DataFrame', '\n\n', data.info())

# Exibir estatísticas descritivas
print('\nExibir estatísticas descritivas', '\n', data.describe())

print(f'Tipo de variável: {type(data)}')

# Plota o grafico
# data1.Close.plot()
# plt.show()

# Exibir uma coluna especifica
print(data['Date'])

# Verifica o tipo de objeto de cada coluna
print(data2.dtypes)

# Verificar qual o index
print(data.index)

# convertendo a coluna data para o padrão de objeto 'Date'
# pd.to_datetime(data1['Date'])

# Definindo como o Index para a coluna Date
# data1.index = data1['Date']

# convertendo a coluna data para o padrão de objeto 'Date' e Definindo como o Index para a coluna Date
data.index = pd.to_datetime(data['Date'])

# Verificando nome das colunas
print(data.columns)

# Verificar dimensões do dataframe
print(data.shape)

# Close é o nome da coluna do dataframe que você quer plotar
data.Close.plot()

# Exibindo o maior valor da Coluna Close
print(data.Close.max().round(2))

# Exibindo o menor valor da Coluna Close (Valor de Fechamento do Pregão)
print(data.Close.min().round(2))

# Exibindo o valor maior que a ação atingiu durante um pregão (Coluna High)
print(data.High.max().round(2))

# Exibindo a média do preço de fechamento
print(data.Close.mean().round(2))

# Exibindo a mediana do preço de fechamento
print(data.Close.median().round(2))

# Valor da moda
print(data.Close.mode().round(2))

# Valor da Variância
print(data.Close.var())

# Valor do desvio padrão
print(data.Close.std())

# Calcular a porcentagem de variação do preço de fechamento de um dia para outro.
pct_retorno = data.Close.pct_change()
print(pct_retorno)

# Calcular o desvio padrão do retorno
print(pct_retorno.std().round(2))

print(petr_profit)

