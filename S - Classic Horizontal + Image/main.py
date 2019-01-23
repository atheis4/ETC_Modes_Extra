import os
import pygame
import time
import random
import glob

last_point = [0, 360]

images = []
image_index = 0

def setup(screen, etc):
    global images
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, etc):
    global last_point
    
    #knob1 = image size     
    #knob2 = y offset
    #knob3 = circle size
    #knob4 = circle color

    for i in range(0, 100) :
        seg(screen, etc, i)   
    

def seg(screen, etc, i):
    global last_point, images
    xoffset = 0
    y1 = int(etc.knob2 * 720) + (etc.audio_in[i] / 35)
    x = i * 13
    color = etc.color_picker()

    max_circle = 120
    image_size = 1
    circle_size = 0
    line_width = 0
    if etc.knob3 <=.5 :
        circle_size = int(etc.knob3 * max_circle)
        line_width = 0
    if etc.knob3 >.501 :
        circle_size = abs(max_circle-int(etc.knob3 * max_circle)) 
        line_width =  abs(30-int(etc.knob3 * 30))
        #if line_width == 0 : line_width = 1

    pygame.draw.circle(screen,color,(x + xoffset, y1),circle_size, line_width)

    image = images[0]
    image = pygame.transform.scale(image, (int(image.get_width() * etc.knob1), int(image.get_height() * etc.knob1)) )
    screen.blit(image, (x + xoffset, y1))
