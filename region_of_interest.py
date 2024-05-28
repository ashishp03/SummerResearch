import cv2
import numpy as np

# Step 1: Create a 210x210 single-channel matrix and set all values to 0
image = np.zeros((210, 210), dtype=np.uint8)

# Step 2: Set pyramid values with a border width of 10 pixels
value = 0
step = 20
border_width = 10

# Loop to set values for each layer of the pyramid
for i in range(0, 210 // (2 * border_width)):
    # Define the top-left and bottom-right points of the ROI
    top_left = (i * border_width, i * border_width)
    bottom_right = (210 - i * border_width, 210 - i * border_width)
    
    # Set the ROI to the current value
    cv2.rectangle(image, top_left, bottom_right, value, thickness=cv2.FILLED)
    
    # Increment the value for the next inner border
    value += step

# Step 3: Display the image
cv2.imshow('Pyramid', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
