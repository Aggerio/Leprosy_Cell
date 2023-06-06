import contour
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../UnLabelled/img/1.jpeg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

threshold = 110
contour, img = contour.MainFunc(img, threshold)


plt.imshow(img)
plt.show()