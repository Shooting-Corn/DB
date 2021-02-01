import os 

path_dir = 'kiss scene/image_kiss scene'
file_list = os.listdir(path_dir)

file_list.sort()
for i in file_list:
    print("data/images/" + i)