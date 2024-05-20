import pygame as pg
import random

class Raindrop:
	def __init__(self, x, y, color, thickness):
		self.x = x
		self.y = y
		self.color = color
		self.thickness = thickness 
		return

	def update(self):
		if self.y > SCREEN_HEIGHT:
			self.x = random.randrange(0, SCREEN_WIDTH) 
			self.y = -30

		self.y += SPEED*self.thickness
		return

	def draw(self):
		pg.draw.rect(display, self.color, (self.x, self.y, int(self.thickness), self.thickness*5))	
		return

def main():
	raindrops = []
	for i in range(N):
		x = random.randrange(0, SCREEN_WIDTH)
		y = random.randrange(0, SCREEN_HEIGHT)
		color = random.choice(COLORS)
		thickess = random.uniform(0, 1)*5

		raindrops.append(Raindrop(x, y, color,thickess))

	while True:
		clock.tick(FPS)

		for event in pg.event.get():
			if event.type==pg.QUIT:
				pg.quit()
				sys.exit()
				break

		display.fill((0,0,0))
		for raindrop in raindrops:
			raindrop.update()
			raindrop.draw()

		pg.display.flip()	

	return

if __name__=="__main__":
	N = 500
	FPS = 60
	SPEED = 3
	SCREEN_WIDTH = 1920
	SCREEN_HEIGHT = 1080
	COLORS = [
		(100, 100, 100), 
		(255, 0, 0), 
		(0, 255, 0), 
		(0, 0, 255), 
		(255, 255, 0), 
		(255, 0, 255), 
		(0, 255, 255), 
		(255, 255, 255)
	]

	pg.init()

	display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pg.time.Clock()

	main()