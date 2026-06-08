from captura import capturar_fotos
from treinamento import treinar_modelo
import os


def gerar_proximo_id():

    if not os.path.exists("funcionarios.txt"):
        return 1

    ultimo_id = 0

    with open(
            "funcionarios.txt",
            "r",
            encoding="utf-8"
    ) as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            if len(dados) < 2:
                continue

            try:

                id_atual = int(dados[0])

                if id_atual > ultimo_id:
                    ultimo_id = id_atual

            except ValueError:
                continue

    return ultimo_id + 1


def cadastrar_funcionario(nome):

    codigo = gerar_proximo_id()

    pasta = f"dataset/{codigo}"

    os.makedirs(
        pasta,
        exist_ok=True
    )

    with open(
            "funcionarios.txt",
            "a",
            encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            f"{codigo};{nome}\n"
        )

    print("=" * 50)
    print(f"Funcionário: {nome}")
    print(f"ID gerado: {codigo}")
    print(f"Pasta criada: {os.path.abspath(pasta)}")
    print("=" * 50)

    sucesso = capturar_fotos(codigo)

    if sucesso:

        print("Treinando modelo...")

        treinar_modelo()

        print("Treinamento concluído.")

        return codigo

    print("Captura cancelada.")

    return None