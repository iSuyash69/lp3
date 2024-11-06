import cv2
import matplotlib.pyplot as plt

# Load the original image
img = cv2.imread('D:/files/endsem 2024/CV Final/Final/image2.jpeg')

# Display the original image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
plt.title('Original Image')
plt.axis('off')  # Hide axes
plt.show()

# Draw a line
line_image = img.copy()  # Create a copy for the line
pointA = (20, 20)
pointB = (200, 20)
cv2.line(line_image, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
plt.imshow(cv2.cvtColor(line_image, cv2.COLOR_BGR2RGB))
plt.title("Image with Line")
plt.axis('off')
plt.show()

# Draw a rectangle
rectangle_image = img.copy()  # Create a copy for the rectangle
start_point = (10, 10)
end_point = (100, 100)
cv2.rectangle(rectangle_image, start_point, end_point, (225, 24, 255), thickness=3, lineType=cv2.LINE_8)
plt.imshow(cv2.cvtColor(rectangle_image, cv2.COLOR_BGR2RGB))
plt.title("Image with Rectangle")
plt.axis('off')
plt.show()

# Draw a circle
circle_image = img.copy()  # Create a copy for the circle
circle_center = (50, 50)
radius = 20
cv2.circle(circle_image, circle_center, radius, (255, 225, 255), thickness=3, lineType=cv2.LINE_AA)
plt.imshow(cv2.cvtColor(circle_image, cv2.COLOR_BGR2RGB))
plt.title("Image with Circle")
plt.axis('off')
plt.show()

# Draw ellipses
ellipse_image = img.copy()  # Create a copy for the ellipses
center = (120, 70)
axis1 = (30, 64)
axis2 = (25, 75)
cv2.ellipse(ellipse_image, center, axis1, 0, 0, 360, (255, 255, 0), thickness=3)
cv2.ellipse(ellipse_image, center, axis2, 90, 0, 360, (0, 255, 255), thickness=3)
plt.imshow(cv2.cvtColor(ellipse_image, cv2.COLOR_BGR2RGB))
plt.title("Image with Ellipses")
plt.axis('off')
plt.show()
