import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Provide your weights and config paths
classes = []
with open("coco.names", "r") as f:  # Provide the path to the COCO class names file
    classes = f.read().strip().split("\n")

# Load image
image = cv2.imread("car.jpeg")  # Provide the path to your image

# Get image dimensions
height, width, _ = image.shape

# Preprocess image for YOLO
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)

# Get output layer names
output_layer_names = net.getUnconnectedOutLayersNames()

# Forward pass through the network
outs = net.forward(output_layer_names)

# Information to be extracted from the output
class_ids = []
confidences = []
boxes = []

# Process the output
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # You can adjust the confidence threshold as needed
            # YOLO returns center coordinates and width/height of the bounding box
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            
            # Calculate the top-left corner coordinates of the bounding box
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])

# Apply non-max suppression to remove overlapping bounding boxes
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

detected_objects = []

# Process the detected objects
for i in indexes:
    i = i[0]
    label = str(classes[class_ids[i]])
    confidence = confidences[i]
    box = boxes[i]
    
    title = f"{label} ({confidence:.2f})"
    detected_objects.append(title)

# Create a title for the image based on detected objects
image_title = ", ".join(detected_objects)

# Display or save the image with the title
cv2.putText(image, image_title, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Image with Title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
