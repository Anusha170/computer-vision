import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread(r'C:\Users\Hello\Pictures\WhatsApp Image 2024-02-09 at 2.00.08 PM.jpeg')
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
