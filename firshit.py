import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
image_w = 100
image_h = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Punch City')


clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

Image = pygame.image.load('poop.jpg')
Image = pygame.transform.scale(Image,(image_w,image_h))

def rando():
	color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
	return color

def emoji(x,y):
	gameDisplay.blit(Image,(x,y))

def crash():
	message_display('You done ducked up and crashed your Dad\'s car',black,25,(display_width/2),(display_height/2))
	pygame.display.update()
	time.sleep(2)	#pauses for 2 sec

def message_display(text,color,size,dimx,dimy):
	Texttype = pygame.font.Font('freesansbold.ttf', size) #Font and size, respectively
	TextSurf,TextRect = text_objects(text,color,Texttype)
	TextRect.center = (dimx,dimy)
	gameDisplay.blit(TextSurf,TextRect)

def things_dodged(count):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def text_objects(text,color,font):
	textSurface = font.render(text,True,color)
	return textSurface, textSurface.get_rect()

def rect(rectx,recty,rectw,recth,color):
	pygame.draw.rect(gameDisplay,color,[rectx,recty,rectw,recth])

def makebutton(text,textcolor,textsize,rectx,recty,rectw,recth,rectcolor,event):
	rect(rectx,recty,rectw,recth,rectcolor)
	message_display(text,textcolor,textsize,(rectx+rectw/2),(recty+recth/2))

	mouse = pygame.mouse.get_pos() #array of [x_pos,y_pos] of 
	if rectx < mouse[0] < rectx+rectw and recty < mouse[1] < recty+recth:
		rect(rectx,recty,rectw,recth,textcolor)
		message_display(text,rectcolor,textsize,(rectx+rectw/2),(recty+recth/2))
		if event.type == pygame.MOUSEBUTTONDOWN:
			return True
	return False

def paused():
	pause = True
	Cont = False
	Quit = False
	Restart = False

	gameDisplay.fill(white)
	message_display('Game Paused',black,50,(display_width/2),(display_height/3))
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pause = False	
			Cont = makebutton('Continue',rando(),20,200,450,100,50,black,event)
			Quit = makebutton('Quit.',rando(),20,(display_width-300),450,100,50,black,event)
			Restart = makebutton('Restart.',rando(),20,(display_width-450),400,100,50,black,event)
			pygame.display.update()
		if Cont == True:
			return 1
		if Quit == True:
			return 2
		if Restart == True:
			return 3
	return 2
def game_intro():
	intro = True
	Go = False
	Quit = False

	gameDisplay.fill(rando())
	message_display('Welcome to Punch City',black,50,(display_width/2),(display_height/3))
	while intro == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False			
			Go = makebutton('Go!',rando(),20,200,450,100,50,black,event)
			Quit = makebutton('Quit.',rando(),20,(display_width-300),450,100,50,black,event)
		if Go == True:
			return True
		if Quit == True:
			return False

		pygame.display.update()
		clock.tick(15)


def game_loop():
	x = (display_width*.45)
	y = (display_height*.8)
	x_change = 0
	y_change = 0
	rect_startx = random.randrange(0,display_width)
	rect_starty = -600
	rect_speed = 7
	rect_width = 100
	rect_height = 100
	color = rando()
	dodged = 0

	quit = game_intro()
	while quit == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = +5
				elif event.key == pygame.K_DOWN:
					y_change = +5
				elif event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_p:
					query = paused()
					if  query == 1:
						x_change = 0
					elif query == 2:
						quit = False
					elif query == 3:
						return True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0
		x += x_change
		y += y_change
		gameDisplay.fill(white)

		rect(rect_startx,rect_starty,rect_width,rect_height,color)
		rect_starty += rect_speed
		emoji(x,y)

		if x > display_width - image_w or x<0 or y > display_height - image_h or y<0:
			crash()
			return True
		if y < rect_starty+rect_height and y> rect_starty or y+image_h>rect_starty and y+image_h<rect_starty+rect_height:
			if x > rect_startx and x < rect_startx+rect_width or x+image_w > rect_startx and x+image_w < rect_startx+rect_width:
				crash()
				return True

		if rect_starty > display_height:
			rect_starty = 0 - rect_height
			rect_startx = random.randrange(0,display_width)
			dodged += 1
			rect_speed += 1
			rect_width += (dodged*1.2)
			#rect_height += (dodged*1.2)
			color  = rando()
		things_dodged(dodged)
		pygame.display.update()
		clock.tick(60) #Game framerate
	return False

Playing = True
while Playing == True:
	Playing = game_loop()

pygame.quit()
quit()