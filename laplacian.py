import numpy as np
import cv2 as cv

# Read the original image
img = cv.imread("img.png")

# Generate Gaussian pyramid
gaussian_pyramid = [img]
for i in range(5):  # Adjust the range for the number of levels you want
    img = cv.pyrDown(img)
    gaussian_pyramid.append(img)

# Generate Laplacian pyramid
laplacian_pyramid = []
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)

# Display the Gaussian and Laplacian pyramids
for i, (g, l) in enumerate(zip(gaussian_pyramid, laplacian_pyramid)):
    cv.imshow(f"Gaussian Level {i}", g)
    cv.imshow(f"Laplacian Level {i}", l)

cv.waitKey(0)
cv.destroyAllWindows()
