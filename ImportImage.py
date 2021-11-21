import cv2  #openCV lib,for image processing.
image=cv2.imread("myimage.jpg") #imread,reading an image from a file.
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #cvt,means converting an image from one color to another.

inverted_image=255-gray_image #inverting grayscale img also called the negative image.

# Finally create the pencil sketch by mixing the grayscale image with the inverted blurry image. 
# This is done by dividing the grayscale image by the inverted blurry image.
blurred=cv2.GaussianBlur(inverted_image,(21,21),0)
inverted_blurred=255-blurred
pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)

#now we are ready to display the pencil_Skecth.
cv2.imshow("Original Image",image)
cv2.imshow("SKecth Image",pencil_sketch)
cv2.waitKey(0)