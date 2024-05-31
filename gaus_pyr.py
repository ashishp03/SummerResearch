import numpy as np
import cv2 as cv

# Read the original image
img = cv.imread("img.png")

# Initialize a list to hold pyramid levels
pyramid = [img]

# Generate pyramid levels
level = img
for _ in range(5):  # Adjust the range for the number of levels you want
    level = cv.pyrDown(level)
    pyramid.append(level)

# Determine the width and height of the final pyramid image
total_height = sum(level.shape[0] for level in pyramid)
max_width = pyramid[0].shape[1]

# Create a blank canvas for the pyramid
pyramid_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)

# Place each level in the correct position
current_y = 0
for level in pyramid:
    h, w = level.shape[:2]
    pyramid_image[current_y:current_y + h, :w] = level
    current_y += h

# Display the pyramid image
cv.imshow("Image Pyramid", pyramid_image)
cv.waitKey(0)
cv.destroyAllWindows()
