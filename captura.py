import cv2
import os
import time


def capturar_fotos(id_usuario):

    pasta = f"dataset/{id_usuario}"
    os.makedirs(pasta, exist_ok=True)

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():

        print("Erro ao abrir webcam.")
        return False

    detector = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    contador = 0
    ultimo_registro = time.time()

    print("Captura automática iniciada...")

    while contador < 20:

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

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            tempo_atual = time.time()

            if tempo_atual - ultimo_registro >= 1:

                rosto = frame[y:y+h, x:x+w]

                caminho = os.path.join(
                    pasta,
                    f"{contador}.jpg"
                )

                cv2.imwrite(
                    caminho,
                    rosto
                )

                contador += 1
                ultimo_registro = tempo_atual

                print(
                    f"Foto {contador}/20 capturada"
                )

        cv2.putText(
            frame,
            f"Fotos: {contador}/20",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Olhe para a camera",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        cv2.imshow(
            "Cadastro Facial",
            frame
        )

        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

    print(
        f"Captura finalizada. {contador} fotos salvas."
    )

    return contador >= 20