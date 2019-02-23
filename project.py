import numpy as np
import cv2

track_parameters = dict(maxCorners=100, 
                        qualityLevel=0.3,
                        minDistance=7, 
                        blockSize=7)
lk_parameters = dict(winSize=(200, 200), 
                     maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS |
                              cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                     
cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

prev_pts = cv2.goodFeaturesToTrack(prev_gray, **track_parameters)
mask = np.zeros_like(prev_frame)

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if len(prev_pts)<10:
        prev_pts = cv2.goodFeaturesToTrack(prev_gray, **track_parameters)

    next_pts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, 
                                                     frame_gray,
                                                     prev_pts, 
                                                     None,
                                                     **lk_parameters)
    good_new = next_pts[status==1]
    good_prev = prev_pts[status==1]                                                     

    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()
        mask = frame = cv2.circle(frame, (x_new, y_new), 8, (0, 255, 0), -1)
    
    img = cv2.add(frame, mask)
    cv2.imshow('1', img)

    k = cv2.waitKey(30) & 0xFF
    if k==27:
        break
    
    prev_gray = frame_gray.copy()
    prev_pts = good_new.reshape(-1, 1, 2)

cv2.destroyAllWindows
cap.release