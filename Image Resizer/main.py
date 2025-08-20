import cv2

#Configurable Parameter
source = "ai-generated-picture-of-a-tiger-walking-in-the-forest-photo.jpg"
destination = 'newImage2.jpg'
# Percent by which the image is resized
scale_percent = 200

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)


# Calculate the 50 percent of original dimension
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

dsize = (new_width, new_height)

output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)

cv2.waitKey(0)