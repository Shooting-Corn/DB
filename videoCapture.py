###pharsing

import cv2
import os
num = 0
print(cv2.__version__)
#vidcap = cv2.VideoCapture('/content/gdrive/My Drive/darknet_detect/video/gun_video.mp4')
vidcap = cv2.VideoCapture("parasite_test.mp4")
fps = vidcap.get(cv2.CAP_PROP_FPS) 
success,image = vidcap.read()
count = 0
save_count = 0
success = True
while success:
    if(int(vidcap.get(1)) % int(fps*5) == 0):
        #print('Saved frame number : ' + str(int(vidcap.get(1))))

        #path = '/content/gdrive/My Drive/darknet_detect/video_cut/'
        path = 'test2/'
        num += 1
        cv2.imwrite(os.path.join(path, "new_frame%d.png" % num), image)  
        save_count += 1
    success,image = vidcap.read()
    #print ('Read a new frame: ', success)
    count += 1