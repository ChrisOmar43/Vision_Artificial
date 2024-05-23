import cv2

imagesRGB = []
imagesGr = []
imagesOg = []

# Load images
images_paths = ['C:/Users/chris/OneDrive/Desktop/Robot.jpg',
                'C:/Users/chris/OneDrive/Desktop/Roma.jpeg',
                'C:/Users/chris/OneDrive/Desktop/EscuelaAtenas.jpg']

for i in range(3):
    imagesRGB.append(cv2.imread(images_paths[i], 1))
    imagesGr.append(cv2.imread(images_paths[i], 0))
    imagesOg.append(cv2.imread(images_paths[i], -1))

    cv2.imshow(f'RGB {i}', imagesRGB[i])
    cv2.imshow(f'Gray {i}', imagesGr[i])
    cv2.imshow(f'Original {i}', imagesOg[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
