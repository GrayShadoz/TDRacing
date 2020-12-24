#            TOP DOWN RACING GAME
#       ORIGINALLY CREATED IN MONOGAME
#                By Timothy J

import sys, pygame
# From player.py import Player Class
from player import Player

# Render Function
def render(cam_x, cam_y, screen, player):
    pygame.draw.rect(screen, (255, 255, 255), (0 + cam_x, 0 + cam_y, 50, 50))
    # screen.blit(car, rect)
    player.render(cam_x, cam_y, screen)


def update(player):
    player.update()

# Initialize pygame
pygame.init()

# Variables
backGroundColor = (0, 150, 120)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen_dim = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Create the screen object
screen = pygame.display.set_mode(screen_dim)

FPS = 60
fpsClock = pygame.time.Clock()

# Set up Player
player = Player(50, 50)
# Set Up Camera
cam_x = 250
cam_y = 250

# Main Loop - Run until the user asks to quit
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

    # Tween Camera
    cam_x += (((SCREEN_WIDTH / 2) - player.x) - cam_x) * 0.01
    cam_y += (((SCREEN_HEIGHT / 2) - player.y) - cam_y) * 0.01

    # Begin Rendering
    screen.fill(backGroundColor)
    render(cam_x, cam_y, screen, player)

    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()
