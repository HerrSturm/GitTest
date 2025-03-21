import pygame
import sys
from object import Object, SlidingObject, GravityObject, ShrinkingObject, Why


def render_text(text, color, coords, window):
    font = pygame.font.SysFont("Consolas", 30)
    text = font.render(text, 1, pygame.Color(color))
    window.blit(text, coords)


def main():
    pygame.init()

    # Fenster-Einstellungen
    WIDTH, HEIGHT = 1200, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Test")

    # Objekte erstellen und in Liste speichern
    gameObjects = []
    gameObjects.append(Object(100, 100, 100, 100, (255, 0, 0), screen))
    # gameObjects.append(SlidingObject(100, 200, 100, 100, (0, 255, 0), screen, 2))
    # gameObjects.append(SlidingObject(600, 200, 100, 100, (0, 255, 0), screen, -2))
    gameObjects.append(GravityObject(600, 200, 100, 100, (0, 255, 0), screen, 10, 0, 1))
    # gameObjects.append(ShrinkingObject(800, 280, 100, 100, screen, -1))
    gameObjects.append(Why(WIDTH / 2, HEIGHT / 2, 100, 30, screen, 10))

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

        render_text(
            "FPS: " + str(round(clock.get_fps(), 2)), (255, 255, 255), (0, 0), screen
        )

        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
