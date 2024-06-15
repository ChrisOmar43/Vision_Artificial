import cv2
from matplotlib import pyplot as plt

### Funciones del primer código

# Función de ploteo
def hist(ch, color):
    plt.figure()
    plt.title(color)
    plt.xlabel('Bins')
    plt.ylabel(f'Numero de pixeles {color}')
    plt.plot(ch)
    plt.grid()
    plt.xlim([0,256])
    plt.show()

# Función para ecualizar y mostrar un canal
def ecualizar_y_mostrar_canal(img_rgb, canal, nombre):
    canal_eq = cv2.equalizeHist(canal)
    cv2.imshow(f'{nombre} Ecualizado', canal_eq)
    return canal_eq

# Función para calcular histogramas de canal original y ecualizado
def calcular_histogramas(canal, canal_eq, nombre):
    canal_hist = cv2.calcHist([canal],[0],None,[256],[0,256])
    canal_eq_hist = cv2.calcHist([canal_eq],[0],None,[256],[0,256])
    hist(canal_hist, f'{nombre} og')
    hist(canal_eq_hist, f'{nombre} eq')

### Funciones y procesamiento con CLAHE

# Función para ecualizar un canal usando CLAHE y mostrarlo
def clahe_y_mostrar_canal(img_rgb, canal, nombre, clip=2.0, tile=8):
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(tile, tile))
    canal_clahe = clahe.apply(canal)
    cv2.imshow(f'{nombre} CLAHE', canal_clahe)
    return canal_clahe

# Declaración de imagen y separación de canales
img_path = 'C:/Users/chris/OneDrive/Desktop/EscuelaAtenas.jpg'
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canales = ['Azul', 'Verde', 'Rojo']
canales_rgb = [img_rgb[:,:,i] for i in range(3)]

# Ecualizando los canales y mostrando los resultados (histograma estándar)
canales_eq = [ecualizar_y_mostrar_canal(img_rgb, canales_rgb[i], canales[i]) for i in range(3)]

# Calculando y ploteando los histogramas (histograma estándar)
for i in range(3):
    calcular_histogramas(canales_rgb[i], canales_eq[i], canales[i])

# Haciendo merge y mostrándolo (histograma estándar)
img_eq = cv2.merge(canales_eq)
cv2.imshow('Imagen Ecualizada', img_eq)

### Procesamiento de CLAHE

# Ecualizando los canales usando CLAHE y mostrando los resultados
canales_clahe = [clahe_y_mostrar_canal(img_rgb, canales_rgb[i], canales[i]) for i in range(3)]

# Calculando y ploteando los histogramas (CLAHE)
for i in range(3):
    calcular_histogramas(canales_rgb[i], canales_clahe[i], f'{canales[i]} CLAHE')

# Haciendo merge y mostrándolo (CLAHE)
img_clahe = cv2.merge(canales_clahe)
cv2.imshow('Imagen CLAHE', img_clahe)
cv2.imshow('Imagen Original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()