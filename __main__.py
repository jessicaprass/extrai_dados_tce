# Programa __main__
# Requisitos: Este programa extrai um arquivo csv do Portal de Dados Abertos do TCE-RS e converte para arquivo xlsx.
# Autor: Jessica Prass
# Versão: 1.0.0
# Dados: 12/09/2022

import pandas as pd
import requests
import openpyxl


def main():
    endereco = "http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv"
    dados = requests.get(endereco, stream=True)

    arquivo = open("balancete.csv", "wb")

    for texto in dados.iter_content(1048576):
        arquivo.write(texto)
    arquivo.close()

    balancete = pd.read_csv("balancete.csv")
    balancete.to_excel("balancete.xlsx", index=False)

    novo_balancete = openpyxl.load_workbook("balancete.xlsx")

    novo_balancete.save("novo_balancete.xlsx")


if __name__ == "__main__":
    main()
