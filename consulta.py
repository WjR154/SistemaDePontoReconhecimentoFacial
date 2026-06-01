import os


def consultar_registros():

    caminho = "registros/ponto.txt"

    if not os.path.exists(caminho):
        return "Nenhum registro encontrado."

    with open(
            caminho,
            "r",
            encoding="utf-8"
    ) as arquivo:

        return arquivo.read()