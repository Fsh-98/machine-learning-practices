import os
import cv2
import glob

folders = glob.glob('E:\\Celeb_DF\\train\\real')

videonames_list = []
for folder in folders:
    for f in glob.glob(folder+'/*.mp4'):
      videonames_list.append(f)
      print(f)
print('There are {} videos in Folder'.format(len(videonames_list)))

count = 0
for i in range(0,len(videonames_list)):
  video_data = videonames_list[i]
  video = cv2.VideoCapture(video_data)
  success = True
  while success:
    success,image = video.read()
    name = 'E:\\Celeb_DF\\train\\real_frames'+str(count)+'.jpg'
    if success == True:
      cv2.imwrite(name,image)
      print('Frame {} Extracted Successfully'.format(count))
      count+=1
    else:
      i = i+1  
    i = i+1
  print('\n\n\nVideo {} Extracted Successfully\n\n\n'.format(video_data))


