import pandas as pd
import sqlite3

conector = sqlite3.connect("aulaDB.db")
#Não existe tabela criada nesse arquivo. Fica como exemplo de como usar o comando pd.read_sql_query()
#variavel = pd.read_sql_query("SELECT * FROM pessoa", conector)
#print(variavel.head())

#data = pd.DataFrame([[111, "Gel para cabelo", 29.9],[222, "Oleo para barba", 49.9], [333, "Minoxidil", 69.9]],
#                    columns =["id", "Descricao", "preco"])

#print(data)
#data.to_sql("Produto", conector)

test = pd.read_sql_query("SELECT * FROM Produto", conector)
print(test.head())
