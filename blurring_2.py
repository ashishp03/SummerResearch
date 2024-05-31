import cv2 as cv
import numpy as np

# Read the image from file
img = cv.imread('img.png')
assert img is not None, "File could not be read, check with os.path.exists()"

# Apply different blur effects
blur = cv.blur(img, (5, 5))
median_blur = cv.medianBlur(img, 5)
gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)

# Function to add label to the image
def add_label(image, text):
    labeled_image = image.copy()
    cv.putText(labeled_image, text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
    return labeled_image

# Add labels to each image
labeled_img = add_label(img, 'Original')
labeled_blur = add_label(blur, 'Blur')
labeled_median_blur = add_label(median_blur, 'Median Blur')
labeled_gaussian_blur = add_label(gaussian_blur, 'Gaussian Blur')

# Concatenate images to form a 2x2 grid
top_row = np.hstack((labeled_img, labeled_blur))
bottom_row = np.hstack((labeled_median_blur, labeled_gaussian_blur))
grid = np.vstack((top_row, bottom_row))

# Display the grid of images
cv.imshow('Image Grid', grid)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

# Destroy all windows
cv.destroyAllWindows()
