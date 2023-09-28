import pymongo
from collections import Counter
urldomongo = (
    "mongodb+srv://richard_julia:ATALIBArm_2018@febracecluster.qme6nyb.mongodb.net/"
)
estados_do_brasil = ['Acre (AC)', 'Alagoas (AL)', 'Amapá (AP)', 'Amazonas (AM)', 'Bahia (BA)', 'Ceará (CE)', 'Distrito Federal (DF)', 'Espírito Santo (ES)', 'Goiás (GO)', 'Maranhão (MA)', 'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)', 'Minas Gerais (MG)', 'Pará (PA)', 'Paraíba (PB)', 'Paraná (PR)', 'Pernambuco (PE)', 'Piauí (PI)', 'Rio de Janeiro (RJ)', 'Rio Grande do Norte (RN)', 'Rio Grande do Sul (RS)', 'Rondônia (RO)', 'Roraima (RR)', 'Santa Catarina (SC)', 'São Paulo (SP)', 'Sergipe (SE)', 'Tocantins (TO)']

# Estabelecer uma conexão com o servidor MongoDB local
client = pymongo.MongoClient(urldomongo)

# Acessar um banco de dados e uma coleção
db = client["Database_Febrace"]
collection = db["tabela_premiados"]
resultados = collection.find()
listcategorias = []

def print_top_5_elementos_mais_repetidos(lista):
    contagem = Counter(lista)
    elementos_mais_comuns = contagem.most_common(28)
    print("Estados mais premiados na febrace dos últimos 6 anos")
    print("----------------------------")
    for escola, frequencia in elementos_mais_comuns:
        if escola == "Campo não encontrado": 
            continue
        else:
            print(f"o estado {escola} foi premiado {frequencia} vezes.")
            print("------------------------")


for documento in resultados:
    listcategorias.append(documento["Estado"])

top5 = print_top_5_elementos_mais_repetidos(listcategorias)

# Fechar a conexão
client.close()