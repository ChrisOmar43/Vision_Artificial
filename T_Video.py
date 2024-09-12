import cv2
import time

video_file = "C:/Users/chris/OneDrive/Desktop/VideoP.mp4"
cap = cv2.VideoCapture(video_file)
retraso = 0.1

# Propiedades del texto
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 0)  # Negro
thickness = 1

if cv2.__version__.startswith('2.4'):
    height_prop = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
    fps_prop = cv2.cv.CV_CAP_PROP_FPS
else:
    height_prop = cv2.CAP_PROP_FRAME_HEIGHT
    fps_prop = cv2.CAP_PROP_FPS

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Cambio a escala de grises
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Obtener altura del frame
        height = int(cap.get(height_prop))
        position_fps1 = (10, 30)  # Posición del texto de FPS en la primera línea
        position_fps2 = (10, 60)  # Posición del texto de FPS en la segunda línea
        position_frame = (10, 90) # Posición del texto del frame en reproducción
        
        # Retardo entre fotogramas
        time.sleep(retraso)  # 100 ms de retardo
        
        # Obtener FPS
        fps_og = cap.get(fps_prop)
        fps_new = 1 / ((1 / fps_og) + retraso)
        
        # Obtener número de frame actual
        frame_actual = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        
        # Colocar el texto de FPS en el frame
        cv2.putText(frame, f'FPS (original) {fps_og:.2f}', position_fps1, font, font_scale, color, thickness)
        cv2.putText(frame, f'FPS actuales {fps_new:.2f}', position_fps2, font, font_scale, color, thickness)
        cv2.putText(frame, f'Frame actual {frame_actual}', position_frame, font, font_scale, color, thickness)
        
        # Mostrar el video
        cv2.imshow("Video", frame)
        
        # Salir si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()