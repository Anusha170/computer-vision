import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Hello\Pictures\WhatsApp Image 2024-02-09 at 1.54.51 PM.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0,1,0], [1,-4,1], [0,1,0]])
sharpened = cv2.filter2D(gray, -1, kernel)
cv2.imshow('Original', gray)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
