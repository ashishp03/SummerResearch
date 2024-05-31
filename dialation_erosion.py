import cv2 as cv
import numpy as np

img = cv.imread("j2.png")

kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img,kernel,iterations = 1)
erosion = cv.erode(img,kernel,iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

                     
def add_label(image, text):
    labeled_image = image.copy()
    cv.putText(labeled_image, text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
    return labeled_image

labeled_orig = add_label(img, "Original")
labeled_dilation = add_label(dilation, "Dilation")
labeled_erosion = add_label(erosion, "Erosion")
labeled_opening = add_label(opening, "Opening")
labeled_closing = add_label(closing, "Closing")
labeled_gradient = add_label(gradient, "Gradient")
labeled_tophat = add_label(tophat, "Tophat")
labeled_blackhat = add_label(blackhat, "Blackhat")

top_row = np.hstack((labeled_orig, labeled_dilation, labeled_erosion, labeled_opening))
bottom_row = np.hstack((labeled_closing, labeled_gradient, labeled_tophat, labeled_blackhat))
grid = np.vstack((top_row, bottom_row))

# Display the grid of images
cv.imshow('Morphological Operations Grid', grid)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

# Destroy all windows
cv.destroyAllWindows()