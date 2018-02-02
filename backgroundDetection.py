import numpy as np
import cv2

cap = cv2.VideoCapture("data.mp4")
w = cap.get(3)
h = cap.get(4)

out = cv2.VideoWriter('out.avi',cv2.VideoWriter_fourcc(*'XVID'), 10, 10, (int(w),int(h)))

#cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame)

    kernel = np.ones((2,2), np.uint8)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    blur = cv2.medianBlur(opening, 5)

    im2, contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cont in contours:
        area = cv2.contourArea(cont)
        if area > 30 and area < 700:
            cv2.drawContours(frame, cont, -1, (0,0,255), 3)

    out.write(frame)

    cv2.imshow("frame2", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
