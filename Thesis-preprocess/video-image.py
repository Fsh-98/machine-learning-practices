import cv2
import os
import glob
vidcap = cv2.VideoCapture('D:\\Py files\\AAA - Thesis Codes\\Celeb-DF\\dataset\\test\\fake\\id0_id1_0002.mp4')
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite("D:\\Py files\\AAA - Thesis Codes\\Celeb-DF\\dataset\\test\\fake\\fake_frames\\frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    #print('Read a new frame: ', success)
    count += 1
