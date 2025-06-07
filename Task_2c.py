import cv2
import numpy as np

img = cv2.imread('/Users/nishanth/Downloads/4.jpg')

def histogram_equalization(img):
    b, g, r = cv2.split(img)
    b_eq = cv2.equalizeHist(b)
    g_eq = cv2.equalizeHist(g)
    r_eq = cv2.equalizeHist(r)
    img_eq = cv2.merge([b_eq, g_eq, r_eq])
    return img_eq

def bilateral_filter(img):
    img_b = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    return img_b

def filter_2d(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    Filter2d = cv2.filter2D(img, -1, kernel)
    return Filter2d

def gaussian_blur(img):
    img_g = cv2.GaussianBlur(img, (5,5), 0)
    return img_g

def unsharp_mask(img):
    blur = cv2.GaussianBlur(img, (9,9), 10)
    unsharp = cv2.addWeighted(img, 1.5, blur, -0.5, 0)
    return unsharp

def detail_enhancement(img):
    img_d = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
    return img_d

img_1 = histogram_equalization(img)
img_2 = bilateral_filter(img_1)
img_3 = filter_2d(img_2)
img_4 = gaussian_blur(img_3)
img_5 = unsharp_mask(img_4)
img_6 = detail_enhancement(img_5)

cv2.imwrite('filtered_image_4.jpg',img_6)
cv2.imshow('filtered_image_4.jpg', img_6)
cv2.waitKey(0)
cv2.destroyAllWindows()