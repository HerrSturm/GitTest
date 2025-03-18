import pygame
import numpy as np
from random import randint

def sign(n):
    return -1 if n < 0 else 1

# Elternklasse für Objekte
class Object:
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100, color=(255, 255, 255),screen=pygame.display.get_surface(), mass: int = -1):

        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.screen = screen
        self.mass = mass
        self.speedx = 0
        self.speedy = 0
        self.acc = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        pass

    def update(self):
        self.draw()
        self.move()

    def static_collide(self, other):
        pass

    def dynamic_collide(self, other = None):
        pass

    def momentum_collide(self, other):
        pass

    def update_speed(self):
        pass


class SlidingObject(Object):
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100, color=(255, 255, 255),screen=pygame.display.get_surface(), speed: int = 1):
        super().__init__(x, y, width, height, color, screen)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speed *= -1

    def dynamic_collide(self, other = None):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

class GravityObject(Object):
    def __init__(self, x: int=0, y: int=0, width: int=100, height:int=100, color=(255, 255, 255),screen=pygame.display.get_surface(), speedx: int = 1, speedy: int = 1, acc: int = 1, mass: int = 1):
        super().__init__(x, y, width, height, color, screen)
        self.speedx = speedx
        self.speedy = speedy
        self.acc = acc
        self.width = width
        self.height = height
        self.mass = mass

    def move(self):
        self.speedy += self.acc
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.rect.x = self.screen.get_width()/2 + sign(self.speedx)*(self.screen.get_width()/2)
            if self.speedx >= 0:
                self.rect.x -= self.width
            self.speedx *= -1
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.rect.y = self.screen.get_height()/2 + sign(self.speedy)*(self.screen.get_height()/2)
            if self.speedy >= 0:
                self.rect.y -= self.height
            self.speedy *= -1
    
    def static_collide(self, other):

        #print(" ")
        if self.rect.x < other.rect.x:
            a = self
            b = other
        else:
            a = other
            b = self
        
        diffx = a.rect.right - b.rect.left
        
        if self.rect.y < other.rect.y:
            c = self
            d = other
        else:
            c = other
            d = self
        
        diffy = c.rect.bottom - d.rect.top

        speeddiffx = a.speedx - b.speedx
        speeddiffy = c.speedy - d.speedy

        if speeddiffx > speeddiffy:
            if a == self:
                a.rect.x -= diffx
                a.speedx = -1*abs(a.speedx)
                #print("x")
            else:
                b.rect.x += diffx
                b.speedx = abs(b.speedx)
                #print("x")

        else:
            if c == self:
                c.rect.y -= diffy
                c.speedy = -1*abs(c.speedy)
                #print("y")
            else:
                d.rect.y += diffy
                d.speedy = abs(d.speedy)
                #print("y")

    def dynamic_collide(self, other = None):
        if other.mass < 0:
            self.static_collide(other)
            return

        print(" ")
        if self.rect.x < other.rect.x:
            a = self
            b = other
        else:
            a = other
            b = self
        
        diffx = a.rect.right - b.rect.left
        
        if self.rect.y < other.rect.y:
            c = self
            d = other
        else:
            c = other
            d = self
        
        diffy = c.rect.bottom - d.rect.top

        speeddiffx = a.speedx - b.speedx
        speeddiffy = c.speedy - d.speedy

        if speeddiffx > speeddiffy:
            a.rect.x -= diffx/2
            a.rect.y -= (a.speedx/(diffx/2))*a.speedy
            b.rect.x += diffx/2
            b.rect.y += (b.speedx/(diffx/2))*b.speedy
            a.speedx = -1*abs(a.speedx)
            b.speedx = abs(b.speedx)
            print("x")
        else:
            print(diffy)
            c.rect.y -= diffy/2
            c.rect.x -= (c.speedy/(diffy/2))*c.speedx
            d.rect.y += diffy/2
            d.rect.x += (d.speedy/(diffy/2))*d.speedx
            c.speedy = -1*abs(c.speedy)
            d.speedy = abs(d.speedy)
            print("y")


    def momentum_collide(self, other):
        if self.mass < 0 or other.mass < 0:
            self.static_collide(other)
        else:
            #print(" ")
            if self.rect.x < other.rect.x:
                a = self
                b = other
            else:
                a = other
                b = self
            
            diffx = a.rect.right - b.rect.left
            
            if self.rect.y < other.rect.y:
                c = self
                d = other
            else:
                c = other
                d = self
            
            diffy = c.rect.bottom - d.rect.top

            speeddiffx = a.speedx - b.speedx
            speeddiffy = c.speedy - d.speedy

            if speeddiffx > speeddiffy:
                a.rect.x -= diffx/2
                b.rect.x += diffx/2
                a.speedx = ((a.mass-b.mass)*a.speedx + 2*b.mass*b.speedx)/(a.mass+b.mass)
                b.speedx = ((b.mass-a.mass)*b.speedx + 2*a.mass*a.speedx)/(b.mass+a.mass)
                #print("x")
            else:
                c.rect.y -= diffy/2
                d.rect.y += diffy/2
                c.speedy = ((a.mass-b.mass)*a.speedy + 2*b.mass*b.speedy)/(a.mass+b.mass)
                d.speedy = ((b.mass-a.mass)*b.speedy + 2*a.mass*a.speedy)/(b.mass+a.mass)
                #print("y")


