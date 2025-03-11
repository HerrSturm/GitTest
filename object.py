import pygame
from random import randint

# Elternklasse für Objekte
class Object:
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100, color=(255, 255, 255),screen=pygame.display.get_surface()):

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

    def collide(self, other = None):
        pass


class SlidingObject(Object):
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100, color=(255, 255, 255),screen=pygame.display.get_surface(), speed: int = 1):
        super().__init__(x, y, width, height, color, screen)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speed *= -1

    def collide(self, other = None):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))


class ShrinkingObject(Object):
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100,screen=pygame.display.get_surface(), speed: int = 3):
        super().__init__(x, y, width, height, screen=screen)
        self.speed = speed
        self.collide_check = False

    def move(self):
        if not self.collide_check:
            self.rect = pygame.Rect(self.rect.left - 1, self.rect.top - 1, self.rect.width + 2, self.rect.height + 2)
        self.collide_check = False
        
        self.rect.x += self.speed
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speed *= -1

    def collide(self, other = None):
        self.collide_check = True
        self.rect = pygame.Rect(self.rect.left + 5, self.rect.top + 5, self.rect.width - 10, self.rect.height - 10)


class UpsidedownGravity(Object):
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100, color=(0, 0, 255),screen=pygame.display.get_surface(), speedx: float = 1,speedy: float = 1, acceleration: float = 0.02):
        super().__init__(x, y, width, height, color, screen)
        self.speedx = speedx
        self.speedy = speedy
        self.acceleration = acceleration
        
    def update(self):
        super().update()
        self.gravity()

    def gravity(self):
        self.speedy += self.acceleration

class GravityObject(Object):
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100, color=(255, 255, 255),screen=pygame.display.get_surface(), speedx: int = 1, speedy: int = 1):
        super().__init__(x, y, width, height, color, screen)
        self.speedx = speedx
        self.speedy = speedy
        self.acc = 2


    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx *= -1
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.speedy *= -1

        self.speedy += self.acc





