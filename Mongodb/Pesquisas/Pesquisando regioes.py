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

resultados = collection.find()
norte = []
nordeste = []
centro = []
sudeste = []
sul = []

for documento in resultados:
    
    if documento["Estado"] == "Pará (PA)" or documento["Estado"] == "Amazonas (AM)" or documento["Estado"] == "Amapá (AP)" or documento["Estado"] == "Roraima (RR)" or documento["Estado"] == "Acre (AC)" or documento["Estado"] == "Rondônia (RO)" or documento["Estado"] == "Tocantins (TO)":        
        norte.append(documento["Escola"])
    if documento["Estado"] == "Bahia (BA)" or documento["Estado"] == "Sergipe (SE)" or documento["Estado"] == "Alagoas (AL)" or documento["Estado"] == "Pernambuco (PE)" or documento["Estado"] == "Paraíba (PB)" or documento["Estado"] == "Rio Grande do Norte (RN)" or documento["Estado"] == "Ceará (CE)" or documento["Estado"] == "Piauí (PI)" or documento["Estado"] == "Maranhão (MA)":
        nordeste.append(documento["Escola"])
    if documento["Estado"] == "Mato Grosso (MT)" or documento["Estado"] == "Mato Grosso do Sul (MS)" or documento["Estado"] == "Goiás (GO)" or documento["Estado"] == "Distrito Federal (DF)":
        centro.append(documento["Escola"])
    if documento["Estado"] == "São Paulo (SP)" or documento["Estado"] == "Rio de Janeiro (RJ)" or documento["Estado"] == "Minas Gerais (MG)" or documento["Estado"] == "Espírito Santo (ES)":
        sudeste.append(documento["Escola"])
    if documento["Estado"] == "Rio Grande do Sul (RS)" or documento["Estado"] == "Santa Catarina (SC)" or documento["Estado"] == "Paraná (PR)":
        sul.append(documento["Escola"])

n = len(set(norte))
nor = len(set(nordeste))
ce = len(set(centro))
sude = len(set(sudeste))
sul = len(set(sul))
print(f"Norte {n}")
print(f"Nordeste {nor}")
print(f"centro {ce}")
print(f"sudeste {sude}")
print(f"sul {sul}")

print(n+nor+ce+sude+sul)
# Fechar a conexão
client.close()