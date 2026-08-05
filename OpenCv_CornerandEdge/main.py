#Corner Detection ve Edge Detection işlemlerini istediğiniz bir fotoğraf üzerinde sırasıyla gerçekleştirin.

import cv2
import numpy as np


image = cv2.imread("chessboard.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_float = np.float32(gray)
corners = cv2.cornerHarris(gray_float, 2, 3, 0.04)
corner_image = image.copy()
corner_image[corners > 0.01 * corners.max()] = [0, 0, 255]
cv2.imwrite("corner.jpg", corner_image)

edges = cv2.Canny(gray, 100, 200)

cv2.imwrite("edge.jpg", edges)