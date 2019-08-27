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
import psutil


class op_key:


    def opk(self) -> object:
        com: str = "start OptiKey.exe"
        os.system(com)




    def opt_kill(self):
        com: str = "killtask OptiKey.exe"
        os.system(com)



    def op_ch(self):
        processName='OptiKey'
        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return True;