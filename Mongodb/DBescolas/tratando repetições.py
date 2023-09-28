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
listaescolas = []



for documento in resultados:
    linha = ""
    listaanos = documento["Anos"].split(" ")
    contagem = Counter(listaanos)
    listsemrep = list(set(listaanos))
    elementos = contagem.most_common(len(listsemrep))
    for ano,frequencia in elementos:
        linha = f"{linha} {ano} {str(frequencia)} vez(es)"
    collection.update_one({"_id": documento["_id"]}, {"$set": {"Anos":linha}})

    
   

# Fechar a conexão
client.close()