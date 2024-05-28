import cv2
import numpy as np

image = np.zeros((100, 100, 3), dtype=np.uint8)

# Define the center, radius, color, and thickness of the circle
center = (50, 50)
radius = 20
color = (255, 0, 0)  # Red color in BGR format
thickness = 2

# Draw the circle
cv2.circle(image, center, radius, color, thickness)

cv2.imshow('Circle', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()