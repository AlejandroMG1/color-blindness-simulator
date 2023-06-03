import cv2
import numpy as np

"""Metodo que ajusta la corrección gamma de una imagen"""
def adjust_gamma(image, gamma=1.0):
    # Se crea una tabla de ajuste con los valores invertidos de gamma
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # se aplica la corrección gamma con la tabla
    return cv2.LUT(image, table)


"""Metodo que obtiene un valor estimado de gamma para una imagen dada"""
def getGamma(img):
    # Se transforma la imagen a blanco y negro
    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Se calcula el histograma de la imagen
    histogram = cv2.calcHist([bw], [0], None, [256], [0, 256])

    # Se encuentra el pico de intensidad
    peak_intensity = np.argmax(histogram)

    # se calcula el valor de gamma con la divicón del logaritmo del pico sobre el logatimo de 255
    gamma = np.log10(peak_intensity) / np.log10(255)

    return gamma


"""Metodo que transforma la imagen a espacio de color lms desde bgr"""
def bgr2lms(img):
    a = img
    # se obtiene un valor estimado de gamma
    gamma = getGamma(a)
    # se remueve la corrección gamma para una correcta transformación de colores
    a = adjust_gamma(a, 1 / gamma)
    # se tranforma primero la imagen a espacio de color xyz
    a = cv2.cvtColor(a, cv2.COLOR_BGR2XYZ)
    # creación de matriz de transformación de espacio de color xyz a lms
    lms_matrix = np.matrix([
        [0.4002, 0.7076, -0.0808],
        [-0.2263, 1.1653, 0.0457],
        [0, 0, 0.9182]
    ])
    # aplicación de la matriz de transformación a la imagen en espacio de color xyz
    a = cv2.transform(a, lms_matrix, None)
    # se retorna la imagen en espacio de color lms y el valor estimado de corrección gamma
    return a, gamma


"""Metodo que transforma una imagen en bgr a lms"""
def lms2bgr(img, gamma):
    a = img
    # creación de matriz de transformación de mls a xyz a partir de la inversa de la usada para pasar de xyz a mls
    lms2xyz_matrix = np.matrix([
        [1.8600666, -1.1294801, 0.2198983],
        [0.3612229, 0.6388043, 0],
        [0, 0, 1.0890870]
    ])
    # aplicación de la matriz de transformación a la imagen en espacio de color lms
    a = cv2.transform(a, lms2xyz_matrix, None)
    # transformación de la imagen en el espacio de colorxyz a lms
    a = cv2.cvtColor(a, cv2.COLOR_XYZ2BGR)
    # se devuelve el ajuste de gamma
    a = adjust_gamma(a, gamma)
    return a


def daltonice(img, type):
    a = img
    # se transforma la imagen de bgr a lms
    a, gamma = bgr2lms(a)
    # instanciación de la matriz de transformación
    daltonization_matrix = np.zeros((3, 3))

    # se asigna los valores de la matriz segun el tipo de daltonismo pedido
    if type == "prot":
        daltonization_matrix = np.matrix([
            [0, 1.05118294, -0.05116099],
            [0, 1, 0],
            [0, 0, 1]
        ])
    elif type == "deu":
        daltonization_matrix = np.matrix([
            [1.025, 0, 0],
            [0.92130920, 0, 0.08866992],
            [0, 0, 1]
        ])
    # aplicación de la matriz de la transformación de daltonismo a la imagen en espacio de color lms
    a = cv2.transform(a, daltonization_matrix, None)
    # se devuelve la imagen a espacio de color bgr
    a = lms2bgr(a, gamma)
    return a
