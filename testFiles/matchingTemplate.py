import numpy as np
import cv2

cap = cv2.VideoCapture(0)
template = cv2.imread("droid.jpg",0)
threshold = 0.7
w, h = template.shape[::-1]

while(True):
    _, frame = cap.read()
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt, (pt[0]+w, pt[1] + h), (0,255,255), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
