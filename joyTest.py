import pygame
import math
import sys
import time
#import pyglet

pygame.init()
pygame.joystick.init()    
js = pygame.joystick.Joystick(0)
js.init()

while True:
    pygame.event.pump()
    jx = js.get_axis(0)    
    print('axis 0: ' + str(jx))
    time.sleep(5)
    pygame.event.clear()
