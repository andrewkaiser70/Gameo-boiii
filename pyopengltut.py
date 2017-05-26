import pygame
import random
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

Black = (0.0, 0.0, 0.0)
Red = (1.0, 0.0, 0.0)
Yellow = (1.0, 1.0, 0.0)
Green = (0.0, 1.0, 0.0)
Cyan = (0.0, 1.0, 1.0)
Blue = (0.0, 0.0, 1.0)
Magenta = (1.0, 0.0, 1.0)
White = (1.0, 1.0, 1.0)
Grey = (0.5, 0.5, 0.5)
colors = (Blue,Green,Magenta,Yellow,Red,Blue)

vertices = (
	(1,-1,-1), #Node zero
	(1,1,-1),
	(-1,1,-1),
	(-1,-1,-1),
	(1,-1,1),
	(1,1,1),
	(-1,-1,1),
	(-1,1,1),
	)
edges = (
	(0,1), # (first node,end node at 1)
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7),
	)
surfaces = (
	(0,1,2,3), #groups nodes
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6),
	)
def Cube():
	glBegin(GL_QUADS) #What are we making inside
	
	for surface in surfaces:
		x = 0

		for vertex in surface:
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
			x+=1
	glEnd()
	glBegin(GL_LINES) #What are we making inside
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex]) #connects nodes using glVertex3fv and does what we specified above
	glEnd()

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #second input tells that we are using openGL

	gluPerspective(45,(display[0]/display[1]), 1, 50.0) #FOV in degrees, aspect ratio, clipping plane (where the object stops)

	glTranslatef(0,0,-5) #Moving about the object (don't want face on thus -5)
	glRotatef(0,0,0,0) #degrees

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-1,0,0) #Moving the object left
				if event.key == pygame.K_RIGHT:
					glTranslatef(1,0,0) #Moving the object right
				if event.key == pygame.K_UP:
					glTranslatef(0,1,0) #Moving the object up
				if event.key == pygame.K_DOWN:
					glTranslatef(0,-1,0) #Moving the object down
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1) #Zooming in
				if event.button == 5:
					glTranslatef(0,0,-1) #Zooming out


		#glRotatef(0,1,1,1) #degrees
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clears after each frame
		Cube()

		pygame.display.flip() #update display
		pygame.time.wait(10) 

main()


