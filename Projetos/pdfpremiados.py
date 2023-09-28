import fitz

caminhodopdfP = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2018/Premiados/Premiados2018.pdf"
caminhodopdfPdois = f"C:/Users/richa/Desktop/Programação/Josenalde/Febrace/2021/Premiados/Premiacao-FEBRACE-2023_Parte-2.pdf"


# função que extrai o texto completo
def pdf_full(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        page_text = page.get_text()
        text += page_text

    return text


premiadosfull = pdf_full(caminhodopdfP)
print(premiadosfull)
