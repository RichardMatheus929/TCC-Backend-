import re
import textwrap
import PyPDF2
import pymongo as mongo
import fitz

# caminho do pdf que usa para chamar a função                                                                                                    
caminhodopdfP = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2023/Premiados/Premiados2023.pdf"
caminhodopdff = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2023/Finalistas/lista_finalistas_2023.pdf"
# url que o mongo dá para conseguir o acesso com o vs code
urldomongo = 'mongodb+srv://richard_julia:ATALIBArm_2018@febracecluster.qme6nyb.mongodb.net/'
# nome do database que eu criei e da colecao
nomedodatabase = 'teste'
nomedacolecao = '2023'
# conectando ao cluster
cluster = mongo.MongoClient(urldomongo)
# conectando ao database   por meio do cluster
database = cluster.get_database(nomedodatabase)
# conectando a colecao     por meio do database
colecao = database.get_collection(nomedacolecao)

estados_do_brasil = ['Acre (AC)', 'Alagoas (AL)', 'Amapá (AP)', 'Amazonas (AM)', 'Bahia (BA)', 'Ceará (CE)', 'Distrito Federal (DF)', 'Espírito Santo (ES)', 'Goiás (GO)', 'Maranhão (MA)', 'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)', 'Minas Gerais (MG)', 'Pará (PA)', 'Paraíba (PB)', 'Paraná (PR)', 'Pernambuco (PE)', 'Piauí (PI)', 'Rio de Janeiro (RJ)', 'Rio Grande do Norte (RN)', 'Rio Grande do Sul (RS)', 'Rondônia (RO)', 'Roraima (RR)', 'Santa Catarina (SC)', 'São Paulo (SP)', 'Sergipe (SE)', 'Tocantins (TO)']


# função que extrai o texto completo
def pdf_full(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        page_text = page.get_text()
        text += page_text

    return text

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

# função que divide a string em parágrafos
def dividir_paragrafos(text):
    paragraphs = textwrap.dedent(text).strip().split('\n\n')
    return paragraphs

# função que divide a string emc linhas
def dividir_linhas(text = ''):
    lines = text.splitlines()
    return lines

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

def encontrar_indice(lista, letras):
    for i, string in enumerate(lista):
        if letras in string:
            return i
    return -1

def remover_espacos_extras(string):
    palavras = string.split()
    string_sem_espacos_extras = ' '.join(palavras)
    return string_sem_espacos_extras

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
                        if "(Orientação)" in paginaemlinhas[linhasdapagina + 1]:
                            if "(Coorientação)" in paginaemlinhas[linhasdapagina + 2]:
                                escola = paginaemlinhas[linhasdapagina + 3]
                            else:
                                escola = paginaemlinhas[linhasdapagina + 2]
                        if "(Orientação)" in paginaemlinhas[linhasdapagina + 2]:
                            if "(Coorientação)" in paginaemlinhas[linhasdapagina + 3]:
                                escola = paginaemlinhas[linhasdapagina + 4]
                            else:
                                escola = paginaemlinhas[linhasdapagina + 3]
                        if "(Orientação)" in paginaemlinhas[linhasdapagina + 3]:
                            escola = paginaemlinhas[linhasdapagina + 4]
                        if "(Orientação)" in paginaemlinhas[linhasdapagina + 4]:
                            escola = paginaemlinhas[linhasdapagina + 5]
    else:
        escola = " "
    return escola

# extrai texto completo do pdf dos premiados
premiadosfull = pdf_full(caminhodopdfP)
# dividi o texto completo do pdf premiados em linhas
linhas = dividir_linhas(premiadosfull)

for contagem in range(len(linhas)):

    cpremiacao = ""
    nomeprojeto = ""
    escola = ""
    participantes = ""

    if "PRÊMIO]" in linhas[contagem]:
        vartempo = linhas[contagem+1]

    if "1° lugar" == linhas[contagem].lower():
        vartempo = vartempo + " " + linhas[contagem]
    if "2° lugar" == linhas[contagem].lower():
        vartempo = vartempo + " " + linhas[contagem]
    if "3° lugar" == linhas[contagem].lower():
        vartempo = vartempo + " " + linhas[contagem]
        
    if "[ PROJETO:" in linhas[contagem]:
        if "]" in linhas[contagem]:
           nomeprojeto = linhas[contagem]
        elif "]" in linhas[contagem+1]:
            nomeprojeto = linhas[contagem] + " " + linhas[contagem+1]
        elif "]" in linhas[contagem+2]:
            nomeprojeto = linhas[contagem] + " " + linhas[contagem+1]+ " " + linhas[contagem+2]
        elif "]" in linhas[contagem+3]:
            nomeprojeto = linhas[contagem] + " " + linhas[contagem+1] + " "+ linhas[contagem+2]+ " "+ linhas[contagem+3]
        
        cpremiacao = vartempo


    projeto = remover_espacos_extras(nomeprojeto).replace("[ PROJETO: ", "").replace("]", "")
    nameescola = achar_escola_another(projeto)

    if len(nomeprojeto)!= 0:
        if nameescola.count(",") <= 1:
            nameescola = "Campo não encontrado"
            namecidade = "Campo não encontrado"
            nameestado = "Campo não encontrado"
        else:
            lista_substrings = re.split(r",", nameescola)
            qualestado = encontrar_indice(estados_do_brasil,lista_substrings[2].strip())    
            nameescola = lista_substrings[0]
            namecidade = lista_substrings[1].title()
            nameestado = estados_do_brasil[qualestado]
            
        
        dadoum = {

        "Categoria_de_premiação":cpremiacao,
        "Nome_do_projeto": projeto,
        "Escola" : nameescola,
        "Cidade": namecidade,
        "Estado": nameestado,
        "Ano" : '2023'
        }
        colecao.insert_one(dadoum)

print("Finalizado")