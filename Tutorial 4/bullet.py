import sys, pygame
from math import *


class Bullet:
    def __init__(self, angle, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.angle = angle

    # Update Method
    def update(self):
        self.x += cos(self.angle) * self.speed
        self.y += sin(self.angle) * self.speed

    # Render
    def render(self, cam_x, cam_y, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x + cam_x, self.y + cam_y, 10, 10))