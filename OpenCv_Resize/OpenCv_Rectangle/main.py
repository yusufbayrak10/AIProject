#Resmin belirli bir kısmını sarı renkli bir çerçeveyle kare veya dikdörtgen içine alın. Bu alanın içini doldurun.

import cv2
image = cv2.imread("image.jpg")
cv2.rectangle(image, (100, 100), (300, 300), (128, 0, 0), -1)
cv2.rectangle(image, (100, 100), (300, 300), (0, 255, 255), 5)
cv2.imwrite("rectangle.jpg", image)