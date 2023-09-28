import fitz


def pdf_full(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        page_text = page.get_text()
        text += page_text

    return text

def dividir_linhas(text = ''):
    lines = text.splitlines()
    return lines

caminhodopdfP = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2019/Premiados/Premiados2019.pdf"
projetosteste = []
premiosteste = []

# extrai texto completo do pdf dos premiados
premiadosfull = pdf_full(caminhodopdfP)
# dividi o texto completo do pdf premiados em linhas
linhas = dividir_linhas(premiadosfull)

for contagem in range(len(linhas)):

    cpremiacao = 'COm alguma coisa'
    nomeprojeto = ''

    if "PRÊMIO]" in linhas[contagem]:
        vartempo = linhas[contagem+1]


    if "[PROJETO:" in linhas[contagem]:
        if "]" in linhas[contagem]:
           nomeprojeto = linhas[contagem]
        elif "]" in linhas[contagem+1]:
            nomeprojeto = linhas[contagem] + " " + linhas[contagem+1]
        elif "]" in linhas[contagem+2]:
            nomeprojeto = linhas[contagem] + " " + linhas[contagem+1]+ " " + linhas[contagem+2]
        elif "]" in linhas[contagem+3]:
            nomeprojeto = linhas[contagem] + " " + linhas[contagem+1] + " "+ linhas[contagem+2]+ " "+ linhas[contagem+3]

        cpremiacao = vartempo


    if len(cpremiacao) != 0 and len(nomeprojeto)!= 0:
        projetosteste.append(nomeprojeto)
        premiosteste.append(cpremiacao)



for i in range(len(projetosteste)):
    print(projetosteste[i])
    print(premiosteste[i])
    print("---------------------------------")

