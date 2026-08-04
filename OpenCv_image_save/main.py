import cv2

image = cv2.imread("images.jpg")
cv2.imwrite("output.jpg", image)