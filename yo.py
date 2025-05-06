import torch
import cv2

# Load YOLOv5 model (from Ultralytics repo)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Set the model to detect only 'person' class (class 0 in COCO dataset)
model.classes = [0]

# Open webcamera
cap = cv2.VideoCapture(0, cv2.CAP_ANY)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break

    # Inference
    results = model(frame)

    # Render detections on frame
    annotated_frame = results.render()[0]  # Returns a list

    # Show the frame
    cv2.imshow("YOLOv5 Person Detection", annotated_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
