from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime


def gerar_pdf(servidor, monitor, alunos, data, horario):
    # Nome do arquivo
    nome_pdf = f"Autorizacao_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.pdf"

    # Documento
    doc = SimpleDocTemplate(nome_pdf)
    styles = getSampleStyleSheet()
    elementos = []

    # Cabeçalho
    elementos.append(Paragraph("<b>IFCIENCIA PODCAST - PVA</b>", styles["Title"]))
    elementos.append(Spacer(1, 20))

    # Texto principal
    texto = (
        f"Por meio desta, o <b>IFCIENCIA PODCAST - PVA</b> solicita que o(s) aluno(s) "
        f"abaixo relacionados fiquem fora de sala no dia <b>{data}</b>, durante o período "
        f"<b>{horario}</b>, para atividades a pedido do monitor <b>{monitor}</b> "
        f"e sob autorização do servidor responsável pelo IFCIENCIA PODCAST, "
        f"<b>{servidor}</b>."
    )

    elementos.append(Paragraph(texto, styles["BodyText"]))
    elementos.append(Spacer(1, 20))

    
    #Tabela
    dados_tabela = [["Nº", "Nome do Aluno"]]

    for i, aluno in enumerate(alunos, start=1):
        dados_tabela.append([str(i), aluno])

    tabela = Table(dados_tabela, colWidths=[45, 420])

    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 1), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),

        ("ALIGN", (1, 1), (1, -1), "LEFT"),
    ]))

    elementos.append(tabela)

    elementos.append(Spacer(1, 35))

    # Campo para data
    elementos.append(
        Paragraph("Data: ____/____/________", styles["BodyText"])
    )

    elementos.append(Spacer(1, 45))

    # Assinaturas
    elementos.append(
        Paragraph(
            "Monitor: _________________________________________________",
            styles["BodyText"]
        )
    )

    elementos.append(Spacer(1, 25))

    elementos.append(
        Paragraph(
            "Servidor Responsável: _____________________________________",
            styles["BodyText"]
        )
    )

    # Geração do PDF
    doc.build(elementos)

    print(f"\nPDF gerado com sucesso: {nome_pdf}\n")


#programa

while True:
    servidor = input("Digite o nome do Servidor Responsável >>> ")
    monitor = input("Digite o nome do Monitor Solicitante >>> ")

    quantidade = int(input("Quantos alunos serão solicitados? "))

    alunos = []

    for i in range(quantidade):
        aluno = input(f"Digite o nome do {i + 1}º aluno >>> ")
        alunos.append(aluno)

    data = input("Digite a data que o(s) aluno(s) está(ão) sendo solicitado(s) >>> ")
    horario = input("Digite o período que o(s) aluno(s) ficarão fora de sala >>> ")

    input("\nAperte ENTER para gerar a autorização...")

    gerar_pdf(servidor, monitor, alunos, data, horario)

    continuar = input("\nDeseja gerar outra autorização? (S/N): ").strip().upper()

    if continuar != "S":
        print("\nPrograma encerrado.")
        break