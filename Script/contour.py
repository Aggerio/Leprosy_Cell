import cv2 as cv
import numpy as np
import argparse
import random as rng
import matplotlib.pyplot as plt


def MainFunc(im, threshold):

        
    def thresh_callback(val):
        non_zero_pixels = 0
        threshold = val
        
        canny_output = cv.Canny(src_gray, threshold, threshold * 2)
        
        
        contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        
        mu = [None]*len(contours)
        for i in range(len(contours)):
            mu[i] = cv.moments(contours[i])
        mc = [None]*len(contours)
        for i in range(len(contours)):
            # add 1e-5 to avoid division by zero
            mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
        
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

        orignal_img_to_draw = src
        
        for i in range(len(contours)):
            color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
            cv.drawContours(drawing, contours, i, color, 2)
            cv.drawContours(orignal_img_to_draw, contours, i, (255,0,255), 2)
            # cv.circle(orignal_img_to_draw, (int(mc[i][0]) , int(mc[i][1])), 4,(255,0,0),1)


        
        for i in range(len(contours)):
            non_zero_pixels += cv.contourArea(contours[i])
        return drawing,non_zero_pixels, orignal_img_to_draw

    src = im
    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)
    src_gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    src_gray = cv.blur(src_gray, (3,3))

    max_thresh = 255
    thresh = threshold

    drawing,non_zero_pixels, orig_img_cont = thresh_callback(thresh)

    return drawing,non_zero_pixels, orig_img_cont
