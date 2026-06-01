from datetime import datetime
import cv2
import os


def carregar_funcionarios():

    funcionarios = {}

    if os.path.exists("funcionarios.txt"):

        with open(
                "funcionarios.txt",
                "r",
                encoding="utf-8"
        ) as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                if len(dados) < 2:
                    continue

                codigo = int(dados[0])
                nome = dados[1]

                funcionarios[codigo] = nome

    return funcionarios


def registrar_ponto(codigo, nome):

    os.makedirs(
        "registros",
        exist_ok=True
    )

    agora = datetime.now()

    with open(
            "registros/ponto.txt",
            "a",
            encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            f"{codigo};"
            f"{nome};"
            f"{agora.strftime('%d/%m/%Y')};"
            f"{agora.strftime('%H:%M:%S')}\n"
        )


def ponto_ja_registrado(codigo):

    caminho = "registros/ponto.txt"

    if not os.path.exists(caminho):
        return False

    hoje = datetime.now().strftime("%d/%m/%Y")

    with open(
            caminho,
            "r",
            encoding="utf-8"
    ) as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            if len(dados) < 4:
                continue

            if (
                    dados[0] == str(codigo)
                    and dados[2] == hoje
            ):
                return True

    return False


def reconhecer_usuario():

    if not os.path.exists("modelo/modelo.yml"):

        print("Modelo não encontrado.")
        return

    funcionarios = carregar_funcionarios()

    reconhecedor = cv2.face.LBPHFaceRecognizer_create()

    reconhecedor.read(
        "modelo/modelo.yml"
    )

    detector = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    camera = cv2.VideoCapture(0)

    codigo_reconhecido = None
    nome_reconhecido = None

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        cinza = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        rostos = detector.detectMultiScale(
            cinza,
            scaleFactor=1.2,
            minNeighbors=5
        )

        for (x, y, w, h) in rostos:

            face = cinza[y:y + h, x:x + w]

            id_usuario, confianca = reconhecedor.predict(face)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            if confianca < 70:

                nome = funcionarios.get(
                    id_usuario,
                    "Desconhecido"
                )

                codigo_reconhecido = id_usuario
                nome_reconhecido = nome

                cv2.putText(
                    frame,
                    f"Funcionario: {nome}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "ENTER = Confirmar Ponto",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    "ESC = Cancelar",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )

            else:

                cv2.putText(
                    frame,
                    "Desconhecido",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

        cv2.imshow(
            "Sistema de Ponto Facial",
            frame
        )

        tecla = cv2.waitKey(1)

        # ENTER
        if tecla == 13:

            if codigo_reconhecido is not None:

                if not ponto_ja_registrado(
                        codigo_reconhecido):

                    registrar_ponto(
                        codigo_reconhecido,
                        nome_reconhecido
                    )

                    print(
                        f"Ponto registrado para "
                        f"{nome_reconhecido}"
                    )

                else:

                    print(
                        f"{nome_reconhecido} "
                        f"ja registrou ponto hoje."
                    )

                break

        # ESC
        elif tecla == 27:
            break

    camera.release()
    cv2.destroyAllWindows()