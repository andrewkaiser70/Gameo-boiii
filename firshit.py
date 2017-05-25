import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
image_w = 100
image_h = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Donkey Dicks')

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
	message_display('You done fucked up and crashed your Dad\'s car') 
	game_loop()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',30) #Font and size, respectively
	TextSurf,TextRect = text_objects(text,largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)	#pauses for 2 sec

def things_dodged(count):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface, textSurface.get_rect()

def rect(rectx,recty,rectw,recth,color):
	pygame.draw.rect(gameDisplay,color,[rectx,recty,rectw,recth])

def game_loop():
	crashed = False
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


	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = +5
				elif event.key == pygame.K_DOWN:
					y_change = +5
				elif event.key == pygame.K_UP:
					y_change = -5
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
		things_dodged(dodged)
		emoji(x,y)

		if x > display_width - image_w or x<0 or y > display_height - image_h or y<0:
			crash()
		if y < rect_starty+rect_height and y> rect_starty or y+image_h>rect_starty and y+image_h<rect_starty+rect_height:
			if x > rect_startx and x < rect_startx+rect_width or x+image_w > rect_startx and x+image_w < rect_startx+rect_width:
				crash()

		if rect_starty > display_height:
			rect_starty = 0 - rect_height
			rect_startx = random.randrange(0,display_width)
			dodged += 1
			rect_speed += 1
			rect_width += (dodged*1.2)
			rect_height += (dodged*1.2)
			color  = rando()

		pygame.display.update()
		clock.tick(60) #Game framerate

game_loop()
pygame.quit()
quit()