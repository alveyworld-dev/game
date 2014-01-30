import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600,600))

gravity = .2
velocity = 0
jump_power = 10

sprite = pygame.image.load("sprite.png")
spriterect = sprite.get_rect()
spriterect.x = 30
spriterect.y = 30
jumping = None

key = pygame.key.get_pressed()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()

		if event.type == pygame.KEYDOWN and jumping == False:
			jumping = True
			velocity -= jump_power
			spriterect.y += velocity
        
	if spriterect.bottom >= 570:
		spriterect.bottom = 570
		jumping = False
		velocity = 0
	if not spriterect.bottom == 570:
		velocity += gravity
		spriterect.y += velocity

	screen.fill((100,100,100))	
	screen.blit(sprite,spriterect)
	pygame.display.flip()