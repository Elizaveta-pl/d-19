import pygame


def draw(n):
    screen.fill((0, 0, 0))
    for i in range(0, n):
        x = 150 / n * i
        d = (150 - x) * 2
        Rect = x, 0, d, 300
        Lect = 0, x, 300, d
        pygame.draw.ellipse(screen, (255, 255, 255), Rect, 1)
        pygame.draw.ellipse(screen, (255, 255, 255), Lect, 1)


pygame.init()
n = int(input())
size = 300, 300
screen = pygame.display.set_mode(size)
draw(n)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
