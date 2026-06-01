from captura import capturar_fotos
from treinamento import treinar_modelo
import os

def cadastrar_funcionario(codigo, nome):

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

    return sucesso  