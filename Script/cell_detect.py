import cv2 as cv
import numpy as np
import argparse
import random as rng

def markContour(img):

    def contour_viewer(img):
            
        def thresh_callback(val):
            non_zero_pixels = 0
            threshold = val
            
            canny_output = cv.Canny(src_gray, threshold, threshold * 2)
            
            
            contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            
            # Get the moments
            mu = [None]*len(contours)
            for i in range(len(contours)):
                mu[i] = cv.moments(contours[i])
            # Get the mass centers
            mc = [None]*len(contours)
            for i in range(len(contours)):
                # add 1e-5 to avoid division by zero
                mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
            # Draw contours
            
            drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
            orignal_img_to_draw = src
            
            for i in range(len(contours)):
                color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
                cv.drawContours(drawing, contours, i, color, 2)
                cv.drawContours(orignal_img_to_draw, contours, i, (255,0,255), 2)
                # cv.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)
                cv.circle(orignal_img_to_draw, (int(mc[i][0]) , int(mc[i][1])), 4,(255,0,0),1)
            
        #     print("contours on orignal image: ")
        #     plt.imshow(orignal_img_to_draw)
        #     plt.show()
            
            
        # #     cv.imshow('Contours', drawing)
        #     print("Contours on a black screen")
        #     plt.imshow(drawing)
        #     plt.show()
    
            # fig, axes = plt.subplots(1,2,figsize=(96,128))
    
            # axes[0].imshow(orignal_img_to_draw)
            # axes[1].imshow(drawing)
            # plt.show()
    
            
            # Calculate the area with the moments 00 and compare with the result of the OpenCV function
            for i in range(len(contours)):
        #         print(' * Contour[%d] - Area (M_00) = %.2f - Area OpenCV: %.2f - Length: %.2f' % (i, mu[i]['m00'],
        #                                                                                           cv.contourArea(contours[i]), cv.arcLength(contours[i], True)))
                non_zero_pixels += cv.contourArea(contours[i])
            return drawing,non_zero_pixels, orignal_img_to_draw
    
        src = img
        if src is None:
            print('Could not open or find the image:', args.input)
            exit(0)
        src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        src_gray = cv.blur(src_gray, (3,3))
    
        max_thresh = 255
        thresh = 70 # initial threshold
    
        # print("Orignal Image: ")
        # plt.imshow(src)
        # print("Contoured Image: ")
        drawing,non_zero_pixels, orig_img_cont = thresh_callback(thresh)
    
        # print("No. of non zero pixels: ",round(non_zero_pixels))
        return drawing,non_zero_pixels, orig_img_cont
    
