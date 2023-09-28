import pymongo
from collections import Counter
urldomongo = (
    "mongodb+srv://richard_julia:ATALIBArm_2018@febracecluster.qme6nyb.mongodb.net/"
)

# Estabelecer uma conexão com o servidor MongoDB local
client = pymongo.MongoClient(urldomongo)

# Acessar um banco de dados e uma coleção
db = client["Database_Febrace"]
collection = db["escolas_premiadas"]
resultados = collection.find()

for documento in resultados:
    print(documento["Escola"])
    print(documento["Estado"])
    print("---------------------------------------")


# Fechar a conexão
client.close()