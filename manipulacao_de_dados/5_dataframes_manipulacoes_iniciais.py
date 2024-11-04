import pandas as pd
import matplotlib.pyplot as plt

cotacoes = pd.read_csv('../dados/cotacoes_pd_series.csv', sep=';', index_col=0)

# Permite a visualização de todas as linhas de um dataframe
#pd.set_option('display.max_rows', None)

#print(cotacoes.head())

# Convertendo o índice no padrão datetime, e o resultado atribuímos ao índice
# Como o dia está vindo primeiro que o mes, devemos usar o parametro dayfirst
cotacoes.index = pd.to_datetime(cotacoes.index, dayfirst=True)

# Data Frames de uma coluna só são chamados pelo 'Pandas' de 'Pandas Series'.
#print(cotacoes.head())

#convertendo Panda Series para Panda Date Frame
cotacoes['Adj Close'].to_frame()

#print(cotacoes.head())


petr = pd.read_csv('../dados/PETR4.csv')

# Transformando a coluna Date no Index, porém ainda mantem a coluna no data frame
petr.index = petr.Date

# Configurar o Index do data frame usando uma coluna existente
#petr.set_index('Date', inplace=True)

print(petr)

# A função 'Drop' remove colunas ou linhas do Data Frame, Argumentos: Axis = 0 'Remove Linhas' | Axis = 1 'Remove Colunas'
#Removendo Coluna Date Duplicada
#petr = petr.drop(["Date"], axis=1)

# Quando inplace=True, a alteração é feita "no local", ou seja, no próprio DataFrame original, sem a necessidade de atribuir o resultado a uma nova variável.
petr.drop(['Date', 'Volume'], axis=1, inplace = True)

print(petr.head())

# Faz uma cópia do data frame
cotacoes_petr = petr.copy()

print(cotacoes_petr.head())

# Geralmente no mercado financeiro trabalhamos com as colunas 'Open, High, Low e Close' = OHLC.

print(cotacoes_petr.tail())

#cotacoes_petr[['High', 'Open', 'Close']].plot()

# Filtra as Colunas e plota os 100 ultimas linhas
cotacoes_petr[['Close']].tail(100).plot()
plt.show()
