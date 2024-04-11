import cv2

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) #videoCapture object
cv2.namedWindow("Live Video Capture")
while True:
    ret, frame = vid.read() #capture frames of video
    cv2.imshow('frame', frame)
    #press Q to exit the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
