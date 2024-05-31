import cv2
import numpy as np

# Inicializar la captura de video
id = 0
captura = cv2.VideoCapture(id)

while captura.isOpened():

    ret, fotograma = captura.read()
    if ret == True:

        # Convertir de BGR a RGB
        fotograma_rgb = cv2.cvtColor(fotograma, cv2.COLOR_BGR2RGB)
        r, g, b = cv2.split(fotograma_rgb)
        black = np.zeros(fotograma.shape[:2],np.uint8)

        # Rotación horizontal
        fotograma_volteado_horizontal = cv2.flip(fotograma, 0)

        # Convertir la imagen con una rotación vertical y escala de grises
        fotograma_volteado_vertical_gris = cv2.cvtColor(cv2.flip(fotograma, 1), cv2.COLOR_BGR2GRAY)

        # Agregar texto a la imagen con rotación horizontal
        texto = "El video se encuentra de cabeza"
        fuente = cv2.FONT_ITALIC
        tamaño_letra = 1.2
        color_texto = (0, 255, 255)
        grosor_texto = 2
        opacidad = 0.6
        cv2.putText(fotograma_volteado_horizontal, texto, (10, 50), fuente, tamaño_letra, color_texto, grosor_texto)

        # Mostrar las imágenes
        cv2.imshow('Original', fotograma)
        cv2.imshow('Volteado Horizontal', fotograma_volteado_horizontal)
        cv2.imshow('Volteado Vertical en Gris', fotograma_volteado_vertical_gris)
        cv2.imshow('Canal R', cv2.merge([black, black, r]))
        cv2.imshow('Canal G', cv2.merge([black, g, black]))
        cv2.imshow('Canal B', cv2.merge([b, black, black]))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

captura.release()
cv2.destroyAllWindows()
#   By Christian Omar Silva Torres