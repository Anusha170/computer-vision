import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:/Users/Hello/Downloads/WhatsApp Video 2024-03-22 at 12.02.27 PM.mp4')

if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
