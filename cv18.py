import cv2

# Read the original image
img = cv2.imread(r"C:\Users\Hello\Pictures\WhatsApp Image 2024-02-09 at 1.54.51 PM.jpeg")

# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Sobel Edge Detection
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
