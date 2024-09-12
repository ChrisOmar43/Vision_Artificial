import cv2
import numpy as np

image_path="C:/Users/chris/OneDrive/Desktop/"
img=cv2.imread(image_path+'Captura.jpeg')
img=cv2.resize(img, [300,300])
ancho= img.shape[1]
alto= img.shape[0]
cv2.imshow("Imagen original",img)

#Traslacional
M=np.float32([[1,0,10],[0,1,100]])
img1=cv2.warpAffine(img,M,(ancho,alto))
cv2.imshow("Imagen traslacionada", img1)

#Rotacional
M2=cv2.getRotationMatrix2D((ancho//2, alto//2), 15,0.5)
img2=cv2.warpAffine(img,M2,(ancho,alto))
cv2.imshow("Imagen rotacional",img2)

#Escalar
img3=cv2.resize(img,(600,300),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Imagen Escalar",img3)

#Recortar una imagen
img4=img[120:270,50:350]
cv2.imshow("Imagen Recortada", img4)

cv2.waitKey(0)
cv2.destroyAllWindows()