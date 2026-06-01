import cv2
import os

def capturar_fotos(id_usuario):

    pasta = f"dataset/{id_usuario}"
    os.makedirs(pasta, exist_ok=True)

    camera = cv2.VideoCapture(0)

    contador = 0

    print("\nCOMANDOS:")
    print("C = Capturar foto")
    print("ESC = Sair\n")

    while True:

        ret, frame = camera.read()

        if not ret:
            print("Erro ao acessar a webcam.")
            break

        texto = f"Fotos capturadas: {contador}/20"

        cv2.putText(
            frame,
            texto,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Captura Facial", frame)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord('c'):

            caminho = os.path.join(pasta, f"{contador}.jpg")

            if cv2.imwrite(caminho, frame):
                contador += 1
                print(f"Foto {contador} salva")

            if contador >= 20:
                break

        elif tecla == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

    return contador >= 20