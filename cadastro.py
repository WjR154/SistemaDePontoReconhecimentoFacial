from captura import capturar_fotos
from treinamento import treinar_modelo
import os

def cadastrar_funcionario(codigo, nome):

    if os.path.exists("funcionarios.txt"):

        with open(
            "funcionarios.txt",
            "r",
            encoding="utf-8"
        ) as arquivo:

            for linha in arquivo:

                id_existente, _ = linha.strip().split(";")

                if id_existente == codigo:
                    return False

    with open(
        "funcionarios.txt",
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            f"{codigo};{nome}\n"
        )

    os.makedirs(
        f"dataset/{codigo}",
        exist_ok=True
    )

    sucesso = capturar_fotos(codigo)

    if sucesso:
        treinar_modelo()
        return True

    return False