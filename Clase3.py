"""Clase
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = 'C:/Users/chris/OneDrive/Desktop/EscuelaAtenas.jpg'
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
red=img_rgb[:,:,0]
green=img_rgb[:,:,1]
blue=img_rgb[:,:,2]

blue_hist=cv2.calcHist([blue],[0],None,[255],[0,255])
green_hist=cv2.calcHist([green],[0],None,[255],[0,255])
red_hist=cv2.calcHist([red],[0],None,[255],[0,255])

def hist(ch, color):
    plt.figure()
    plt.figure(color)
    plt.xlabel('Bins')
    plt.ylabel(f'Numero de pixeles {color}')
    plt.plot(ch)
    plt.grid()
    plt.xlim([0,256])
    plt.show()
    
hist(blue_hist, 'Azules')
hist(green_hist, 'Verdes')
hist(red_hist, 'Rojos')

cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#Ejercicio

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular y mostrar el histograma de un canal de color
def hist(ch, color, img_name):
    plt.figure()
    plt.title(f'Histograma de {color} - {img_name}')
    plt.xlabel('Bins')
    plt.ylabel(f'Número de píxeles {color}')
    plt.plot(ch, color=color)
    plt.grid()
    plt.xlim([0, 256])
    plt.show()

# Rutas de las imágenes
images_paths = [
    'C:/Users/chris/OneDrive/Desktop/Robot.jpg',
    'C:/Users/chris/OneDrive/Desktop/Roma.jpeg',
    'C:/Users/chris/OneDrive/Desktop/EscuelaAtenas.jpg'
]

# Listas para almacenar las imágenes y sus versiones en RGB
imagesRGB = []

# Cargar y procesar cada imagen
for img_path in images_paths:
    # Leer imagen en BGR
    img = cv2.imread(img_path)
    
    # Convertir a RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imagesRGB.append(img_rgb)

    # Separar canales de color
    red = img_rgb[:,:,0]
    green = img_rgb[:,:,1]
    blue = img_rgb[:,:,2]

    # Calcular histogramas
    blue_hist = cv2.calcHist([blue], [0], None, [256], [0, 256])
    green_hist = cv2.calcHist([green], [0], None, [256], [0, 256])
    red_hist = cv2.calcHist([red], [0], None, [256], [0, 256])

    # Mostrar histogramas
    img_name = img_path.split('/')[-1]  # Obtener el nombre de la imagen para los títulos
    hist(blue_hist, 'blue', img_name)
    hist(green_hist, 'green', img_name)
    hist(red_hist, 'red', img_name)

    # Mostrar imagen
    cv2.imshow(f'Imagen RGB - {img_name}', img)

cv2.waitKey(0)
cv2.destroyAllWindows()