import pygame
import sys
import random

pygame.init()

Width, Hight = 800, 600


screen = pygame.display.set_mode((Width, Hight))
pygame.display.set_caption("Pong!")
clock = pygame.time.Clock()

#Padels
player = pygame.Rect(Width - 110, Hight/2 - 50, 10, 100)
player2 = pygame.Rect(110, Hight / 2- 50, 10, 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")

    pygame.draw.rect(screen, "white", player)
    pygame.draw.rect(screen, "white", player2)

    pygame.display.update()
    clock.tick(300)
#   P i n g - P o n g - G a m e  
 