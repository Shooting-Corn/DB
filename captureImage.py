import cv2
import datetime
import time

cap = cv2.VideoCapture("parasite_test.mp4")

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS) 
print(fps)    ## 29.97
prevTime = time.time()

while(cap.isOpened):
    ret, frame = cap.read()
    if ret == False:
        break
    ## imshow() 팝업창을 띄워 하나의 프레임을 출력하는 함수 
    cv2.imshow("video capture", frame)
    now = datetime.datetime.now().strftime("%d-%H-%M-%S")
    ## 33ms 동안 특정 입력이 들어 올때까지 대기 
    '''
    cv.waitKey() 함수는 프레임을 표출하는 시간을 정의합니다. 
    이때 단위는 밀리초, 즉 천분의 1초가 됩니다. 
    현재 otter.avi의 FPS는 24입니다. 
    초당 24 프레임으로 구성되어 있으니 1000밀리초 당 24 프레임, 역산하면 프레임 당 약 42 밀리초를 표출하고 있습니다. 
    이때 if 문은 프레임 당 42 밀리초를 표출하되, 'q'가 입력되었을 때는 프레임 표출이 종료되도록 설정하고 있습니다.
    '''
    key = cv2.waitKey(int(1000/fps))

    curTime = time.time()
    sec = curTime - prevTime
    if sec >= 5:
        cv2.imwrite("test/test_" + now + ".jpg", frame)
        prevTime = curTime
    ## 27은 esc key 
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()