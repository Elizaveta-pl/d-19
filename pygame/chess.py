import pygame

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

def board(num, size):
    new_color = (255, 255, 255)
    massiv0 = [0 if i % 2 == 0 else 1 for i in range(0, num)]
    massiv1 = [1 if i % 2 == 0 else 0 for i in range(0, num)]
    massiv = [massiv0 if i % 2 == 0 else massiv1 for i in range(0, num)]
    # new_image = Image.new('RGB', (num * size, num * size), new_color)
    # draw = ImageDraw.Draw(new_image)
    # for i in range(num):
    #     for j in range(num):
    #         if massiv[i][j] == 0:
    #             draw.rectangle((j * size, i * size, (j + 1) * size, (i + 1) * size), fill=(0, 0, 0))


pygame.init()
# w = int(input())
# n = int(input())
w=300
n = 60
h=600
size = w, w
if w / n % 2 == 0:
    # Surface black
    color_surface = pygame.Color(0, 0, 0)
    color = pygame.Color(255, 255, 255)
else:
    # Surface white
    color_surface = pygame.Color(255, 255, 255)
    color = pygame.Color(0, 0, 0)

# Устанавливаем размеры окна
screen = pygame.display.set_mode(size)
# Устанавливаем цвет окна
screen.fill(color_surface)
# screen.fill(pygame.Color('red'), (1, 1, 1, 1))

left, top, width, height = 10, 10, 50, 50
# pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 100), 0)
screen.fill(color, (left, top, width, height))

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()