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


listdicionaty = []
listescolas = []

resultados = collection.find()


for documento in resultados:
    dicionary = {
        "Escola":documento["Escola"],
        "Cidade":documento["Cidade"],
        "Estado":documento["Estado"]
    }
    listdicionaty.append(dicionary) #lista de dicionary com os itens  
    listescolas.append(documento["Escola"]) #lista de escolas com todas as escolas 

  
def acharcidade(escola):
    cidade = ""
    for i in range(len(listdicionaty)):
        if listdicionaty[i]["Escola"] == escola:
            cidade = listdicionaty[i]["Cidade"]
    return cidade


def acharestado(escola):
    estado = ""
    for i in range(len(listdicionaty)):
        if listdicionaty[i]["Escola"] == escola:
            estado = listdicionaty[i]["Estado"]
    return estado

escolasconj = set(listescolas)
listescolas = list(escolasconj) #removendo as escolas repetidas da lista de escolas

for i in range(len(listescolas)):  #for dentro da lista de escolas sem rep
    objeto = {
        "Escola":listescolas[i],
        "Cidade":acharcidade(listescolas[i]), #achar a cidade pelo nome da escola - pesquisando no meu database
        "Estado":acharestado(listescolas[i])  #o mesmo pra estado
    }
    escolas.insert_one(objeto)

# Fechar a conexão
client.close()

