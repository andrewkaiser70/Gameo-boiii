import pygame
import random
import time
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

pygame.init()
clock = pygame.time.Clock()

Filename = 'wall.jpg'

image_w = 100
image_h = 100
Black = (0.0, 0.0, 0.0)
Red = (1.0, 0.0, 0.0)
Yellow = (1.0, 1.0, 0.0)
Green = (0.0, 1.0, 0.0)
Cyan = (0.0, 1.0, 1.0)
Blue = (0.0, 0.0, 1.0)
Magenta = (1.0, 0.0, 1.0)
White = (1.0, 1.0, 1.0)
Grey = (0.5, 0.5, 0.5)
Colors = (Red,Green,Blue,Yellow)


vertices = (
		(-1,1,0),
		(1,1,0),
		(1,-1,0),
		(-1,-1,0),
		)
def Window(width,height):
	gameDisplay = (width,height)
	pygame.display.set_mode(gameDisplay,DOUBLEBUF|OPENGL)
	glClearColor(0,0,0,0)
	gluPerspective(
		50, # field of view in degrees
		(width/height), # aspect ratio
		.1, # near clipping plane
		200, # far clipping plane
	)
	glShadeModel(GL_SMOOTH); #Enables Smooth Shading
	glClearDepth(1) #depth buffer setup
	glEnable(GL_DEPTH_TEST) #Enables depth testing
	glDepthFunc(GL_LEQUAL) #Type of depth test
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST); #nice persepective calcs, may slow down

	glTranslatef(0,0,-5)

def Texture(filename):
	Image = pygame.image.load(filename)
	data = pygame.image.tostring(Image,"RGBA",1)
	ix = Image.get_width()
	iy = Image.get_height()

	texture = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D,texture)
	glPixelStorei(GL_UNPACK_ALIGNMENT,1)
	glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,ix,iy,0,GL_RGBA,GL_UNSIGNED_BYTE,data)
	glGenerateMipmap(GL_TEXTURE_2D)

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

def Square():

	glBegin(GL_QUADS) #What are we making inside
	x=0
	for vertex in vertices:
		glColor3fv(Colors[x])
		glVertex3fv(vertex)
		x+=1
	glEnd()




def Main():
	
	display_width = 1000
	display_height = 700

	Window(display_width,display_height)

	in_loop = True
	while in_loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				in_loop = False

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		Square()
		pygame.display.flip()

Main()
pygame.quit()
quit()