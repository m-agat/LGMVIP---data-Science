import cv2

'''Load the image'''
image = cv2.imread("kitten.jpg")

'''Convert to grey scale and resize'''
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''Convert to negative image (inversion)'''
inverted_image = 255 - grey_image

'''Blurred image'''
blurred_image = cv2.GaussianBlur(inverted_image, (15,15), 0)


'''Pencil sketch'''
def pencil_sketch(img, blurred_img):
    return cv2.divide(img, 255 - blurred_img, scale=256)


pencil_skch = pencil_sketch(grey_image, blurred_image)

#resizing
scale = 0.3
height = int(grey_image.shape[0]*scale)
width = int(grey_image.shape[1]*scale)
dimensions = (width, height)
pencil_sketch_resized = cv2.resize(pencil_skch, dimensions)

'''Show image'''
cv2.imshow("Pencil sketch", pencil_sketch_resized)
cv2.waitKey(0)
