#            TOP DOWN RACING GAME
#       ORIGINALLY CREATED IN MONOGAME
#                By Timothy J

import sys, pygame
from math import *
from player import Player


def render(screen, player):
    pygame.draw.rect(screen, (255, 255, 255), (0 + player.x, 0 + player.y, 50, 50))
    player.render(player.x, player.y, screen)


def update(player):
    player.update()


pygame.init()

backGroundColor = (0, 150, 120)
screen_width = 1280
screen_height = 720
screen_dim = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_dim)

FPS = 60
Clock = pygame.time.Clock()

# Set up Player
player = Player()

pygame.display.set_caption("Top Down Racing")
# icon = pygame.image.load('image.png')
# pygame.display.set_icon(icon)

# Game Loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.key_down(event.key)
        if event.type == pygame.KEYUP:
            player.key_up(event.key)

    # Update Game
    update(player)

    # Begin Rendering
    screen.fill(backGroundColor)
    render(screen, player)
    pygame.display.flip()
    Clock.tick(FPS)

pygame.quit()
