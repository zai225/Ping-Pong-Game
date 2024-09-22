import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

Width, Hight = 800, 600
Font = pygame.font.SysFont("Arial", int(Width/20))

score = 0

screen = pygame.display.set_mode((Width, Hight))
pygame.display.set_caption("Pong!")
clock = pygame.time.Clock()

#sound effect
paddle_hit_sound = pygame.mixer.Sound("C:\\zaidd\\pong game\\ping-pong-paddle-sound.mp3")
score_sound = pygame.mixer.Sound("C:\\zaidd\\pong game\\score_sound_effect.mp3")

#Padels
player = pygame.Rect(Width - 110, Hight/2 - 50, 10, 100)
player2 = pygame.Rect(110, Hight / 2- 50, 10, 100)
player_score, player2_score = 0, 0


#Ball
ball = pygame.Rect(Width / 2 - 10, Hight / 2 - 20, 20, 20)
x_speed, y_speed = 3, 3

def display_score():
    pass

while True:
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= 5

    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < Hight:
            player.top += 5

    if keys_pressed[pygame.K_w]:
        if player2.top > 0:
            player2.top -= 5

    if keys_pressed[pygame.K_s]:
        if player2.top < Hight:
            player2.top += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()

    #ball movement and collision logic
    if ball.top <= 0 or ball.bottom >= Hight:  
        y_speed = -y_speed

    if ball.left <= 0:  
        player_score += 1
        ball.center = (Width / 2, Hight / 2)
        x_speed, y_speed = random.choice([3, -3]), random.choice([3, -3])

    if ball.right >= Width:  
        player2_score += 1
        ball.center = (Width / 2, Hight / 2)
        x_speed, y_speed = random.choice([3, -3]), random.choice([3, -3])
        pygame.mixer.Sound.play(score_sound)

    # Ball and paddle collision
    if player.colliderect(ball):  
        x_speed = -x_speed
        pygame.mixer.Sound.play(paddle_hit_sound)

    if player2.colliderect(ball):  
        x_speed = -x_speed
        pygame.mixer.Sound.play(paddle_hit_sound)
    
    #Update ball position
    ball.x += x_speed 
    ball.y += y_speed 

    #ScoreBoad
    player_score_text = Font.render(str(player_score), True, (190, 235, 229))
    player2_score_text = Font.render(str(player2_score), True, (190, 235, 229))
    
    screen.fill("black")

    pygame.draw.rect(screen, "white", player)
    pygame.draw.rect(screen, "white", player2)
    pygame.draw.circle(screen,"yellow",ball.center, 10)
    screen.blit(player_score_text, (Width / 2 + 50, 50))
    screen.blit(player2_score_text, (Width / 2 - 150, 50))

    pygame.display.update()
    clock.tick(60)













