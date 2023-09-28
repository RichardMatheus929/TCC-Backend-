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
dbescolas = db["escolas_premiadas"]


listdicionaty = []
listescolas = []

escolas = dbescolas.find()
resultados = collection.find()


for documento in resultados:
    listescolas.append(documento["Escola"])

escolasconj = set(listescolas)
listsemrepetição = list(escolasconj)

def contar_repeticoes(string, lista):
    contador = 0
    for item in lista:
        if item == string:
            contador += 1
    return contador

for schol in escolas:

    dbescolas.update_one({"_id": schol["_id"]}, {"$set": {"qntdpremiacao": contar_repeticoes(schol["Escola"],listescolas)}})





# Fechar a conexão
client.close()

