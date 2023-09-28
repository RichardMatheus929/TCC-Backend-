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

escolas = db["escolas_premiadas"]


listdicionary = []

resultados = collection.find()
resultadosescolas = escolas.find()

def acharanos(escola: str, listaobjetos:list):

    anos = ""

    for i in range(len(listaobjetos)):
        if escola == listaobjetos[i]["Escola"]:
            anos = listaobjetos[i]["Anos"] + " " + anos

    return anos.strip()

for documento in resultados:
    dicionary = {
        "Escola":documento["Escola"],
        "Anos":documento["Ano"]
    }
    listdicionary.append(dicionary)


for escola in resultadosescolas:
  
    escolas.update_one({"_id": escola["_id"]}, {"$set": {"Anos":acharanos(escola["Escola"],listdicionary)}})









        


# Fechar a conexão
client.close()

