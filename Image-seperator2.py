import cv2

# Load the image
img = cv2.imread('SlidesImage/3.7 Supply-side Policies.pdf/page2.jpg')

# Define the lower and upper bounds of the yellow color in BGR format
lower_yellow = (0, 254, 254)
upper_yellow = (2, 255, 255)

# Create a mask using the lower and upper bounds of the yellow color
mask = cv2.inRange(img, lower_yellow, upper_yellow)

# Apply the mask to the original image to extract only the yellow pixels
yellow_pixels = cv2.bitwise_and(img, img, mask=mask)

# Convert the yellow_pixels image to grayscale
yellow_pixels_gray = cv2.cvtColor(yellow_pixels, cv2.COLOR_BGR2GRAY)

# Find the coordinates of the non-zero pixels (i.e., the yellow pixels)
coords = cv2.findNonZero(yellow_pixels_gray)

# Print the array of yellow pixel coordinates
print(coords)