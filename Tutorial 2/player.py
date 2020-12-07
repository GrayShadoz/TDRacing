import sys, pygame
from math import *

class Player:
    def __init__(self):
        self.direction = None
        self.x = 50
        self.y = 50

        self.velocity = 0  # Current velocity in pixels per second
        self.acceleration = 1  # Pixels per second (Also friction)
        self.topSpeed = 30  # Max speed in pixels per second
        self.rotation = 0  # In degrees
        self.turnRate = 5  # In degrees per second

        self.car = pygame.image.load("res/Car_Left.png").convert_alpha()
        self.rect = self.car.get_rect()
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        if self.up:
            self.y -= 1
        if self.down:
            self.y += 1

        self.rect.x = self.x
        self.rect.y = self.y

    def render(self, x, y, screen):
        screen.blit(self.car, self.rect)

    def key_down(self, key):
        if key == pygame.K_w:
            self.up = True
        if key == pygame.K_s:
            self.down = True
        if key == pygame.K_a:
            self.left = True
        if key == pygame.K_d:
            self.right = True

    def key_up(self, key):
        if key == pygame.K_w:
            self.up = False
        if key == pygame.K_s:
            self.down = False
        if key == pygame.K_a:
            self.left = False
        if key == pygame.K_d:
            self.right = False

