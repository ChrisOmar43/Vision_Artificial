import cv2
import numpy as np
"""
filename = 'C:/Users/chris/OneDrive/Desktop/Ajedrez.jpg'
img = cv2.imread(filename)

#RGB -> Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Input image shoud be grayscale and float32 type
gray = np.float32(gray)

#Corner detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k= 0.04)

#Threshold for an optimal calue, it may vany depending
#img[dst>0.01*dis.max()]=[0,255,0]
height, width = dst.shape
color = (0,255,0)

for y in range(0,height):
    for x in range (0, width):
        if dst.item(y,x) > 0.01*dst.max():
            cv2.circle(img, (x,y), 3, color, cv2.FILLED, cv2.LINE_AA)
            
cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()"""
import cv2
import numpy as np

camera_id = 0
cap = cv2.VideoCapture(camera_id)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Convertir RGB a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # La imagen de entrada debe ser de tipo float32
        gray = np.float32(gray)
        
        # Detección de esquinas
        dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
        
        # Aplicar un umbral a dst y marcar las esquinas detectadas en la imagen original
        frame[dst > 0.01 * dst.max()] = [0, 255, 0]

        cv2.imshow('dst', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()