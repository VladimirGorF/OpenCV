import cv2
# тут лежат все варианты обнаружения разных объектов  https://github.com/opencv/opencv.git  путь opencv/data/haarcascades/   
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('faces.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #делаем картинку серой типо так лучше работает программа, но вроде и так работает

faces = face_cascades.detectMultiScale(img_gray)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w,  y + h), (255, 0, 255), 2)   # рисуем прямоугольник \ где\ ккоординаты начала и конца\ цвет линии и ее толщина


cv2.imshow('Somthing Title here', img)
cv2.waitKey(10000)

# cap = cv2.VideoCapture(0)

# while True:
#     success, frame = cap.read()
#     # cv2.imshow('camera', frame)
#     img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #делаем картинку серой типо так лучше работает программа, но вроде и так работает
#     faces = face_cascades.detectMultiScale(img_gray)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w,  y + h), (255, 0, 255), 2)   # рисуем прямоугольник \ где\ ккоординаты начала и конца\ цвет линии и ее толщина

#     cv2.imshow('Somthing Title here', frame)

#     if cv2.waitKey(1) & 0xff == ord('q'):   #выход на букву q
#         break
