import sys
try:
    import argparse
    import os
    import cv2 as cv
    import matplotlib.pyplot as plt 
    import contour

except Exception as e:
    print("run setup.py please, incomplete dependencies")
    sys.exit()

argParser = argparse.ArgumentParser()
argParser.add_argument("-i", "--input-dir", required=True, help = "your input directory")


args = argParser.parse_args()
orignal_dir = os.getcwd()
output_dir = orignal_dir + "/Predicted_Masks"
# print(f"outp_dir: {output_dir}")
target_dir = orignal_dir + "/" + args.input_dir
os.chdir(args.input_dir)

if not os.path.isdir(target_dir):
    print(f"Invalid file directory specified\n suggested to copy all images in the same dir and then try")
    sys.exit()

if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# try:
    # print(os.listdir())
    
for i in os.listdir(target_dir):
    lst_ext = (i.split('.'))[-1]
    valid = True if (lst_ext == "jpg" or lst_ext == "jpeg") else False 
    # print(f"valid file: {i} with status {valid}")

    if valid:
        threshold = 70
        img = cv.imread(target_dir + "/" + i) # --> Here the exception is occuring
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        _,_,img_temp = contour.MainFunc(img, threshold)
        # plt.imshow(img_temp)
        # plt.show()

        print(f" Writing image: {i} in directory {target_dir}")
        img_temp = cv.cvtColor(img_temp, cv.COLOR_BGR2RGB)
        cv.imwrite(output_dir + "/" +  i , img_temp)


# except Exception as e:
#     print(f"The following exception occured {e}")
