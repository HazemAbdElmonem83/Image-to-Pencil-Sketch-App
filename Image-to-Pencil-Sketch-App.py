import cv2

def pencil_sketch(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Blur the inverted image using the GaussianBlur function
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    # Blend the inverted blurred image with the original grayscale image using the color dodge blend mode
    pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    return pencil_sketch


# Read input image
input_image = cv2.imread('1.jpg')

# Generate pencil sketch
output_sketch = pencil_sketch(input_image)

# Display the input and output images
cv2.imshow('Input Image', input_image)
cv2.imshow('Pencil Sketch', output_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
