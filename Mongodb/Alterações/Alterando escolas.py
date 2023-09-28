import pymongo
from collections import Counter
import re
import PyPDF2

urldomongo = (
    "mongodb+srv://richard_julia:ATALIBArm_2018@febracecluster.qme6nyb.mongodb.net/"
)

caminhodopdff = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2018/Finalistas/lista_finalistas_2018.pdf"

estados_do_brasil = ['Acre (AC)', 'Alagoas (AL)', 'Amapá (AP)', 'Amazonas (AM)', 'Bahia (BA)', 'Ceará (CE)', 'Distrito Federal (DF)', 'Espírito Santo (ES)', 'Goiás (GO)', 'Maranhão (MA)', 'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)', 'Minas Gerais (MG)', 'Pará (PA)', 'Paraíba (PB)', 'Paraná (PR)', 'Pernambuco (PE)', 'Piauí (PI)', 'Rio de Janeiro (RJ)', 'Rio Grande do Norte (RN)', 'Rio Grande do Sul (RS)', 'Rondônia (RO)', 'Roraima (RR)', 'Santa Catarina (SC)', 'São Paulo (SP)', 'Sergipe (SE)', 'Tocantins (TO)']


# Estabelecer uma conexão com o servidor MongoDB local
client = pymongo.MongoClient(urldomongo)

# Acessar um banco de dados e uma coleção
db = client["Database_Febrace"]
collection = db["tabela_premiados"]

resultados = collection.find({"Ano":"2023"})
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

def achar_escola_another(nome_do_projeto=""):
    if len(nome_do_projeto) > 3:
        
        primeiro_mod = nome_do_projeto.upper().strip()
        projpesquisa = divide_string(primeiro_mod)
        escola = ""
        texto_pag = extract_pag(caminhodopdff)
        texto_pag.append("Finja que isso é uma página")
        for paginas in range(len(texto_pag)):
            padrao = re.escape(projpesquisa)
            resposta = re.search(padrao, texto_pag[paginas-1])
            if resposta:
                paginaemlinhas = dividir_linhas(texto_pag[paginas-1] + texto_pag[paginas])
                for linhasdapagina in range(len(paginaemlinhas)):
                    if projpesquisa in paginaemlinhas[linhasdapagina]:
                        paginaemlinhas.append("Linha alternativa")
                        paginaemlinhas.append("Linha alternativa (02)")
                        paginaemlinhas.append("Linha alternativa (03)")
                        paginaemlinhas.append("Linha alternativa (04)")
                        if "(Orientador)" in paginaemlinhas[linhasdapagina + 1]:
                            if "(Coorientador)" in paginaemlinhas[linhasdapagina + 2]:
                                escola = paginaemlinhas[linhasdapagina + 3]
                            else:
                                escola = paginaemlinhas[linhasdapagina + 2]
                        if "(Orientador)" in paginaemlinhas[linhasdapagina + 2]:
                            if "(Coorientador)" in paginaemlinhas[linhasdapagina + 3]:
                                escola = paginaemlinhas[linhasdapagina + 4]
                            else:
                                escola = paginaemlinhas[linhasdapagina + 3]
                        if "(Orientador)" in paginaemlinhas[linhasdapagina + 3]:
                            escola = paginaemlinhas[linhasdapagina + 4]
                        if "(Orientador)" in paginaemlinhas[linhasdapagina + 4]:
                            escola = paginaemlinhas[linhasdapagina + 5]
    else:
        escola = " "
    return escola

for documento in resultados:

    collection.update_one({"_id": documento["_id"]}, {"$set": {"Orientador": "Nome do orientador"}})

        

print(contagem)
# Fechar a conexão
client.close()
