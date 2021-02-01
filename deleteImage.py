import cv2   # OpenCV
from skimage.metrics import structural_similarity as ssim
import os
import pandas as pd

photo_list = []
for f in os.listdir('kiss scene'):
    photo_list.append(f)

photo_size = list(map(lambda x: os.path.getsize('kiss scene/' + x), photo_list))
fsp = pd.DataFrame({'filename':photo_list, 'size':photo_size})

print('사진의 갯수 :', len(fsp))

# Photo Value Counts
pvc = pd.DataFrame({'filename':fsp['filename'].value_counts().index, 'fn_counts':fsp['filename'].value_counts().values})   
psvc = pd.DataFrame({'size':fsp['size'].value_counts().index, 'size_counts':fsp['size'].value_counts().values})   

fsp = pd.merge(fsp, pvc, how = 'left', on = 'filename')
fsp = pd.merge(fsp, psvc, how = 'left', on = 'size')

fsp.sample(2)
fsp_nsn = fsp.sort_values(['filename'], ascending = False).drop_duplicates(['filename'], keep = 'first')
pvc_nsn = pd.DataFrame({'filename':fsp_nsn['filename'].value_counts().index, 'fn_counts_nsn':fsp_nsn['filename'].value_counts().values})   
psvc_nsn = pd.DataFrame({'size':fsp_nsn['size'].value_counts().index, 'size_counts_nsn':fsp_nsn['size'].value_counts().values})   

fsp_nsn = pd.merge(fsp_nsn, pvc_nsn, how = 'left', on = 'filename')
fsp_nsn = pd.merge(fsp_nsn, psvc_nsn, how = 'left', on = 'size')
# 삭제될 사진의 리스트
delete = []


for i in range(len(psvc_nsn)):
    
    # 중복된 크기(size)가 있는 경우
    if psvc_nsn['size_counts_nsn'][i] == 2:
        
        # 그 크기에 해당하는 사진을 불러온다. 
        temp = fsp_nsn[fsp_nsn['size']==psvc_nsn['size'][i]].reset_index(drop = True).sort_values(['filename'])
        
        # 사진 읽기
        imageA = cv2.imread('kiss scene/'+temp['filename'][0])
        imageB = cv2.imread('kiss scene/'+temp['filename'][1])
        (H,W, E) = imageA.shape
        imageB = cv2.resize(imageB, (W,H))
        
        # 이미지를 grayscale로 변환
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        
        # 이미지의 구조가 같다면 이미지 비교
        if len(grayA)==len(grayB):
            (score, diff) = ssim(grayA, grayB, full=True)
            
            # 차이가 없다면 하나는 delete에 넣어주기
            if score == 1:
                delete.append(temp['filename'][1])
            
            # 구조가 같지만 차이가 존재한다면 직접 확인하기     
            else:
                print('확인해보시오! : ', temp['filename'][0], '/', temp['filename'][1], f'(score : {score})')

# 중복제거된 것들은 delete 리스트에 넣어주기
delete = delete + list(fsp[~fsp['filename'].isin(fsp_nsn['filename'])]['filename'])

print('삭제할 목록 :', len(delete))
print(delete)