import pymongo

urldomongo = 'mongodb+srv://richard_julia:ATALIBArm_2018@febracecluster.qme6nyb.mongodb.net/'

# Estabelecer uma conexão com o servidor MongoDB local
client = pymongo.MongoClient(urldomongo)

# Acessar um banco de dados e uma coleção
db = client["Database_Febrace"]
collection = db["tabela_premiados"]

# Definir o filtro para encontrar os documentos que devem ser excluídos
filtro = {"Ano": "2021"}

# Excluir os documentos que correspondem ao filtro
resultado = collection.delete_many(filtro)

# Exibir o número de documentos excluídos
print(f"Foram excluídos {resultado.deleted_count} documentos com Ano igual a '2021'.")

# Fechar a conexão
client.close()