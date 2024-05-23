import cv2

"""    #load
    image_path = "Images/Image.jpg"
    image1 = cv2.imread(image_path,1)
    image2 = cv2.imread(image_path,0)
    image3 = cv2.imread(image_path,-1)

    cv2.imshow('RGB', image1)
    cv2.imshow('Gray', image2)
    cv2.imshow('Original', image3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""
id = 0
cap = cv2.VideoCapture(id)

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        v_frame = cv2.flip(frame, 1)

        cv2.imshow('Vertical flip', v_frame)
        cv2.imshow('Original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
