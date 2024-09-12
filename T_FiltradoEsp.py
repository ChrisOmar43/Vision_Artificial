"""
# Filtro de la media
mean_kernel = np.ones((5, 5), np.float32) / 25
mean_filtered_image = cv2.filter2D(image, -1, mean_kernel)

# Filtro Gaussiano
gaussian_filtered_image = cv2.GaussianBlur(image, (5, 5), 0)

# Filtro de mediana
median_filtered_image = cv2.medianBlur(image, 5)

# Filtro de Sobel
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)  # Gradiente en X
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)  # Gradiente en Y
sobel_combined = cv2.sqrt(cv2.add(cv2.pow(sobelx, 2), cv2.pow(sobely, 2)))

# Filtro Laplaciano
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Detector de bordes Canny
edges = cv2.Canny(image, 100, 200)"""
import cv2  # Biblioteca para procesamiento de imágenes
import numpy as np  # Biblioteca para operaciones matemáticas con matrices

image_path = "C:/Users/chris/OneDrive/Desktop/V.A./"

# Lee y redimensiona la imagen
imgMN = cv2.imread(image_path + 'captura.png')
imgMN = cv2.resize(img, [300, 300])

# Aplicación de filtros y detección de bordes
kernel_media = np.ones((5, 5), np.float32) / 25
img_media = cv2.filter2D(img, -1, kernel_media)
img_gaussiano = cv2.GaussianBlur(img, (5, 5), 0)
img_mediana = cv2.medianBlur(imgMN, 5)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
edges = cv2.Canny(img, 100, 200)

# Mostrar imágenes con diferentes filtros
cv2.imshow("Imagen original", img)
cv2.imshow("Imagen Media", img_media)
cv2.imshow("Imagen Gaussiano", img_gaussiano)
cv2.imshow("Imagen Mediana", img_mediana)
cv2.imshow("Imagen Sobel x", sobel_x)
cv2.imshow("Imagen Sobel y", sobel_y)
cv2.imshow("Imagen Laplaciano", laplacian)
cv2.imshow("Imagen Canny", edges)

# Esperar y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
#####################################
import cv2  # Biblioteca para procesamiento de imágenes
import numpy as np  # Biblioteca para operaciones matemáticas con matrices

image_path = "C:/Users/chris/OneDrive/Desktop/V.A./"

# Lee y redimensiona la imagen
img = cv2.imread(image_path + 'RG.png')
img = cv2.resize(img, [300, 300])

# Aplicación de filtros y detección de bordes
kernel_media = np.ones((5, 5), np.float32) / 25
img_media = cv2.filter2D(img, -1, kernel_media)
img_gaussiano = cv2.GaussianBlur(img, (5, 5), 0)
img_mediana = cv2.medianBlur(img, 5)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
edges = cv2.Canny(img, 100, 200)

# Mostrar imágenes con diferentes filtros
cv2.imshow("Imagen original", img)
cv2.imshow("Imagen Media", img_media)
cv2.imshow("Imagen Gaussiano", img_gaussiano)
cv2.imshow("Imagen Mediana", img_mediana)
cv2.imshow("Imagen Sobel x", sobel_x)
cv2.imshow("Imagen Sobel y", sobel_y)
cv2.imshow("Imagen Laplaciano", laplacian)
cv2.imshow("Imagen Canny", edges)

# Esperar y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
###################################################3
import numpy as np
import cv2

# Funciones para agregar ruido
def ruido_gaussiano(imagen, media=0, desviacion=25):

    imagen_con_ruido = imagen.copy()
    h, w, c = imagen_con_ruido.shape
    ruido = np.random.normal(media, desviacion, (h, w, c))
    imagen_con_ruido += ruido.astype(np.uint8)
    return imagen_con_ruido

def ruido_sal_y_pimienta(imagen, cantidad=0.02):
    imagen_con_ruido = imagen.copy()
    num_sal = np.ceil(cantidad * imagen.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_sal))
             for i in imagen.shape]
    imagen_con_ruido[coords[0], coords[1], :] = 255

    num_pimienta = np.ceil(cantidad * imagen.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_pimienta))
             for i in imagen.shape]
    imagen_con_ruido[coords[0], coords[1], :] = 0
    return imagen_con_ruido

def ruido_poisson(imagen):
    imagen_con_ruido = imagen.copy()
    imagen_con_ruido = np.random.poisson(imagen_con_ruido).astype('uint8')
    return imagen_con_ruido

# Funciones para aplicar filtros pasabajas
def filtro_media(imagen, tamano_kernel=3):
    imagen_filtrada = cv2.blur(imagen, (tamano_kernel, tamano_kernel))
    return imagen_filtrada

