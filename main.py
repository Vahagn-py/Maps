import cv2 as cv
import numpy as np


aia_img = cv.imread('aia.jpg', cv.IMREAD_UNCHANGED)
air_img = cv.imread('air.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(aia_img, air_img, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found needle.')


    air_w = air_img.shape[1]
    air_h = air_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + air_w, top_left[1] + air_h)

    cv.rectangle(aia_img, top_left, bottom_right,
                color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', aia_img)
    cv.waitKey()
    cv.imwrite('result.jpg', aia_img)

else:
    print('Needle not found.')


# cv.imshow('Result', result)
# cv.waitKey()
