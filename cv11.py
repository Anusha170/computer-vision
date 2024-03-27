import cv2
path = r"C:\Users\Hello\Pictures\WhatsApp Image 2024-02-09 at 2.00.08 PM.jpeg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0)
