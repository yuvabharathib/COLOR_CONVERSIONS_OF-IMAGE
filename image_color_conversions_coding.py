


import cv2
from google.colab.patches import cv2_imshow

#read and diplay image

#WRITE AN IMAGE


# Save the original image to a file
original_output_path = "image path"
cv2.imwrite(original_output_path, image)
print(f"Original image saved to: {original_output_path}")

# Read the saved image


# Display the saved image


# Save the saved image to a new file

cv2.imwrite(new_output_path, saved_image)
print(f"Saved image saved to: {new_output_path}")

#ACCESSING ROWS AND COLUMNS

# Get the shape of the image (rows, columns, channels)

print(f"Image Shape: Rows={rows}, Columns={columns}, Channels={channels}")

# Assign random values to pixels in the first row and first column
                                                                 # Random values for the first row
image[:, 0] = np.random.randint(0, 256, size=(rows, channels))  # Random values for the first column

# Display the modified image

#Cut and paste the image


# Display the original image


# Get the shape of the image (rows, columns, channels)


# Define the region to cut (example: top-left corner, width=100, height=100)
cut_region = image[0:100, 0:100]

# Paste the cut region back onto the image (example: paste at (200, 200))
image[] = cut_region

#######COLOR CONVERSION
#Convert BGR and RGB to HSV and GRAY

# Convert BGR to RGB
image_rgb = (image_bgr, cv2.COLOR_BGR2RGB)

# Convert BGR to HSV
image_hsv_bgr = cv2.cvtColor(image_bgr, )

# Convert RGB to HSV


# Convert BGR to Grayscale


# Convert RGB to Grayscale


# Display the original BGR image

# Display the HSV image (BGR and RGB converted)

# Display the Grayscale image (BGR and RGB converted)
print("BGR TO GRAY")
cv2_imshow(image_gray_bgr)
print("RGB TO GRAY")
cv2_imshow(image_gray_rgb)

#Convert HSV to RGB and BGR

# Convert BGR to HSV

# Convert HSV to RGB

# Convert HSV to BGR
image_bgr_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

# Display the original BGR image

cv2_imshow(image_bgr)

# Display the HSV image

cv2_imshow(image_hsv)

# Display the RGB image (HSV to RGB)
print("HSV TO RGB")


# Display the BGR image (HSV to BGR)

#Convert RGB and BGR to YCrCb


# Convert BGR to YCrCb
image_ycrcb_bgr = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YCrCb)

# Convert RGB to YCrCb
                                                                # Convert BGR to RGB
image_ycrcb_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# Display the original BGR image


# Display the YCrCb image (BGR to YCrCb)


# Display the YCrCb image (RGB to YCrCb)

#Split and Merge RGB Image


# Split the RGB channels
blue_channel, green_channel, red_channel = cv2.split(image_bgr)

# Display the original BGR image


# Display the individual RGB channels
print("BLUE CHANNEL")
cv2_imshow(blue_channel)


# Merge the RGB channels back together


# Display the merged image

#Split and merge HSV Image

# Convert BGR to HSV


# Split the HSV channels

# Display the original BGR image and the converted HSV image
print("ORIGINAL IMAGE")
cv2_imshow(image_bgr)
print("HSV IMAGE")
cv2_imshow(image_hsv)

# Display the individual HSV channels

