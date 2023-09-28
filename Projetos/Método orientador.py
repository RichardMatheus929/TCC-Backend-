import re
import PyPDF2


def dividir_linhas(text=""):
    lines = text.splitlines()
    return lines


def extract_pag(file_path):
    try:
        # Abre o arquivo PDF em modo de leitura binária
        with open(file_path, "rb") as file:
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
                pagsemlinhas = re.sub(r"^\s*\n", "", page_text, flags=re.MULTILINE)

                # Adiciona o texto da página à string final
                text.append(pagsemlinhas)

            return text
    except Exception as e:
        print(f"Ocorreu um erro ao extrair o texto do PDF: {str(e)}")


def divide_string(txt):
    tamanho = len(txt)

    if tamanho >= 150:
        div = txt[: tamanho // 2 // 2 // 2]
    if tamanho >= 60 and tamanho < 150:
        div = txt[: tamanho // 2 // 2]
    if tamanho < 60 and tamanho > 20:
        div = txt[: tamanho // 2]
    if tamanho <= 20:
        div = txt
    return div

def achar_escola_another(nome_do_projeto=""):
    if len(nome_do_projeto) > 3:
        primeiro_mod = nome_do_projeto.upper().strip()
        projpesquisa = divide_string(primeiro_mod)
        escola = ""
        texto_pag = extract_pag(caminhodopdff)
        for paginas in range(len(texto_pag)):
            padrao = re.escape(projpesquisa)
            resposta = re.search(padrao, texto_pag[paginas - 1])
            if resposta:
                paginaemlinhas = dividir_linhas(
                    texto_pag[paginas - 1] + texto_pag[paginas]
                )
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

                            if "publicado" in paginaemlinhas[linhasdapagina + 2].lower():
                                escola = paginaemlinhas[linhasdapagina + 3]
                        if "(Orientador)" in paginaemlinhas[linhasdapagina + 2]:
                            if "(Coorientador)" in paginaemlinhas[linhasdapagina + 3]:
                                escola = paginaemlinhas[linhasdapagina + 4]
                            else:
                                escola = paginaemlinhas[linhasdapagina + 3]
                            
                            if "publicado" in paginaemlinhas[linhasdapagina + 3].lower():
                                escola = paginaemlinhas[linhasdapagina + 4]
                        if "(Orientador)" in paginaemlinhas[linhasdapagina + 3]:
                            escola = paginaemlinhas[linhasdapagina + 4]
                        if "(Orientador)" in paginaemlinhas[linhasdapagina + 4]:
                            escola = paginaemlinhas[linhasdapagina + 5]

                        
    else:
        escola = " "
    return escola

def remover_espacos_extras(string):
    palavras = string.split()
    string_sem_espacos_extras = ' '.join(palavras)
    return string_sem_espacos_extras

caminhodopdff = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2023/Finalistas/lista_finalistas_2023.pdf"

textopag = extract_pag(caminhodopdff)


def orientador(nomeproj = ""):
    projmod = divide_string(nomeproj).strip().upper()
    for paginas in range(len(textopag)):
        resposta = re.search(re.escape(projmod), textopag[paginas - 1])
        if resposta:
            paginaorientador = dividir_linhas(textopag[paginas-1]+textopag[paginas])
            for linha in range(len(paginaorientador)):
                resposta = re.search(re.escape(projmod),paginaorientador[linha])
                if resposta:
                    if "orientação" in paginaorientador[linha + 1].lower() or paginaorientador[linha + 1].count(",") >= 2:
                        if "orientação" in paginaorientador[linha + 2].lower():
                            linhaorientador = paginaorientador[linha + 1] + paginaorientador[linha + 2]
                        else:
                            linhaorientador = paginaorientador[linha + 1]
                    elif "orientação" in paginaorientador[linha + 2].lower() or paginaorientador[linha + 2].count(",") >= 2:
                        linhaorientador = paginaorientador[linha + 2]
                        if "orientação" in paginaorientador[linha + 3].lower():
                            linhaorientador = paginaorientador[linha + 2] + paginaorientador[linha + 3]
                    elif "orientação" in paginaorientador[linha + 3].lower() or paginaorientador[linha + 3].count(",") >= 2:
                        linhaorientador = paginaorientador[linha + 3]
                        if "orientação" in paginaorientador[linha + 4].lower():
                            linhaorientador = paginaorientador[linha + 3] + paginaorientador[linha + 4]

                    linhaorientadordiv = re.split(r",",linhaorientador)
                    contador = 0

                    for contorienta in linhaorientadordiv:
                        if "orientação" in contorienta.lower():
                            contador += 1
                    componentes = len(linhaorientadordiv) - contador
                    for procurar in linhaorientadordiv:
                        if "Orientação" in procurar:
                            orientador = procurar.replace("(Orientação)","").strip()

    if len(orientador) < 3:
        orientador = "Campo não encontrado"
        componentes = 0

    return orientador,componentes,linhaorientador



nameprojeto = "Evasão escolar e a desumanização: um estudo à luz do pensamento de Paulo Freire "
print(orientador(nameprojeto))
