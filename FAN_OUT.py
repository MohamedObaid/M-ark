import numpy as np
import cv2
import pywin
import autopy
import pygame

pygame.init()
cl = pygame.time
cap = cv2.VideoCapture(1)  #'e1.avi' 'ey2.mp4' 'output.avi'

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('outputxxx1.avi',fourcc, 20.0, (640,480))


cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)
cv2.resizeWindow("detected circles", 800, 480)

cv2.namedWindow(' medianBlur', cv2.WINDOW_NORMAL)
cv2.resizeWindow(' medianBlur', 800, 480)



cv2.namedWindow('ex ', cv2.WINDOW_NORMAL)
cv2.resizeWindow('ex ', 800, 480)

cv2.namedWindow('lanv', cv2.WINDOW_NORMAL)
cv2.resizeWindow('lanv', 800, 480)

m = 800
n = 480
im_bw = np.zeros((n, m))
while (cap.isOpened()):

    ret, frame = cap.read()
    out.write(frame)
    frame= cv2.flip(frame, 1)
    frame = frame[200:400, 200:400]
    #frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.4)
    imgxx = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))
    imgxx = clahe.apply(imgxx)


    bo = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    xxx = cv2.cvtColor(frame, cv2.COLOR_LAB2BGR)

    im_bw = cv2.threshold(imgxx, 80, 90, cv2.THRESH_TRUNC)[1]

    cimg = cv2.cvtColor(im_bw, cv2.COLOR_GRAY2BGR)
    s1 = cv2.cvtColor(cimg,cv2.COLOR_RGB2GRAY)
    img = cv2.medianBlur(s1, 5)
    cv2.imshow(' medianBlur',img)
    cl.delay(40)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=40, param2=25, minRadius=20, maxRadius=40)
    if circles is not None:
        x = np.around(circles)

        circles = np.uint16(x)
        for i in circles[0, :]:
            # draw the outer circle
           # cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
            print((i[0]*10.6))
            print((i[1]*10))
        if (i[0]*10.6 ) <1900:
            if (i[1]*5.6)<1050:
                a=int(((i[0])*10.5))
                b=int(i[1]*5.6)
                print(a)
                print(b)
                #autopy.mouse.move(a, b)

    else:
        im_bw=im_bw
    cv2.imshow('detected circles not', frame)
    cv2.imshow('lanv', bo)
    cv2.imshow('ex ', s1)





    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        cap.release()
        cv2.destroyAllWindows()