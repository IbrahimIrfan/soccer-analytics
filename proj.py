import numpy as np
import cv2

casc = cv2.CascadeClassifier("haarcascade_eye.xml")
#cap = cv2.VideoCapture("data.mp4")
cap = cv2.VideoCapture(0);

fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ppl = casc.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in ppl:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    #fgmask = fgbg.apply(frame)
    #cv2.imshow("frame", fgmask)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
