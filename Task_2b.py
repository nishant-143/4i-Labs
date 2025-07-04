import numpy as np
import cv2

img=cv2.resize(cv2.imread('/Users/nishanth/ab/templete.png', 0),(0,0),fx=1,fy=1)
template = cv2.resize(cv2.imread('/Users/nishanth/Downloads/9.png', 0),(0,0),fx=1,fy=1)

h, w = template.shape

#methods = [cv2.TM_SQDIFF,cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
methods = [cv2.TM_CCORR]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 0, 5)

    cv2.imwrite('image_9.png',img2)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()