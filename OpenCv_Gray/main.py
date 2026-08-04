#OpenCV kullanarak açtığınız bu resmi gri tonlamaya dönüştürün. (Filtre uygulansın.)
import cv2

image = cv2.imread("images.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg", gray)