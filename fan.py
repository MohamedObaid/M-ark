import multiprocessing
import sys
import time
from win32api import GetSystemMetrics

import cv2
import numpy as np
import pygame
import pygame.freetype

from MOSE_MOD import Mose
from OP_K1 import op_key

pygame.init()
s1 = GetSystemMetrics(0)

s2 = GetSystemMetrics(1)
aj_V1 = 10.5
aj_V2 = 5.68


class eye():
    def ey_modl(self):
        pygame.init()
        cl = pygame.time
        time.sleep(2)
        cap = cv2.VideoCapture(1)  # 'e1.avi' 'ey2.mp4' 'output.avi' 'output100.avi'hello'output100.avi'

        # fourcc = cv2.VideoWriter_fourcc(*'XVID')

        # out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

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
            #   out.write(frame)
            frame = cv2.flip(frame, 1)
            frame = frame[200:400, 200:400]
            # frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.4)
            imgxx = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            imgxx = cv2.equalizeHist(imgxx)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))
            imgxx = clahe.apply(imgxx)

            bo = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

            im_bw = cv2.threshold(imgxx, 80, 90, cv2.THRESH_TRUNC)[1]

            cimg = cv2.cvtColor(im_bw, cv2.COLOR_GRAY2BGR)
            s1 = cv2.cvtColor(cimg, cv2.COLOR_RGB2GRAY)
            img = cv2.medianBlur(s1, 5)
            cv2.imshow(' medianBlur', img)
            cl.delay(70)
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                                       param1=40, param2=25, minRadius=20, maxRadius=40)
            if circles is not None:
                x = np.around(circles)
                circles = np.uint16(x)
                for i in circles[0, :]:
                    # draw the outer circle
                    # cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

                v1 = i[0] * aj_V1
                v2 = i[1] * aj_V2
                if (i[0] * aj_V1) > 1900:
                    v1 = 1910
                if (i[1] * aj_V2) > 1050:
                    v2 = 1060

                obj_mo = Mose(v1, v2)
                obj_mo.mose()
                obj_mo.mous_move()


            else:
                im_bw = im_bw
            cv2.imshow('detected circles not', frame)
            cv2.imshow('lanv', bo)
            cv2.imshow('ex ', s1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

                cap.release()
                cv2.destroyAllWindows()

    # +------------------------


def ey_cl():
    w = GetSystemMetrics(0)

    h = GetSystemMetrics(1)
    size = w, h

    x = 300

    y = 240

    cl = pygame.time

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption('Eye-keyboered')

    obj = pygame.image.load('BAK.png')

  #  GAME_FONT = pygame.freetype.Font("XX.ttf", 24)

    obj_c = pygame.image.load('MC_t1.png')

   # obj_c = pygame.transform.scale(obj_c, (64, 64))

    #obj_a = pygame.image.load('x.png')

    xx, yy = 300, 300

    #str = "Hello World!"

    obj = pygame.transform.scale(obj, (size))
    flg = 0
    flg1 = 0
    flg2 = 0
    flg3 = 0
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    k = 0
    k1 = 0
    k2 = 0
    k3 = 0
    co = 0
    # /////////////////////////////////////////

    m = 800

    n = 480

    im_bw = np.zeros((n, m))

    # /////////////////////////////////////////

    cap = cv2.VideoCapture(1)  # 'output100.avi'

    while (cap.isOpened() & co < 9):

        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)

        imgxx = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        imgxx = cv2.equalizeHist(imgxx)

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))

        imgxx = clahe.apply(imgxx)

        bo = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

        xxx = cv2.cvtColor(frame, cv2.COLOR_LAB2BGR)

        im_bw = cv2.threshold(imgxx, 80, 90, cv2.THRESH_TRUNC)[1]

        cimg = cv2.cvtColor(im_bw, cv2.COLOR_GRAY2BGR)

        s1 = cv2.cvtColor(cimg, cv2.COLOR_RGB2GRAY)

        img = cv2.medianBlur(s1, 5)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=40, param2=35, minRadius=10, maxRadius=40)
        if circles is not None:

            x = np.around(circles)
            print(circles)

            circles = np.uint16(x)

            for i in circles[0, :]:
                # draw the outer circle
                # cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
                k2 = i[0]
                k3 = i[1]
            cv2.imwrite('me.png', frame)

        objey = pygame.image.load('me.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            screen.fill((0, 0, 0))
        screen.blit(obj, (0, 0))

        if xx < 30 & flg == 0:
            xx = 100
            yy = 100
            if co == 1:
                x1.append(i[0])

            if co > 1:
                k = 1920 - 100
                if co == 3:
                    x2.append(i[0])

            if co > 4:
                k = 1920 - 100
                k1 = 1080 - 100
                if co == 3:
                    y1.append(i[1])  # i[]

            if co > 6:
                k = 0
                k1 = 1080 - 100

                if co == 7:
                    y2.append(i[1])  # i[]

            if co > 7:
                k = 1920 / 2
                k1 = 1080 / 2
            co = co + 1

            if co > 8:
                screen = pygame.display.set_mode((1000, 555))

                cap.release()
                cv2.destroyAllWindows()

                flg1 = 1
                break
                pygame.quit()

        if flg1 == 0:
            obj_a = pygame.image.load('cc.png')
            obj_a = pygame.image.load('x.png')
            obj_a = pygame.transform.scale(obj_a, (xx, yy))

            # text_surface, rect = GAME_FONT.render(str, (0, 0, 0))
            # str+='a'

            # screen.blit(text_surface, (10, 5))
            # screen.blit(obj_c, (mx-32,my-32))

            screen.blit(objey, (500, 200))

            screen.blit(obj_a, (k, k1))

            screen.blit(obj_a, (k, k1))

            pygame.display.update()

        if flg == 0:
            xx = xx - 5
            yy = yy - 5

        pygame.display.update()

        if (flg1 == 1):
            cl.delay(50)

        #    xx1 = 200  # min(x1)

         #   xx2 = 200  # max(x2)

          #  yy1 = 200  # min(y1)

           # yy2 = 200  # max(y2)
            pygame.quit()

    pygame.quit()


try:
    ey_cl()
    key = op_key()
    ey = eye()

    p1 = multiprocessing.Process(target=key.opk())

    p2 = multiprocessing.Process(target=ey.ey_modl())

    p1.start()

    p1.join()

    p2.start()


    p2.join()

except:
    print("errer")
