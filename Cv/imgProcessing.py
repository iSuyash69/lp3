import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display an image in Jupyter Notebook
def display_image(image, title="Image"):
    if image is None:
        print("Error: Image not found or could not be loaded.")
        return
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Read the image in grayscale
img = cv2.imread('./CV Final/Final/Ferrari.jpg')
if img is None:
    print("Error: The image could not be loaded.")
    exit()

display_image(img, "Original")

# Crop the image (example coordinates)
cropped_image = img[300:1300, 200:2000]
display_image(cropped_image, "Cropped Image")

# Resize image (down and up)
down_points = (300, 200)
resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
up_points = (600, 400)
resized_up = cv2.resize(img, up_points, interpolation=cv2.INTER_LINEAR)
display_image(resized_down, 'Resized Down')
display_image(resized_up, 'Resized Up')

# Image contouring on color channels (Blue, Green, Red)
image = cv2.imread('./CV Final/Final/Ferrari.jpg')
blue, green, red = cv2.split(image)

# Contours on Blue Channel
contours, _ = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_contour_blue = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
display_image(image_contour_blue, "Contour on Blue Channel")

# Contours on Green Channel
contours, _ = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_contour_green = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
display_image(image_contour_green, "Contour on Green Channel")

# Contours on Red Channel
contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_contour_red = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
display_image(image_contour_red, "Contour on Red Channel")

# Blob detection
im = cv2.imread("./CV Final/Final/Ferrari.jpg")
detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(im)
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
display_image(im_with_keypoints, "Blob Detection")
