import pandas as pd
import matplotlib.pyplot as plt

# index_col - defini diretamente qual será a coluna utilizada para o índice.
data = pd.read_excel('../dados/WIN_MT5.xlsx', index_col=0)

print(data.dtypes)







# Plotando grafico
data.open.plot()
plt.show()
