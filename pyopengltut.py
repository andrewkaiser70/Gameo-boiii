import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

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
def Cube():
	glBegin(GL_LINES) #What are we making inside
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex]) #connects nodes using glVertex3fv and does what we specified above
	glEnd()

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #second input tells that we are using openGL

	gluPerspective(45,(display[0]/display[1]), 0.1, 50.0) #FOV in degrees, aspect ratio, clipping plane (where the object stops)

	glTranslatef(0.0,0.0,-5) #Moving about the object (don't want face on thus -5)
	glRotatef(0,0,0,0) #degrees

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glRotatef(1,0,1,1) #degrees
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clears after each frame
		Cube()
		pygame.display.flip() #update display
		pygame.time.wait(10) 

main()


