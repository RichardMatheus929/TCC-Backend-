import pymongo
from collections import Counter
import re
import PyPDF2

urldomongo = (
    "mongodb+srv://richard_julia:ATALIBArm_2018@febracecluster.qme6nyb.mongodb.net/"
)

caminhodopdff = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2020/Finalistas/lista_finalistas_2020.pdf"

estados_do_brasil = ['Acre (AC)', 'Alagoas (AL)', 'Amapá (AP)', 'Amazonas (AM)', 'Bahia (BA)', 'Ceará (CE)', 'Distrito Federal (DF)', 'Espírito Santo (ES)', 'Goiás (GO)', 'Maranhão (MA)', 'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)', 'Minas Gerais (MG)', 'Pará (PA)', 'Paraíba (PB)', 'Paraná (PR)', 'Pernambuco (PE)', 'Piauí (PI)', 'Rio de Janeiro (RJ)', 'Rio Grande do Norte (RN)', 'Rio Grande do Sul (RS)', 'Rondônia (RO)', 'Roraima (RR)', 'Santa Catarina (SC)', 'São Paulo (SP)', 'Sergipe (SE)', 'Tocantins (TO)']


# Estabelecer uma conexão com o servidor MongoDB local
client = pymongo.MongoClient(urldomongo)

# Acessar um banco de dados e uma coleção
db = client["Database_Febrace"]
collection = db["tabela_premiados"]
resultados = collection.find({"Ano":"2020"})




contagem = 0




def divide_string(txt):

    tamanho = len(txt)

    if tamanho >= 150:
        div = txt[:tamanho//2//2//2]
    if tamanho >= 60 and tamanho < 150:
        div = txt[:tamanho//2//2]
    if tamanho < 60 and tamanho > 20:
        div = txt[:tamanho//2]
    if tamanho <= 20: 
        div = txt
    return div

def extract_pag(file_path):
    try:
        # Abre o arquivo PDF em modo de leitura binária
        with open(file_path, 'rb') as file:
            # Cria um objeto PdfReader para ler o PDF
            reader = PyPDF2.PdfReader(file)
            
            # Inicializa a string para armazenar o texto extraído
            text = []
            
            # Percorre todas as páginas do PDF
            for page_num in range(len(reader.pages)):
                 # Obtém o objeto Page da página atual
                page = reader.pages[page_num]
               
                
                # Extrai o texto da página preservando a estrutura original
                page_text = page.extract_text()
                pagsemlinhas = re.sub(r'^\s*\n', '',page_text, flags=re.MULTILINE)
                
                # Adiciona o texto da página à string final
                text.append(pagsemlinhas)
                
            return text
    except Exception as e:
        print(f"Ocorreu um erro ao extrair o texto do PDF: {str(e)}")

def dividir_linhas(text = ''):
    lines = text.splitlines()
    return lines

def encontrar_indice(lista, letras):
    for i, string in enumerate(lista):
        if letras in string:
            return i
    return -1


def orientador(nomeproj = ""):
    projmod = divide_string(nomeproj).strip().upper()
    orientador = "Campo não encontrado"
    componentes = 0
    linhaorientador = "Campo não encontrado"
    for paginas in range(len(textopag)):
        resposta = re.search(re.escape(projmod), textopag[paginas - 1])
        if resposta:
            paginaorientador = dividir_linhas(textopag[paginas-1]+textopag[paginas])
            for linha in range(len(paginaorientador)):
                resposta = re.search(re.escape(projmod),paginaorientador[linha])
                if resposta:
                    paginaorientador.append("Linha alternativa")
                    paginaorientador.append("Linha alternativa")
                    paginaorientador.append("Linha alternativa")
                    paginaorientador.append("Linha alternativa")
                    if "orientador" in paginaorientador[linha + 1].lower() or paginaorientador[linha + 1].count(",") >= 2:
                        if "orientador" in paginaorientador[linha + 2].lower():
                            linhaorientador = paginaorientador[linha + 1] + paginaorientador[linha + 2]
                        else:
                            linhaorientador = paginaorientador[linha + 1]
                    elif "orientador" in paginaorientador[linha + 2].lower() or paginaorientador[linha + 2].count(",") >= 2:
                        linhaorientador = paginaorientador[linha + 2]
                        if "orientador" in paginaorientador[linha + 3].lower():
                            linhaorientador = paginaorientador[linha + 2] + paginaorientador[linha + 3]
                    elif "orientador" in paginaorientador[linha + 3].lower() or paginaorientador[linha + 3].count(",") >= 2:
                        linhaorientador = paginaorientador[linha + 3]
                        if "orientador" in paginaorientador[linha + 4].lower():
                            linhaorientador = paginaorientador[linha + 3] + paginaorientador[linha + 4]

                    linhaorientadordiv = re.split(r",",linhaorientador)
                    contador = 0

                    for contorienta in linhaorientadordiv:
                        if "orientador" in contorienta.lower():
                            contador += 1
                    componentes = len(linhaorientadordiv) - contador
                    for procurar in linhaorientadordiv:
                        if "Orientador" in procurar:
                            orientador = procurar.replace("(Orientador)","").strip()

    if len(orientador) < 3:
        orientador = "Campo não encontrado"
        componentes = 0

    return orientador,componentes,linhaorientador

textopag = extract_pag(caminhodopdff)

for documento in resultados:

    dadosproj = orientador(documento["Nome_do_projeto"])

    collection.update_one({"_id": documento["_id"]}, {"$set": {"Orientador": dadosproj[0]}})
    collection.update_one({"_id": documento["_id"]}, {"$set": {"Componentes": dadosproj[1]}})
    collection.update_one({"_id": documento["_id"]}, {"$set": {"Integrantes": dadosproj[2]}})

        

print("EU SOU FODA")
# Fechar a conexão
client.close()
