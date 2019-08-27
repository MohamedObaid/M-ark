import pygame
import sys
import pygame.freetype
import cv2
from pygame.locals import *



pygame.init()
size = w,h,=920,820
x=300
y=240
cl = pygame.time
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Eye-keyboered')
obj = pygame.image.load('KEY_t1.jpg')
GAME_FONT = pygame.freetype.Font("XX.ttf", 24)

obj_c = pygame.image.load('MC_t1.png')
obj_c = pygame.transform.scale(obj_c,(64,64))
obj_a= pygame.image.load('x.png')
xx,yy=300,300
str="Hello World!"
obj = pygame.transform.scale(obj,(size))
while 1:
    mx,my=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        screen.fill((0,0,0))
    screen.blit(obj, (0, 0))
    if xx < 30:
        xx = 100
        yy = 100
        obj_a.image.fill((0,0,0))
        obj_a = pygame.image.load('cc.png')
    obj_a = pygame.image.load('x.png')
    obj_a = pygame.transform.scale(obj_a, (xx, yy))
    text_surface, rect = GAME_FONT.render(str, (0, 0, 0))
    str+='a'


    screen.blit(text_surface, (10, 5))
    #screen.blit(obj_c, (mx-32,my-32))
    screen.blit(obj_a, (mx - yy, my - xx))
    screen.blit(obj_a,(mx - yy, my - xx))
    pygame.display.update()


    xx = xx-5
    yy = yy-5


    pygame.display.update()
