import pymongo
from collections import Counter
urldomongo = (
    "mongodb+srv://richard_julia:ATALIBArm_2018@febracecluster.qme6nyb.mongodb.net/"
)

# Estabelecer uma conexão com o servidor MongoDB local
client = pymongo.MongoClient(urldomongo)

# Acessar um banco de dados e uma coleção
db = client["Database_Febrace"]
collection = db["tabela_premiados"]
resultados = collection.find({"Escola":"E.E. Doutor José Fernandes de Melo"})

x = 0

for documento in resultados:
        print(documento["Escola"])
        print(documento["Categoria_de_premiação"])

# Fechar a conexão
client.close()