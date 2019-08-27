import numpy as np
import cv2
import pywin
import autopy
import pygame
import PIL
from numba import vectorize, cuda

class Cam:
    def cam_aj(self):
        pygame.init()
        cap = cv2.VideoCapture(1)  # 'e1.avi' 'ey2.mp4'

        cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)

        cv2.namedWindow(' medianBlur', cv2.WINDOW_NORMAL)

        cv2.namedWindow('ex ', cv2.WINDOW_NORMAL)

        cv2.namedWindow('lanv', cv2.WINDOW_NORMAL)

        m = 480
        n = 640
        im_bw = np.zeros((n, m))
        while (cap.isOpened()):

            ret, frame = cap.read()
            img = cv2.flip(frame, 1)
            height = img.shape[0]
            width = img.shape[1]
            channels = img.shape[2]
            im = frame
            roi = im[200:350, 250:400]
            cv2.imshow('this', roi)

            print('Image Height       : ', height)
            print('Image Width        : ', width)
            print('Number of Channels : ', channels)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

                cap.release()
                cv2.destroyAllWindows()

obj=T()
obj.cam_aj()