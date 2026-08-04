#Resmi yeniden boyutlandırın. Bu işlem sonrası, seçtiğiniz belirli bir alanı gösteren bir görüntü oluşturun.

import cv2

image = cv2.imread("images.jpg")
resized = cv2.resize(image, (500, 500))
roi = resized[100:300, 100:300]
cv2.imwrite("resized.jpg", resized)
cv2.imwrite("roi.jpg", roi)