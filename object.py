from random import randint
from math import sin, cos, pi
import pygame


def sign(n):
    return -1 if n < 0 else 1


# Elternklasse für Objekte
class Object:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 100,
        height: int = 100,
        color=(255, 255, 255),
        screen=pygame.display.get_surface(),
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        pass

    def update(self):
        self.move()
        self.draw()

    def collide(self, other=None):
        pass


class SlidingObject(Object):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 100,
        height: int = 100,
        color=(255, 255, 255),
        screen=pygame.display.get_surface(),
        speed: int = 1,
    ):
        super().__init__(x, y, width, height, color, screen)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speed *= -1

    def collide(self, other=None):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))


class GravityObject(Object):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 100,
        height: int = 100,
        color=(255, 255, 255),
        screen=pygame.display.get_surface(),
        speedx: int = 1,
        speedy: int = 1,
        acc: int = 1,
    ):
        super().__init__(x, y, width, height, color, screen)
        self.speedx = speedx
        self.speedy = speedy
        self.acc = acc
        self.width = width
        self.height = height

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.rect.x = self.screen.get_width() / 2 + sign(self.speedx) * (
                self.screen.get_width() / 2
            )
            if self.speedx >= 0:
                self.rect.x -= self.width
            self.speedx *= -1
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.rect.y = self.screen.get_height() / 2 + sign(self.speedy) * (
                self.screen.get_height() / 2
            )
            if self.speedy >= 0:
                self.rect.y -= self.height
            self.speedy *= -1
        self.speedy += self.acc

    def collide(self, other=None):
        self.speedy -= self.acc
        self.rect.x -= self.speedx
        if not self.rect.colliderect(other.rect):
            self.speedx *= -1
        else:
            self.rect.x += self.speedx
            self.rect.y -= self.speedy
            self.speedy *= -1
        self.speedy += self.acc


class ShrinkingObject(Object):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 100,
        height: int = 100,
        screen=pygame.display.get_surface(),
        speed: int = 3,
    ):
        super().__init__(x, y, width, height, screen=screen)
        self.speed = speed
        self.collide_check = False

    def move(self):
        if not self.collide_check:
            self.rect = pygame.Rect(
                self.rect.left - 1,
                self.rect.top - 1,
                self.rect.width + 2,
                self.rect.height + 2,
            )
        self.collide_check = False

        self.rect.x += self.speed
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speed *= -1

    def collide(self, other=None):
        self.collide_check = True
        self.rect = pygame.Rect(
            self.rect.left + 5,
            self.rect.top + 5,
            self.rect.width - 10,
            self.rect.height - 10,
        )


class Why(Object):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        radius: int = 5,
        size: int = 2,
        screen=pygame.display.get_surface(),
        speed: int = 3,
    ):
        super().__init__(x, y, screen=screen)
        self.center = (x, y)
        self.speed = speed
        self.radius = radius
        self.size = size
        self.collide_check = False
        self.deg = 0
        self.rect.width = 2 * size
        self.rect.height = 2 * size

    def draw(self):
        x = self.center[0] + sin(self.deg) * self.radius
        y = self.center[1] + cos(self.deg) * self.radius
        # pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        pygame.draw.circle(self.screen, self.color, (x, y), self.size)

    def move(self):
        self.deg += self.speed * pi / 180
        x = self.center[0] + sin(self.deg) * self.radius
        y = self.center[1] + cos(self.deg) * self.radius
        self.rect.x = x - self.size
        self.rect.y = y - self.size
