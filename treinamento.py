import cv2
import os
import numpy as np

def treinar_modelo():

    caminho_dataset = "dataset"

    faces = []
    ids = []

    detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    for id_usuario in os.listdir(caminho_dataset):

        pasta_usuario = os.path.join(caminho_dataset, id_usuario)

        if not os.path.isdir(pasta_usuario):
            continue

        for imagem_nome in os.listdir(pasta_usuario):

            caminho_imagem = os.path.join(
                pasta_usuario,
                imagem_nome
            )

            imagem = cv2.imread(caminho_imagem)

            if imagem is None:
                continue

            cinza = cv2.cvtColor(
                imagem,
                cv2.COLOR_BGR2GRAY
            )

            rostos = detector.detectMultiScale(
                cinza,
                scaleFactor=1.2,
                minNeighbors=5
            )

            for (x, y, w, h) in rostos:

                face = cinza[y:y+h, x:x+w]

                faces.append(face)
                ids.append(int(id_usuario))

    if len(faces) == 0:
        return False

    reconhecedor = cv2.face.LBPHFaceRecognizer_create()

    reconhecedor.train(
        faces,
        np.array(ids)
    )

    os.makedirs("modelo", exist_ok=True)

    reconhecedor.save(
        "modelo/modelo.yml"
    )

    return True