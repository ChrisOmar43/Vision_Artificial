import cv2
import numpy as np
import time

"""
# Load images
image_path = 'C:/Users/chris/OneDrive/Desktop/Roma.jpeg'
image1 = cv2.imread(image_path, 1)
img_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
red = img_rgb[:,:,0]
green = img_rgb[:,:,1]
blue = img_rgb[:,:,2]
black = np.zeros(image1.shape[:2],np.uint8)
cv2.imshow('Rojo', cv2.merge([black, black, red]))
cv2.imshow('Azul', cv2.merge([blue, black, black]))
cv2.imshow('Verde', cv2.merge([black, green, black]))

id = 0
cap = cv2.VideoCapture(id)

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:
        
        black = np.zeros(frame.shape[:2],np.uint8)
        frames_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        r,g,b = cv2.split(frames_rgb)
        cv2.imshow('Rojo', cv2.merge([black, black, r]))
        cv2.imshow('Azul', cv2.merge([b, black, black]))
        cv2.imshow('Verde', cv2.merge([black, g, black]))
        cv2.imshow('Original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
"""
video_file = "C:/Users/chris/OneDrive/Desktop/VideoP.mp4"
cap = cv2.VideoCapture(video_file)


#Text Propieries
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1 
color = (0,0,0)
thickness = 1

if cv2.__version__.startswith('2.4'):
    height_prop = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
    fps_prop = cv2.cv.CV_CAP_PROP_FPS
else:
    height_prop = cv2.CAP_PROP_FRAME_HEIGHT
    fps_prop = cv2.CAP_PROP_FPS

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        #Cambio a Escala de Grises
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Text position
        height = int(cap.get(height_prop))
        position = (0, height - 808)
        
        #Frames per second
        fps = "{0:.2f}".format(cap.get(fps_prop))
        text = "FPS: " + fps
        
        #Put text
        cv2.putText(frame, text, position, font, font_scale, color, thickness)
        
        #Display
        cv2.imshow("Video", frame)
        time.sleep(30/1000)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        

cv2.destroyAllWindows()
