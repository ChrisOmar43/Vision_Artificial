import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
###Primer tema de la clase
img_path = 'C:/Users/chris/OneDrive/Desktop/EscuelaAtenas.jpg'
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', img_gray)


#Ecuación de histograma
eq=cv2.equalizeHist(img_gray)
cv2.imshow('Ecualizado', eq)

#Calculo del histograma
org_hist=cv2.calcHist([img_gray], [0], None, [256], [0,256])
eq_hist=cv2.calcHist([eq], [0], None, [256], [0,256])

#Ploteamos el histograma original
plt.figure()
plt.xlabel('Bins')
plt.ylabel('Numero de Pixeles')
plt.plot(org_hist)
plt.grid()
plt.xlim([0,256])
plt.show()

#Ploteamos el histograma Ecualizado
plt.figure()
plt.xlabel('Bins')
plt.ylabel('Numero de Pixeles')
plt.plot(eq_hist)
plt.grid()
plt.xlim([0,256])
plt.show()

### Ejercicio
#Funcion de ploteo
def hist(ch, color):
    plt.figure()
    plt.figure(color)
    plt.xlabel('Bins')
    plt.ylabel(f'Numero de pixeles {color}')
    plt.plot(ch)
    plt.grid()
    plt.xlim([0,256])
    plt.show()

#Declaracion de imagen y separacion de canales
img_path = 'C:/Users/chris/OneDrive/Desktop/EscuelaAtenas.jpg'
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
red=img_rgb[:,:,0]
green=img_rgb[:,:,1]
blue=img_rgb[:,:,2]

#Ecualizando los Canales
blue_eq=cv2.equalizeHist(blue)
cv2.imshow('Azul Ecualizado', blue_eq)
green_eq=cv2.equalizeHist(green)
cv2.imshow('Verde Ecualizado', green_eq)
red_eq=cv2.equalizeHist(red)
cv2.imshow('Rojo Ecualizado', red_eq)

#Calculando los Histogramas
blue_hist=cv2.calcHist([blue],[0],None,[255],[0,255])
blue_Eq_hist=cv2.calcHist([blue_eq],[0],None,[255],[0,255])
green_hist=cv2.calcHist([green],[0],None,[255],[0,255])
green_Eq_hist=cv2.calcHist([green_eq],[0],None,[255],[0,255])
red_hist=cv2.calcHist([red],[0],None,[255],[0,255])
red_Eq_hist=cv2.calcHist([red_eq],[0],None,[255],[0,255])

#Ploteando los Histogramas
hist(blue_hist, 'Azules og')
hist(blue_Eq_hist, 'Azules eq')
hist(green_hist, 'Verdes og')
hist(green_Eq_hist, 'Verdes eq')
hist(red_hist, 'Rojos og')
hist(red_Eq_hist, 'Rojos eq')

#Haciendo merge y mostrandolo
cv2.imshow('Imagen Ecualizada', cv2.merge([blue_eq, green_eq, red_eq]))
cv2.imshow('Imagen', img)"""

###Tema dos de la Clase
img_path = "C:/Users/chris/OneDrive/Desktop/Radiografia.jpeg"
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', img_gray)
#Umbral para limitar el contraste
clip = 2.0

#Tamaño de la celda. El algoritmo dicidira las imagenes en seldas de tamaño (tile)
tile = 8
#Instanciamos el algoritmo CLAHE
clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(tile,tile))
#Ecualizamos la imagen
#Nota: Esta funcion solo opera sobre imagenes con un solo color
equalized = clahe.apply(img_gray)
#Mostramos el resultado
cv2.imshow('Ecualizada', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()