def filtro_gaussiano(imagen, tamano_kernel=5, sigma=0):
    imagen_filtrada = cv2.GaussianBlur(imagen, (tamano_kernel, tamano_kernel), sigma)
    return imagen_filtrada

def filtro_mediana(imagen, tamano_kernel=3):
    imagen_filtrada = cv2.medianBlur(imagen, tamano_kernel)
    return imagen_filtrada

# Imagen a manipular
imagen = cv2.imread('C:/Users/chris/OneDrive/Desktop/V.A./Roma.jpeg')

# Agregar diferentes tipos de ruido a la imagen original
imagen_con_ruido_gaussiano = ruido_gaussiano(imagen)
imagen_con_ruido_sal_pimienta = ruido_sal_y_pimienta(imagen)
imagen_con_ruido_poisson = ruido_poisson(imagen)

# Aplicar filtros pasabajas a cada imagen con ruido
imagen_filtrada_gaussiano_gaussiano5 = filtro_gaussiano(imagen_con_ruido_gaussiano)
imagen_filtrada_gaussiano_gaussiano3 = filtro_gaussiano(imagen_con_ruido_gaussiano,tamano_kernel=3)
imagen_filtrada_sal_pimienta_mediana = filtro_mediana(imagen_con_ruido_sal_pimienta)
imagen_filtrada_poisson_media = filtro_media(imagen_con_ruido_poisson)

# Mostrar imágenes resultantes (con y sin filtros)
cv2.imshow('Ruido Gaussiano', imagen_con_ruido_gaussiano)
cv2.imshow('Ruido Gaussiano Filtrado - FGaussiano5', imagen_filtrada_gaussiano_gaussiano5)
cv2.imshow('Ruido Gaussiano Filtrado - FGaussiano3', imagen_filtrada_gaussiano_gaussiano3)

cv2.imshow('Sal y Pimienta', imagen_con_ruido_sal_pimienta)
cv2.imshow('Sal y Pimienta Filtrado - Mediana', imagen_filtrada_sal_pimienta_mediana)

cv2.imshow('Ruido Poisson', imagen_con_ruido_poisson)
cv2.imshow('Poisson Filtrado - Media', imagen_filtrada_poisson_media)

cv2.waitKey(0)
cv2.destroyAllWindows()
##################
import cv2
import numpy as np

# Función para aplicar el filtro Sobel
def apply_sobel(image, dx=1, dy=1, ksize=3):
    """
    Aplica el filtro Sobel a la imagen para detectar bordes.
    
    Parámetros:
    - image: La imagen de entrada (en formato BGR).
    - dx: Orden de derivada en dirección X.
    - dy: Orden de derivada en dirección Y.
    - ksize: Tamaño del kernel Sobel (debe ser 1, 3, 5 o 7).
    
    Retorna:
    - La imagen con los bordes detectados por Sobel.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, dx, dy, ksize=ksize)
    sobely = cv2.Sobel(gray, cv2.CV_64F, dx, dy, ksize=ksize)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = np.uint8(sobel_combined)
    return sobel_combined

# Función para aplicar el filtro Laplaciano
def apply_laplacian(image):
    """
    Aplica el filtro Laplaciano a la imagen para detectar bordes.
    
    Parámetros:
    - image: La imagen de entrada (en formato BGR).
    
    Retorna:
    - La imagen con los bordes detectados por Laplaciano.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    return laplacian

# Función para aplicar el detector de bordes Canny
def apply_canny(image, threshold1=100, threshold2=200):
    """
    Aplica el detector de bordes Canny a la imagen.
    
    Parámetros:
    - image: La imagen de entrada (en formato BGR).
    - threshold1: Primer umbral para el detector de bordes.
    - threshold2: Segundo umbral para el detector de bordes.
    
    Retorna:
    - La imagen con los bordes detectados por Canny.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    return edges

# Ejemplo de uso
image_path = "C:/Users/chris/OneDrive/Desktop/V.A./"
img1 = cv2.imread(image_path + 'PP.png')
img2 = cv2.imread(image_path + 'OCR.png')
img3 = cv2.imread(image_path + 'PC.png')

# Aplicar filtros
sobel_image = apply_sobel(img1)
laplacian_image = apply_laplacian(img2)
canny_image = apply_canny(img3)

# Mostrar las imágenes resultantes (opcional)
cv2.imshow('Carretera', img1)
cv2.imshow('Documento', img2)
cv2.imshow('camara', img3)
cv2.imshow('Sobel Edges', sobel_image)
cv2.imshow('Laplacian Edges', laplacian_image)
cv2.imshow('Canny Edges', canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()