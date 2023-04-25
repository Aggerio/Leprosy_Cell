import colorsys
import sys

# usage.
# run this script, in particular the function convert_rgb_to_hsv()
# edit red, green, blue


def convert_rgb_to_hsv():
    # rgb normal: range (0-255, 0-255, 0.255)
    red = int(sys.argv[1])
    green = int(sys.argv[2])
    blue = int(sys.argv[3])

    # get rgb percentage: range (0-1, 0-1, 0-1 )
    red_percentage = red / float(255)
    green_percentage = green / float(255)
    blue_percentage = blue / float(255)

    # get hsv percentage: range (0-1, 0-1, 0-1)
    color_hsv_percentage = colorsys.rgb_to_hsv(
        red_percentage, green_percentage, blue_percentage)
    print('color_hsv_percentage: ', color_hsv_percentage)

    # get normal hsv: range (0-360, 0-255, 0-255)
    color_h = round(360*color_hsv_percentage[0])
    color_s = round(255*color_hsv_percentage[1])
    color_v = round(255*color_hsv_percentage[2])
    color_hsv = (color_h, color_s, color_h)

    print('color_hsv: ', color_hsv)


# INVOCATE MAIN FUNCTION
convert_rgb_to_hsv()
