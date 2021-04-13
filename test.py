import pygame
import random


WIDTH = 1000
HEIGHT = 1000
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
player = pygame.image.load("/home/sevashasla/coding/python/projects/TowerDefence/Assets/ChadUnit.png")
# player = pygame.image.load("/home/sevashasla/coding/python/projects/TowerDefence/test.png")
player.set_colorkey((255,0,255))

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    screen.blit(player, (0, 0))
    pygame.display.flip()
pygame.quit()
