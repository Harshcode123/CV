import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)
cap.isOpened()

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break
    
    # Define the text and its properties
    text = "Harsh How Are you"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = .0
    color = (0, 255, 0)  # Green (BGR format)
    thickness = 2
    position = (50, 50)  # (x, y) coordinates
    
    # Put the text on the frame
    cv2.putText(frame, text, position, font, font_scale, color, thickness)
    
    # Display the frame
    cv2.imshow('Camera Feed with Text', frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()