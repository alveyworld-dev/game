

#Climbing
class climbing_block
	"""If player is dected in the collison of the block, if he press the UP key, he be able to go up with falling = off."""
	def __init__(self, block_blueprint, collusion = True, player.movement.y, texture)
		pygame.sprite.Sprite.__init__(self)
			if collusion(player + block) == True and pygame.KEYUP:
				game.alvey.jumping = False
				player.y = -10
			if collusion(player + Block) == True and pygame.KEYDOWN:
				pgame.alvey.jumping = False
				player.y = 10
			#Test code, and see what happen if jumping. Goal = Jump completely off ladder as same height without and bugs.
			#Also I'm not sure if there is a "falling = falses" or if it "Jumping = falses", or whatever that do with gravity
			#Also I i made theses variety of block from scratch (Not the program), so im not sure if it do well
#Death
class death_block
	"""If touched, player is automatic killed"""
	def __init__(self, block_blueprint,collusion, health,texture)
		pygame.sprite.Sprite.__init__(self)
		if collusion(Player + Block) == True
			player.health == 0

#Water
class water_block
	"""If inside water block, you fall slowly, you can "jump" and not slowly fall, and a lot slower"""
	def __init_(self, block_blueprint, collusion = True, player.movement, physic, texture)
		pygame.sprite.Sprite.__Inti__(self)
		if collusion(player + block) == True
			game.alvey.gravity = .45 # 1/2 of gravity
			game.alvey.speed = 7.5  # 1/4 of speed is lost
			game.alvey.jump_power = 3 # 1/4 of jump power, but since he underwater, he be connately "jumping" if spacebar is being hold		
		#Im probably missing something, but im not quire sure.

#Power_Up (Speed increase)
class Power_Up_Speed
	"""When touch, block will be automatically gone, speed increase by 1.5, jumping increase by 1.5, and can't be kill in 1 secound"""
		def __init_(self, block_blueprint, collusion = True, player.movement, physic, tex ture)
		pygame.sprite.Sprite.__Inti__(self)
		if collusion(player + block) == True
			#While something,something. Not sure, but basically it a code that make it so he has the power up for 15 seconds. But im not sure how code it.
				game.alvey.gravity = 9
				game.alvey.speed = 10*1.5
				game.alvey.jump_power = 12*1.5 
				#game.alvey.health = -1 #Not quite sure how make it so does it for a secound, also maybe also make it so he can't move for 1 sec.
				self.collosion = False #You can no longer gain more power
				self.texture = False #Whatever to make it so it disappears.

			
	








#Please Ignore, just keeping this code just incase we meed it again.

#import pygame
#class block(#pygame.sprite.Sprite):
	#"""The main blueprint all block should have"""
	#def __init__(self, x, y) #texture, physic, moving, properties)
			#pygame.sprite.Sprite.__init__(self) 
			#self.x=x
			#self.y=y
			#self.height=20
			#self.width=20	
			#self.rect=self.sprite.get_rect(x=self.x,y=self.y)
			#self.interaction = True
			#self.texture = texture
			#self.properties = properties
#Main block, Clossion = True, Physic = False, Moving = False, Properties = None
#Water block, Clossion = True (If player in clossion, slow speed x and y by 10, but also he can go throught it), moving = false
#Spike Block, clossion = True (If player in clossion, remove health, and give invisiablty frame, plus push toward side)
#for y in range(0,len(level1))
	#for x in range(0,len(level1[y]))
		#if (level1[x][y]==1) #0 = air, 1 = normal, 2 = water, 3 = brick, etc
			#blocklist.append(block(x*20, y*20)	
	#for block in blocklist:	Not sure about this, something about rendering.
		#block.render(window)
		
