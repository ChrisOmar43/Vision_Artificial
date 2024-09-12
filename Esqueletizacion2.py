# -- coding: utf-8 --
"""
Created on Tue Feb 27 08:02:33 2024

@author: JORGE AGUILAR


import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


with mp_pose.Pose(
    static_image_mode=False) as pose:
    cv2.VideoCapture

    image = cv2.imread("d:\imagenes\kungfu.jpg")
    height, width, _ = image.shape
    #Cambio de espacio de color a RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #Inicia proceso de reconocimiento de morfología
    results = pose.process(image_rgb)
    print("Pose landmarks:", results.pose_landmarks)
    #detección de marcas
    if results.pose_landmarks is not None:
        #print(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width))
        # x1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width)
        # y1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height)

        # x2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * width)
        # y2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * height)

        # x3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width)
        # y3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height)

        # x4 = int(results.pose_landmarks.landmark[11].x * width)
        # y4 = int(results.pose_landmarks.landmark[11].y * height)

        # x5 = int(results.pose_landmarks.landmark[13].x * width)
        # y5 = int(results.pose_landmarks.landmark[13].y * height)

        # x6 = int(results.pose_landmarks.landmark[15].x * width)
        # y6 = int(results.pose_landmarks.landmark[15].y * height)

        # cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
        # cv2.line(image, (x2, y2), (x3, y3), (0, 255, 0), 3)
        # cv2.circle(image, (x1, y1), 6, (128, 0, 255), -1)
        # cv2.circle(image, (x2, y2), 6, (128, 0, 255), -1)
        # cv2.circle(image, (x3, y3), 6, (128, 0, 255), -1)

        # cv2.line(image, (x4, y4), (x5, y5), (0, 255, 0), 3)
        # cv2.line(image, (x5, y5), (x6, y6), (0, 255, 0), 3)
        # cv2.circle(image, (x4, y4), 6, (255, 191, 0), -1)
        # cv2.circle(image, (x5, y5), 6, (255, 191, 0), -1)
        # cv2.circle(image, (x6, y6), 6, (255, 191, 0), -1)

        
        mp_drawing.draw_landmarks(image, results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3),
            mp_drawing.DrawingSpec(color=(0, 255,0 ), thickness=2))
        
    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands"""
import cv2
import mediapipe as mp
import math as mt

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=4,
    min_detection_confidence=0.5) as hands:

    cap = cv2.VideoCapture(1)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("No se puede acceder a la cámara")
            break

        image = cv2.flip(image, 1)
        height, width, _ = image.shape

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
                x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
                y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
    

                # coordenadas muñeca
                x6 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * width)
                y6 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * height)

                cv2.circle(image, (x1, y1), 3, (255, 0, 0), 3)
                cv2.circle(image, (x2, y2), 3, (255, 0, 0), 3)
                cv2.circle(image, (x6, y6), 3, (255, 0, 0), 3)

                # línea muñeca indice
                cv2.line(image, (x2, y2), (x6, y6), (255, 0, 0), 2)
                #Indice pulgar
                cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)
                #Pulgar muñeca
                cv2.line(image,(x1,y1),(x6,y6),(255,0,0),2)
                
                #indice pulgar
                l1 = mt.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
                #Indice muñeca
                l2 = mt.sqrt((x2 - x6) ** 2 + (y2 - y6) ** 2) 
                #Pulgar muñeca 
                l3 = mt.sqrt((x1 - x6) ** 2 + (y1 - y6) ** 2) 
                
                gama = ((l2)**2 + (l3)**2 - (l1)**2)/(2*l2*l3)
                gama = (mt.acos(gama))*180/3.14
                

                xm = int((x2 + x1) / 2)
                ym = int((y2 + y1) / 2)

                cv2.putText(image, "Pulgar", (x1 + 25, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "Indice", (x2 + 25, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "Muneca", (x6 + 25, y6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "c=" + str(round(l1, 2)), (xm + 25, ym), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
                cv2.putText(image, "a=" + str(round(l2, 2)), ((x2 + x6) // 2, (y2 + y6) // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
                cv2.putText(image, "b=" + str(round(l3, 2)), ((x1 + x6) // 2, (y1 + y6) // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
                cv2.putText(image, "Gama= " + str(gama), (x6 + 25,y6 + 27), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
                
                
        cv2.imshow("Marcas manuales", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()