import pygame

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

def draw(x_pos, clock):
    yellow = (255, 255, 0)
    screen.fill((0, 0, 225))
    pygame.display.flip()

    f = 0
    fps = 20
    v = 100
    for i in range(60):
        mouse = 0
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = 1
                draw(event.pos, clock)
        if mouse == 0:
            pygame.draw.circle(screen, yellow, x_pos, f)
            f += int(v * clock.tick(fps) / 1000)
            pygame.display.flip()
        else:
            break



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