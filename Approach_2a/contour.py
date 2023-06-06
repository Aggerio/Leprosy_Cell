import cv2 as cv
import numpy as np
import argparse
import random as rng
import matplotlib.pyplot as plt



# img = cv.imread("../UnLabelled/1.jpeg")
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

def MainFunc(im, threshold):
    img = im
    def getContours(threshold, img):
        src_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

        canny_output = cv.Canny(src_gray, threshold, threshold * 2)


        contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        return contours

    def draw_img(contours,threshold, img): 
        copy_img = img
        src_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

        canny_output = cv.Canny(src_gray, threshold, threshold * 2)
        # Get the moments
        mu = [None]*len(contours)
        for i in range(len(contours)):
            mu[i] = cv.moments(contours[i])
        # Get the mass centers
        mc = [None]*len(contours)
        for i in range(len(contours)):
            # add 1e-5 to avoid division by zero
            mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))

        #Drawing
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

        for i in range(len(contours)):
            color = (170,255,0)
            # cv.drawContours(drawing, contours, i, color, 2)
            # cv.drawContours(copy_img, contours, i, color, 2)
            cv.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)
            cv.circle(copy_img, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)

        # plt.imshow(drawing)
        # plt.show()
        print("Img with Contours")
        # plt.imshow(copy_img)
        # plt.show()
        return copy_img

    return getContours(threshold, img), draw_img(getContours(threshold, img), threshold, im)
