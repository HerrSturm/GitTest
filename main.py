import pygame
import sys
from object import Object, SlidingObject, UpsidedownGravity


def main():
    pygame.init()
    
    # Fenster-Einstellungen
    WIDTH, HEIGHT = 1200, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Test")

    # Objekte erstellen und in Liste speichern
    gameObjects = []
    gameObjects.append(Object(100, 100, 100, 100, (255, 0, 0), screen))
    gameObjects.append(SlidingObject(100, 200, 100, 100, (0, 255, 0), screen, 2))
    gameObjects.append(SlidingObject(700, 200, 100, 100, (0, 255, 0), screen, -2))
    gameObjects.append(UpsidedownGravity(200, 300, 100, 100, (0, 255, 0), screen, 5, -5, -0.25))
    gameObjects.append(UpsidedownGravity(400, 400, 100, 100, (0, 255, 0), screen, 2, 2, -1))
    gameObjects.append(UpsidedownGravity(500, 200, 100, 100, (0, 255, 0), screen, -6, -7, -1))
    gameObjects.append(UpsidedownGravity(300, 100, 100, 100, (0, 255, 0), screen, -2, -5, -0.5))
    


    clock = pygame.time.Clock()
    # Hauptschleife
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Hintergrund färben
        screen.fill((0, 0, 0))  # Schwarz
        
        # Objekte updaten (bewegen, zeichnen, etc.)
        for obj in gameObjects:
            obj.update()

        # Kollisionen prüfen und collisions-Methoden aufrufen
        for obj in gameObjects:
            for other in gameObjects:
                if obj != other and obj.rect.colliderect(other.rect):
                    obj.collide(other)
        


        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
