#Kare içine alınan bu alanı önce griye dönüştürün, ardından bu alanı bulanıklaştırın. Bu işlemlerin gerçek hayatta nerelerde kullanıldığını araştırın.


import cv2
image = cv2.imread("images.jpg")
roi = image[50:150, 50:150]
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
blurred_roi = cv2.GaussianBlur(gray_roi, (15, 15), 0)
blurred_roi = cv2.cvtColor(blurred_roi, cv2.COLOR_GRAY2BGR)
image[50:150, 50:150] = blurred_roi
cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 255), 3)
cv2.imwrite("processed_image.jpg", image)