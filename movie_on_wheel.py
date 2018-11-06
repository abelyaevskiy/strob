import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.display.flip()

    # pygame.time.delay(1000)
    # pygame.draw.line(screen, WHITE, [0, 0], [100, 100], 5)
    # pygame.display.flip()

    clock.tick(60)

pygame.quit()
