import cv2
import numpy as np

# Paths
images_paths = ['C:/Users/chris/OneDrive/Desktop/Robot.jpg',
                'C:/Users/chris/OneDrive/Desktop/EscuelaAtenas.jpg',
                'C:/Users/chris/OneDrive/Desktop/Roma.jpeg']

#Lectura de imagenes
image1 = cv2.imread(images_paths[0], -1) #Original
image2 = cv2.imread(images_paths[1], 1) 
image3 = cv2.imread(images_paths[2], 0) #Gris

#Capa de negro
black = np.zeros(image2.shape[:2],np.uint8)

#RGB
image2RGB = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(image2RGB)

#Mostrar imagenes
cv2.imshow('Imagen 1 (Original)',image1)
cv2.imshow('Imagen 2 canal R', cv2.merge([black, black, r]))
cv2.imshow('Imagen 2 canal G', cv2.merge([black, g, black]))
cv2.imshow('Imagen 2 canal B', cv2.merge([b, black, black]))
cv2.imshow('Imagen 3 (Escala de Grises)', image3)

cv2.waitKey(0)
cv2.destroyAllWindows()
