# -- coding: utf-8 --
"""
Created on Wed Nov 15 19:05:32 2023

@author: JORGE AGUILAR
"""
import cv2
import mediapipe as mp
import math as mt

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=4,
    min_detection_confidence=0.5) as hands:

    cap = cv2.VideoCapture(0)

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
                x3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * width)
                y3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
                x4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * width)
                y4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
                x5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * width)
                y5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * height)

                # coordenadas muñeca
                x6 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * width)
                y6 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * height)

                cv2.circle(image, (x1, y1), 3, (255, 0, 0), 3)
                cv2.circle(image, (x2, y2), 3, (255, 0, 0), 3)
                cv2.circle(image, (x3, y3), 3, (255, 0, 0), 3)
                cv2.circle(image, (x4, y4), 3, (255, 0, 0), 3)
                cv2.circle(image, (x5, y5), 3, (255, 0, 0), 3)
                cv2.circle(image, (x6, y6), 3, (0, 255, 0), 3)

                # línea muñeca
                cv2.line(image, (x3, y3), (x6, y6), (0, 255, 0), 2)
                cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)
                
                l1 = mt.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
                l2 = mt.sqrt((x3 - x6) ** 2 + (y3 - y6) ** 2) 

                # Regla de tres
                l1_cm = (l1 / l2) * 17.5

                xm = int((x2 + x1) / 2)
                ym = int((y2 + y1) / 2)

                cv2.putText(image, "Pulgar", (x1 + 25, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "Indice", (x2 + 25, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "Medio", (x3 + 25, y3), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "Anular", (x4 + 25, y4), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "Menique", (x5 + 25, y5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "Muneca", (x6 + 25, y6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
                cv2.putText(image, "l=" + str(round(l1_cm, 2)) + " cm", (xm + 25, ym), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
                cv2.putText(image, "R=" + str(round(l2, 2)), ((x3 + x6) // 2, (y3 + y6) // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)

        cv2.imshow("Marcas manuales", image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()