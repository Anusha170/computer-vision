import cv2

path = r"C:\Users\Hello\Pictures\WhatsApp Image 2024-02-09 at 2.00.08 PM.jpeg"
src = cv2.imread(path)
window_name = 'Image'

if src is not None:  # Checking if the image was read successfully
    image = cv2.rotate(src, cv2.ROTATE_180)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to read the image. Please check the file path.")

