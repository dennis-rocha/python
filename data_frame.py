import pandas as pd 
import numpy as np
#Declação de um DataFrame
df = pd.DataFrame ({
    "Nome": ["Joao", "Marcelo", "Ana Maria"],
    "Idade": [21,36,29],
    "Sexo": ["Masculino", "Masculino", "Feminino"],
    "telefone": [123,456, 789]
})

#Declaração de uma Series
s= pd.Series(np.random.randn(5), index=[1,'b',3,'c',5]) #Usando o index para mostrar diferente a listagem

print(df)
print("===============")
print(s)
print("===============")

#Criando um DataFrame atraves de um dicionario
dicionario = {"Produto": ["Gel capilar", "Oleo para barba", "Minoxidil"], "Preco": [34.90, 54.90, 79.90]}

produtos= pd.DataFrame(dicionario)

print (produtos)

print("===============")

#Criando uma Series atraves de um vetor
vetor = np.array([11,22,33,44])
print(vetor)
series=pd.Series(vetor)
print(series)

#Mostrando apenas uma coluna em um DataFrame
print("===============")
print(f"Mostrando a coluna com os nomes do DataFrame \n{df.Nome}")
print(f"Mostrando a media das idades do dataframe \n\n{df.Idade.mean()}")