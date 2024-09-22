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

#Ball
ball = pygame.Rect(Width / 2 - 10, Hight / 2 - 20, 20, 20)
x_speed, y_speed = 1,1


while True:
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= 2

    if keys_pressed[pygame.K_DOWN]:
        if player.top < Hight:
            player.top += 2

    if keys_pressed[pygame.K_w]:
        if player2.top > 0:
            player2.top -= 2

    if keys_pressed[pygame.K_s]:
        if player2.top < Hight:
            player2.top += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.x += x_speed * 2
    ball.y += y_speed * 2

    screen.fill("black")

    pygame.draw.rect(screen, "white", player)
    pygame.draw.rect(screen, "white", player2)
    pygame.draw.circle(screen,"yellow",ball.center, 10)

    pygame.display.update()
    clock.tick(300)










