import cv2

camera = cv2.VideoCapture(0)
if camera.isOpened():
    while True:
        success, frame = camera.read()
        if success:
            cv2.imshow("test", frame)
            if cv2.waitKey(1) == 27:
                break
        else:
            print("Unable to grab frame")
            break
cv2.destroyAllWindows()
