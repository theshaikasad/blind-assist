import cv2
import pyttsx3
import threading
import time

# List of object classes
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

# Load pre-trained model
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet_iter_73000.caffemodel")

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    threading.Thread(target=lambda: engine.say(text) or engine.runAndWait()).start()

# Start camera
cap = cv2.VideoCapture(0)
last_spoken = 0
cooldown = 2  # seconds
PROXIMITY_THRESHOLD = 180  # Width of bounding box in pixels

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    # Prepare frame for detection
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    too_close_spoken = False

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.4:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (startX, startY, endX, endY) = box.astype("int")
            box_width = endX - startX

            # Draw box and label
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            text = f"{label}: {int(confidence * 100)}%"
            cv2.putText(frame, text, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

            print(f"Detected: {label} with confidence {confidence}")

            if box_width > PROXIMITY_THRESHOLD and time.time() - last_spoken > cooldown:
                speak(f"{label} is too close")
                last_spoken = time.time()
                too_close_spoken = True

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        print("Key 's' pressed, announcing detected objects")
        objects_in_frame = set()
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.4:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                objects_in_frame.add(label)

        if objects_in_frame:
            speak("I see: " + ", ".join(objects_in_frame))
        else:
            speak("I see nothing.")

    # Display
    cv2.imshow("Object Proximity Detector", frame)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
