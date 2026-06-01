def consultar_registros():

    try:
        with open("ponto.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except FileNotFoundError:
        return "Nenhum registro encontrado."