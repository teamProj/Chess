import pygame
from math import sqrt
from Troop import Front

pygame.init()
game = pygame.display.set_mode((677,725))
clock = pygame.time.Clock()
white = (250,250,250)
red = (255,0,0)
bg1 = (109,90,46)
yellow = (200,200,0)

valid_mouse = []
for x in range(65, 659, 66):
    for y in range(65, 725, 66):
        valid_mouse.append((x, y))

# Objects initialization
front1 = Front(game, yellow)

while True:
    eve = pygame.event.get()
    for event in eve:
        if event.type == pygame.QUIT:
            pygame.quit()

    game.fill(bg1)

    for row in range(65, 725, 66):
        pygame.draw.line(game, white, (65, row), (593, row), 2)
    for col in range(65, 659, 66):
        pygame.draw.line(game, white, (col, 65), (col, 329), 2)
        pygame.draw.line(game, white, (col, 395), (col, 659), 2)
        pygame.draw.line(game, white, (262, 65), (395, 197), 2)
        pygame.draw.line(game, white, (262, 526), (395, 658), 2)
        pygame.draw.line(game, white, (262, 197), (395, 65), 2)
        pygame.draw.line(game, white, (262, 658), (395, 526), 2)

    front1.display()

    m_x, m_y = pygame.mouse.get_pos()
    for check in valid_mouse:
        valid_dist = sqrt(((m_x-check[0])**2)+((m_y-check[1])**2))
        if valid_dist <= 32:
            pygame.draw.circle(game, (200,200,200), (check[0], check[1]), 20, 2)
            for event in eve:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    front1.x = check[0]
                    front1.y = check[1]


    pygame.display.flip()
    clock.tick(60)
