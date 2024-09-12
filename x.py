# -- coding: utf-8 --
"""
Created on Wed Nov 15 19:05:32 2023

@author: JORGE AGUILAR
"""
import cv2
import mediapipe as mp
import math as mt

mp_drawing = mp.solutions.drawing_utils #Herramienta que permite dibujar las detecciones solicitadas
mp_hands = mp.solutions.hands #Algoritmo que permite resolver la identificación de las manos

with mp_hands.Hands(
    #Configuración del modo de trabajo. True - Imagenes estáticas, False - Tiempo real
    static_image_mode=True, 
    #Cantidad máxima de manos detectadas simultaneamente
    max_num_hands=4,
    min_detection_confidence=0.5) as hands:

    image = cv2.imread("C:/Users/chris/OneDrive/Desktop/V.A/WIN_20240718_12_13_55_Pro.jpg")
    height, width, _ = image.shape

    image = cv2.flip(image, 1)
    image_rgb =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb) #Procesamos la imagen para la detección de manos
    print('Deteccion:', results.multi_handedness)
    
    # HAND LANDMARKS  - Algoritmo para la detección de los 21 puntos
    # Estos puntos estas identificados en decimales.
    #print('Puntos Obtenidos:', results.multi_hand_landmarks)
    
    #Identificamos si el algoritmo cuenta con los puntos de la mano
    if results.multi_hand_landmarks is not None:    
    # Accediendo a los puntos de referencia, de acuerdo a su nombre
        for hand_landmarks in   results.multi_hand_landmarks:
            #Mediante la multiplicación del ancho y alto de la imagen transformamos los decimales a escala de imagen
            
            x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width)
            y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
            x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
            y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)

            x3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * width)
            y3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)

            x4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * width)
            y4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * height)

            x5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * width)
            y5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * height)

            #Con los puntos adquiridos procedemos a dibujar circulos en las coordenadas obtenidas
            cv2.circle(image, (x1, y1), 3,(255,0,0),3)
            cv2.circle(image, (x2, y2), 3,(255,0,0),3)
            cv2.circle(image, (x3, y3), 3,(255,0,0),3)
            cv2.circle(image, (x4, y4), 3,(255,0,0),3)
            cv2.circle(image, (x5, y5), 3,(255,0,0),3)
            cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)
            l1=mt.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
            xm=int(x2-x1/2)
            ym=int(y2+y1/2)
            cv2.putText(image,"Pulgar",(x1+25,y1),cv2.FONT_HERSHEY_SIMPLEX,1,color=(0,0,255),thickness=4)
            cv2.putText(image,"Indice",(x2+25,y2),cv2.FONT_HERSHEY_SIMPLEX,1,color=(0,0,255),thickness=4)
            cv2.putText(image,"Medio",(x3+25,y3),cv2.FONT_HERSHEY_SIMPLEX,1,color=(0,0,255),thickness=4)
            cv2.putText(image,"Anular",(x4+25,y4),cv2.FONT_HERSHEY_SIMPLEX,1,color=(0,0,255),thickness=4)
            cv2.putText(image,"Menique",(x5+25,y5),cv2.FONT_HERSHEY_SIMPLEX,1,color=(0,0,255),thickness=4)
            cv2.putText(image,"l="+ str(l1),(xm+25,ym),cv2.FONT_HERSHEY_SIMPLEX,1,color=(0,0,255),thickness=4)
cv2.imshow("Marcas manuales",image)
cv2.waitKey(0)
cv2.destroyAllWindows()