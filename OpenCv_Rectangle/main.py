#Resmin belirli bir kısmını sarı renkli bir çerçeveyle kare veya dikdörtgen içine alın. Bu alanın içini doldurun.

import cv2
image = cv2.imread("images.jpg")
cv2.rectangle(image, (50, 50), (150, 150), (128, 0, 0), -1)
cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 255), 2)
cv2.imwrite("rectangle.jpg", image)