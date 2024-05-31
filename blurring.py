import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('img.png')
assert img is not None, "file could not be read, check with os.path.exists()"
 
median = cv.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()