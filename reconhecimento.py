from datetime import datetime
import cv2


def registrar_ponto(codigo, nome):

    agora = datetime.now()

    with open("ponto.txt", "a", encoding="utf-8") as arquivo:

        arquivo.write(
            f"{codigo};"
            f"{nome};"
            f"{agora.strftime('%d/%m/%Y')};"
            f"{agora.strftime('%H:%M:%S')}\n"
        )

def reconhecer_usuario():

    print("Abrindo webcam...")

    camera = cv2.VideoCapture(0)

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        cv2.imshow(
            "Reconhecimento Facial",
            frame
        )

        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()