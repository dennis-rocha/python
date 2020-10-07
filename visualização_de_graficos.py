import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn 
import numpy as np

"""
#Visualição do grafico da taxa de desemprego
data = {'Ano': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
        'Taxa_Desemprego': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]}

df = pd.DataFrame(data, columns =[ "Ano", "Taxa_Desemprego"])

df.plot(x= 'Ano', y="Taxa_Desemprego", kind="line")
df.plot(x= 'Ano', y="Taxa_Desemprego", kind="bar")
plt.show()
"""
x=np.random.randn(200)
y=np.random.randn(200)

#Criei um data frame para mostrar os graficos do eixo X e Y. Utilizei os rotulos X para X e Y paara Y. Poderia por outro nome, mas no exemplo, melhor manter a mesma relação 'x' e 'y'
df = pd.DataFrame({"x":x, "y":y})

sbn.displot(df['x'])
plt.show()

sbn.barplot(df.x, df.y)
plt.show()

sbn.scatterplot(df.x, df.y, hue=df.x)
plt.show()

sbn.pairplot(data=df, vars=["x","y"], hue="x")
plt.show()