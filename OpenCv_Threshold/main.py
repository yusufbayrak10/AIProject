#Thresholding nedir, hangi alanlarda kullanılır araştırın ve bir yaprak resmi üzerinde bu işlemi gerçekleştirin.

import cv2


image = cv2.imread("leaf.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value, threshold_image = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)
cv2.imwrite("threshold_leaf.jpg", threshold_image)