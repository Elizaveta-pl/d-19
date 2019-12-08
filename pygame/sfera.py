import pygame


def draw(n):
    screen.fill((0, 0, 0))
    Rect = 0, 0, 300, 300
    g = 0
    s = 2 * n
    for i in range(1, 1 + n):
        pygame.draw.ellipse(screen, (255, 255, 255), Rect, 1)
        Rect = 300/(n*i), 0, 300 - (300 / n * i), 300
        g += 2 * n
        s += 2 * n


pygame.init()
n = int(input())
size = 300, 300
screen = pygame.display.set_mode(size)
draw(n)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()