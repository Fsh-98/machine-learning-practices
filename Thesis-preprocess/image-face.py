import os

import cv2

image_path = "E:\\Celeb_DF\\train_real_frames"

count = 0
face_cascade = "D:\\Py files\\AAA - Thesis Codes\\Face Detection\\opencv-4.x\\data\\haarcascades\\haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(face_cascade)
# Iterate through files
for f in [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]:
    img = cv2.imread(os.path.join(image_path, f))
    for i, face in enumerate(cascade.detectMultiScale(img)):
        x, y, w, h = face
        sub_face = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join("E:\\Celeb_DF\\train_real_cropped", "{}_{}.jpg".format(f, i)), sub_face)
        count += 1





