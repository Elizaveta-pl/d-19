import pygame


def draw():
    # pygame.draw.rect(screen, color_surface, (0, 0, 200, 200))
    font = pygame.font.Font(None, 100)
    text = font.render(str(s), 1, (100, 255, 100))
    # Выравниваем по центру
    place = text.get_rect(center=(100, 100))
    # Отрисовываем текст
    screen.blit(text, place)
    pygame.display.flip()


pygame.init()
size = 200, 200
s = 0

# Задаем  цвет окна
color_surface = pygame.Color('black')
# Устанавливаем размеры окна
screen = pygame.display.set_mode(size)

# Устанавливаем цвет окна
screen.fill(color_surface)

# Задаем  цвет фигур
color = pygame.Color('red')

# draw()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEOEXPOSE:
            s += 1
            draw()
pygame.display.flip()
pygame.quit()
