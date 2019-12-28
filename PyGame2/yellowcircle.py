import pygame

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

def draw(x_pos, clock):
    yellow = (0, 255, 0)

    f = 0
    fps = 20
    v = 200
    for i in range(20):
        pygame.draw.circle(screen, yellow, x_pos, f)
        f += v * clock.tick(fps) / 1000

        pygame.display.flip()

pygame.init()
size = 600, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 225))
clock = pygame.time.Clock()
pygame.display.flip()
running = True

while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    screen.fill((0, 0, 225))
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            draw(event.pos, clock)

pygame.quit()