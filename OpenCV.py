import cv2

img = cv2.imread('1.png')
print(img)
# img = cv2.resize(img, (500, 500))
print(img.shape)


cv2.imshow('Somthing here', img)
cv2.waitKey(5000)