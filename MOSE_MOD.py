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
from OP_K1 import op_key


class Mose:
    def __init__(self,v1: int,v2: int):

        self.x=v1

        self.y=v2


    def mose (self):

        if self.x is not None:

            if self.y is not None:

                self.x = round(self.x)

                self.y = round(self.y)

                print(self.x)

                print(self.y)

                if self.x < (1920 / 3):

                    self.x = self.x - 70
                if self.y > (720):
                    self.y = self.y + 60
                if self.y < (620):
                    self.y = self.y - 60
                if self.x > (1280):

                    self.x = self.x + 70

                if self.x > 1910:

                    self.x = 1910



    def mous_move(self):

        try:
            if self.x is not None:

                if self.y is not None:

                    if self.x > 1915:

                        self.x = 1915

                    if self.x < 10:

                        self.x = 10

                    if self.y > 1070:

                        self.y = 1070

                    if self.y < 10:

                        self.y = 10

                    autopy.mouse.move(self.x, self.y)

        except:

            print("erre mose")