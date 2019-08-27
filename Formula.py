from typing import Any, Union

import numpy as np
import cv2
import pywin
import autopy
import pygame
import os
import multiprocessing
import sys
import pygame.freetype
from win32api import GetSystemMetrics
import cv2
import numpy as np
from numba import vectorize, cuda
import autopy
from pygame.locals import *
import time


class Form:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def cut(self):
        try:
            x1 = min(self.x1)
            x2 = max(self.x2)
            y1 = min(self.y1)
            y2 = max(self.y2)
            if (x2 - x1) > 210:
                if (y2 - y1) > 210:
                    cut_num: int = int(x1), int(x2), int(y1), int(y2)
                    return cut_num
            else:
                cut_num = 200, 400, 200, 400
                return cut_num
        except:
            cut_num = 200, 400, 200, 400
            return cut_num

    def Mar(self,cut):
       try:
           s1 = GetSystemMetrics(0)

           s2 = GetSystemMetrics(1)

           x1,x2,y1,y2 = cut
           s1:int=int(s1)
           s2:int=int(s2)
           v1=x2-x1
           v2=y2-y1
           p1=v1/s1
           p2=v2/s2
           x=p1+(p1/(1/10))
           y=p2+(p2/(1/10))
           re=x,y
           return re
       except:
           aj_V1 = 10.5
           aj_V2 = 5.68
           re=aj_V1,aj_V2
           return re


