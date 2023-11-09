# Importamos cv2

import cv2

# Cargamos la imagen
image = cv2.imread('imagenes_v/lena.tif')
cv2.imshow('mat/original', image)
cv2.waitKey(0)
# Aplicamos ecualización de histogramas a la imagen de entrada.
equalized = cv2.equalizeHist(image)
# Mostramos el resultado.
# cv2.imshow('equalizada', equalized)
cv2.imshow('Im Original', image)
cv2.imshow('Im Equalizada', equalized)
cv2.waitKey(0)
# Destruimos las ventanas creadas.
cv2.destroyAllWindows()
