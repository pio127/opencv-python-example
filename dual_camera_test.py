import cv2

camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)

if camera1.isOpened() and camera2.isOpened():
    while True:
        success1, frame1 = camera1.read()
        success2, frame2 = camera2.read()
        if success1 and success2:
            cv2.imshow("camera 1", frame1)
            cv2.imshow("camera 2", frame2)
            if cv2.waitKey(1) == 27:
                break
        else:
            print("Unable to grab frame")
            break
cv2.destroyAllWindows()
