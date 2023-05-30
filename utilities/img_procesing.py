import cv2
import numpy as np


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def getGamma(img):
    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([bw], [0], None, [256], [0, 256])

    # Find the peak intensity value
    peak_intensity = np.argmax(histogram)

    # Calculate the gamma value
    gamma = np.log10(peak_intensity) / np.log10(255)

    return gamma


def normaliza(a):
    a = a.astype(np.double)
    a = a / a.max() * 255
    b = a.astype(np.uint8)
    return b


def bgr2lms(img):
    a = img
    gamma = getGamma(a)
    a = adjust_gamma(a, 1 / gamma)
    a = cv2.cvtColor(a, cv2.COLOR_BGR2XYZ)
    lms_matrix = np.matrix([
        [0.4002, 0.7076, -0.0808],
        [-0.2263, 1.1653, 0.0457],
        [0, 0, 0.9182]
    ])
    a = cv2.transform(a, lms_matrix, None)
    return a, gamma


def lms2bgr(img, gamma):
    a = img
    lms2xyz_matrix = np.matrix([
        [1.8600666, -1.1294801, 0.2198983],
        [0.3612229, 0.6388043, 0],
        [0, 0, 1.0890870]
    ])
    a = cv2.transform(a, lms2xyz_matrix, None)
    a = cv2.cvtColor(a, cv2.COLOR_XYZ2BGR)
    a = adjust_gamma(a, gamma)
    return a


def daltonice(img, type):
    a = img
    a, gamma = bgr2lms(a)
    daltonization_matrix = np.zeros((3, 3))
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
    a = cv2.transform(a, daltonization_matrix, None)
    a = lms2bgr(a, gamma)
    return a
