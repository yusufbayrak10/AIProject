#OpenCV kütüphanesindeki Watershed fonksiyonunu kullanarak segmentasyon yapın.

import cv2
import numpy as np

image = cv2.imread("water_coins.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)
kernel = np.ones((3, 3), np.uint8)
# Küçük gürültüleri temizle
opening = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel,
    iterations=2
)
# Kesin arka plan
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# Paraların merkezlerini bul
dist_transform = cv2.distanceTransform(
    opening,
    cv2.DIST_L2,
    5
)
_, sure_fg = cv2.threshold(
    dist_transform,
    0.5 * dist_transform.max(),
    255,
    0
)
sure_fg = np.uint8(sure_fg)
# Belirsiz alan
unknown = cv2.subtract(sure_bg, sure_fg)
# Her para bölgesine farklı marker numarası ver
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
# Watershed uygula
markers = cv2.watershed(image, markers)
# Segment sınırlarını kırmızı göster
image[markers == -1] = [0, 0, 255]

cv2.imwrite("watershed_result.jpg", image)