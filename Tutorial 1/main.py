#            TOP DOWN RACING GAME
#       ORIGINALLY CREATED IN MONOGAME
#                By Timothy J

import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Top Down Racing")
# icon = pygame.image.load('image.png')
# pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 150, 205))
    pygame.display.update()
