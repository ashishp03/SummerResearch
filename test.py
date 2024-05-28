import cv2

# Initialize the USB camera
cap = cv2.VideoCapture(0)  # 0 indicates the first camera device, change it if you have multiple cameras

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera")
    exit()

# Print camera properties
print("Camera properties:")
print("Width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("FPS:", cap.get(cv2.CAP_PROP_FPS))

# Read and display the video stream
while True:
    ret, frame = cap.read()  # Read a frame from the camera

    # Check if the frame was read successfully
    if not ret:
        print("Error: Couldn't read frame")
        break

    cv2.imshow('USB Camera', frame)  # Display the frame in a window

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
