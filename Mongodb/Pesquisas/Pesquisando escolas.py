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

ano = "2018"

resultados = collection.find({"Ano":ano})

listescolas = []  #Onde vão ficar todas as escolas do db, necessário para usar o counter
listdicionary = [] #list onde guarda um obj de cada escola


def acharcidade(escola):
    cidade = ""
    for i in range(len(listdicionary)):
        if listdicionary[i]["Escola"] == escola:
            cidade = listdicionary[i]["Cidade"]
    return cidade

def acharestado(escola):
    estado = ""
    for i in range(len(listdicionary)):
        if listdicionary[i]["Escola"] == escola:
            estado = listdicionary[i]["Estado"]
    return estado


for documento in resultados:  

    listescolas.append(documento["Escola"]) 
    
    dicionarydb = {
        "Escola":documento["Escola"],
        "Cidade":documento["Cidade"],
        "Estado":documento["Estado"]
    }

    listdicionary.append(dicionarydb)




contagem = Counter(listescolas) #Cria um objeto para contar os elementos das escolas do DB

elementos_mais_comuns = contagem.most_common(26)#Cria uma tupla com as escolas e frequencias

for escolas,frequencia in elementos_mais_comuns:
    
    if escolas == "Campo não encontrado":
        continue
    else:
        print("-----------------------------------------------------------------------")
        print(f"{escolas} da cidade {acharcidade(escolas)} de {acharestado(escolas)} foi premiada {frequencia} vezes em {ano}")
        print("-----------------------------------------------------------------------")








# Fechar a conexão
client.close()
