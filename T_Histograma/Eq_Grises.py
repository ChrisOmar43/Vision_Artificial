import cv2
from matplotlib import pyplot as plt

# Funcion de ploteo
def hist(ch, color, title):
    plt.figure()
    plt.title(title)
    plt.xlabel('Bins')
    plt.ylabel(f'Numero de pixeles {color}')
    plt.plot(ch)
    plt.grid()
    plt.xlim([0,256])
    plt.show()

# Funcion para procesar y mostrar imagenes
def process_image(img_path):
    img_path2 = path + img_path
    img = cv2.imread(img_path2)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow(f'Original - {img_path}', img_gray)

    # Ecuación de histograma
    eq = cv2.equalizeHist(img_gray)
    cv2.imshow(f'Ecualizado - {img_path}', eq)

    # Calculo del histograma
    org_hist = cv2.calcHist([img_gray], [0], None, [256], [0,256])
    eq_hist = cv2.calcHist([eq], [0], None, [256], [0,256])

    # Ploteamos el histograma original y el equalizado
    hist(org_hist, 'Grises', f'Histograma Original - {img_path}')
    hist(eq_hist, 'Grises equalizados', f'Histograma Equalizado - {img_path}')

# Rutas de las imagenes
path='C:/Users/chris/OneDrive/Desktop/'
img_names = [
    'EscuelaAtenas.jpg',
    'Robot.jpg',
    'Roma.jpeg'
]

# Procesar cada imagen
for img_name in img_names:
    process_image(img_name)

cv2.waitKey(0)
cv2.destroyAllWindows()
