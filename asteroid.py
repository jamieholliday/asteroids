import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += pygame.Vector2(0, 1) + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(new_angle)
            vec2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius).velocity = vec1 * 1.2
            Asteroid(self.position.x, self.position.y, new_radius).velocity = vec2 * 1.2
