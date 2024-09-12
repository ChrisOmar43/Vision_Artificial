import cv2
"""##Ejemplo1 Aritmatricas
image_path = 'C:/Users/chris/OneDrive/Desktop/'
img1=cv2.imread(image_path+'EscuelaAtenas.jpg')
img1=cv2.resize(img1,[600,600])
img2=cv2.imread(image_path+'Roma.jpeg')
img2=cv2.resize(img2,[600,600])
resta=cv2.subtract(img1, img2)
suma=cv2.add(img1,img2)
suma2=img1+img2
multi=cv2.multiply(img1, img2)
div=cv2.divide(img1,img2)
cv2.imshow("Imagen1",img2)
cv2.imshow("Imagen2",img1)
cv2.imshow("Resta",resta)
cv2.imshow("Suma",suma)
cv2.imshow("Multiplicacion",multi)
cv2.imshow("Division",div)

##Ejemplo2 Logicas
op_not=cv2.bitwise_not(img2)
op_and=cv2.bitwise_and(img2,img1)
op_or=cv2.bitwise_or(img2, img1)
op_and_same=cv2.bitwise_and(img2,img2)
cv2.imshow("OG1",img1)
cv2.imshow("OG2",img2)
cv2.imshow("OpNot",op_not)
cv2.imshow("OpAND",op_and)
cv2.imshow("OpOR",op_or)
cv2.imshow("MejoraAND",op_and_same)

##Ejemplo3 Geometricas
#Indicando el factor de escala
res = cv2.resize(img1,None, fx=2,fy=2, interpolation=cv2.INTER_CUBIC)
#Indicando mannualmente el nuevo tamaño deseado de la imagen
height, width = img1.shape[:2]
res2 = cv2.resize(img1,(int(2*width), int(2*height)), interpolation = cv2.INTER_CUBIC)

rows, cols = img1.shape[:2]
M = np.float32([[1,0,100],
                [0,1,50]])
dst = cv2.warpAffine(img1,M,(cols,rows))

M2=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst2 = cv2.warpAffine(img1, M2, (cols, rows))

cv2.imshow("OG",img1)
cv2.imshow("Escalado",dst2)

"""


cv2.waitKey(0)
cv2.destroyAllWindows() 