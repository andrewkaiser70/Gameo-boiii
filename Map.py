import pygame
import random
import time
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


clock = pygame.time.Clock()

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
Color = (Red,Green,Blue,Yellow)

vertices = (
		(-1,1,50),
		(1,1,50),
		(1,1,-50),
		(-1,1,-50),
		)
def ceiling_floor(side,startx,startz,width,length): #side=1=ceiling, side=-1=floor
	vertices = (
		(-startx,side,startz),
		((-startx+width),side,startz),
		((-startx+width),side,-(startz+length)),
		(-startx,side,-(startz+length)),
		)
	return vertices
def side_wall(startx,startz,height,length): #side is positive for right side, negative for left
	vertices = (
		(startx,(height/2),startz), 
		(startx,-(height/2),startz),
		(startx,-(height/2),-(startz+length)),
		(startx,(height/2),-(startz+length)),
		)
	return vertices
def front_wall(startx,startz,height,length):
	vertices = (
		(-startx,(height/2),startz),
		(-startx,-(height/2),startz),
		(-startx+length,-(height/2),startz),
		(-startx+length,(height/2),startz),
		)
	return vertices
def Plane(plane_type,color,startx,startz,height,length): 
	if plane_type == 0: # side wall
		vertices = side_wall(startx,startz,height,length)
	elif plane_type == 1: #front/back wall
		vertices = front_wall(startx,startz,height,length)
	elif plane_type == 2: #floor
		vertices = ceiling_floor(-1,startx,startz,height,length) #height is actually width
	elif plane_type == 3: #ceiling
		vertices = ceiling_floor(1,startx,startz,height,length) #height is actually width
	
	glBegin(GL_QUADS)
	x =0
	for vertex in vertices:
		glColor3fv(Color[x])
		glVertex3fv(vertex)
		x+=1
	glEnd()

def Maze():
	Plane(0,White,1,1,2,1)
	Plane(0,White,-1,1,2,1)
	Plane(2,Red,1,1,2,1)
	Plane(3,Blue,1,1,2,1)
	Plane(1,Black,1,-1,2,2)
def main():
	pygame.init()
	display_width = 1000
	display_height = 700

	gameDisplay = (display_width,display_height)
	pygame.display.set_caption('Map')
	pygame.display.set_mode(gameDisplay,DOUBLEBUF|OPENGL)


	gluPerspective(
		50, # field of view in degrees
		(gameDisplay[0]/gameDisplay[1]), # aspect ratio
		.25, # near clipping plane
		200, # far clipping plane
	)
	glTranslatef(0,0,-5)
	y = 1
	in_loop = True
	while in_loop:
		x = glGetDoublev(GL_MODELVIEW_MATRIX) #where the camera is
		camera_x = x[3][0]
		camera_y = x[3][1]
		camera_z = x[3][2]

		#FIX CAMERA MOVES WITH MOUSE
		#delmouspos = pygame.mouse.get_rel()
		#print(camera_z)
		#gluLookAt(camera_x,camera_y,camera_z,camera_x+delmouspos[0],camera_y+delmouspos[1],camera_z,0,1,0)
		
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				in_loop = False
		if keys[K_ESCAPE]:
			in_loop = False
		if keys[K_LEFT]:
			glRotatef(-1,0,1,0) #Rotate the camera left
		if keys[K_RIGHT]:
			glRotatef(1,0,1,0) #Rotate the camera right
		'''
		FIX LOOKING UP AND DOWN USING KEYS
		if keys[K_UP]:
			if y > -60: #max viewing angle up
				glRotate(-1,1,0,0) #Rotate the camera up
				y-=1
		if keys[K_DOWN]:
			if y < 60: #max viewing angle down
				glRotatef(1,1,0,0) #Rotate the camera down
				y+=1
		'''
		if keys[K_w]:
			glTranslatef(0,0,.1) #Move camera forward
		if keys[K_s]:
			glTranslatef(0,0,-.1) #Move camera back
		if keys[K_a]:
			glTranslatef(.1,0,0) #Move camera left
		if keys[K_d]:
			glTranslatef(-.1,0,0) #Move camera right
		#glRotatef(0,1,1,1) #degrees
			'''
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1) #Zooming in
				if event.button == 5:
					glTranslatef(0,0,-1) #Zooming out
			'''
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clears after each frame to stop overlap

		Maze()

		pygame.display.flip() #update display
		pygame.time.wait(10) #"speed? FPS?"

main()
pygame.quit()
quit()