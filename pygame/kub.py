import pygame

# Определяем несколько цветов, которые мы будем
# использовать (RGB)
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

pygame.init()
# w = int(input())
# n = int(input())
w = 300
n = 60
h = 300
W = 100
Hue = 0

# Устанавливаем размер
size = w, h

# Задаем  цвет окна
color_surface = pygame.Color('black')
# Задаем  цвет фигур
color = pygame.Color('orange')

hsv = color.hsva
print(hsv)
# увеличиваем параметр Value, который влияет на яркость
color.hsva = (Hue, hsv[1], hsv[2] - 30, hsv[3])

# Устанавливаем размеры окна
screen = pygame.display.set_mode(size)
# Устанавливаем цвет окна
screen.fill(color_surface)

for i in range(h // n):
    for j in range(w // n):
        pos1 = (n / 2 , n / 2 - n / 2 + n * i)
        pos2 = (pos1[0] - n / 2, pos1[1] + n / 2)
        pos3 = (pos1[0], pos1[1] + n)
        pos4 = (pos2[0] + n, pos2[1])
        # Точки для отрисовки ромба
        points = [pos1, pos2, pos3, pos4]
        # Рисуем первый ромб в строке
        pygame.draw.polygon(screen, color, points)
        # Рисуем последующие ромбы
        secondPoints = [(p[0] + n * j, p[1]) for p in points]
        pygame.draw.polygon(screen, color, secondPoints)

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
