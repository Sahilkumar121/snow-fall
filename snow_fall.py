import pygame
import random

pygame.init()

black_color = [0,0,0]
white_color = [225,225,225]

size = [800,600]
screen = pygame.display.set_mode(size)
moon_img = pygame.image.load("snow fall\\full-moon.png")
sky_img = pygame.image.load("snow fall\\cloud.png")

snowFall = []
for i in range(50):
  x = random.randrange(0,800)
  y = random.randrange(0,600)
  snowFall.append([x,y])

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(black_color)
  screen.blit(moon_img,(680,10))  

  for snow in range(len(snowFall)):
    pygame.draw.circle(screen,white_color,snowFall[snow],2)
    snowFall[snow][1] += 1
    
    if snowFall[snow][1] > 600:
      y = random.randrange(-50,-10)
      snowFall[snow][1] = y

      x = random.randrange(0,800)
      snowFall[snow][0] = x
      
    pygame.display.flip()
