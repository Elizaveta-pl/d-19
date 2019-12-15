import pygame

pygame.init()

FPS = 60
size = (300, 300)

screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

hero_main = pygame.image.load('C:/Users/users/PycharmProjects/d-19/pygame/data/'
                              'creature.png').convert().convert_alpha()
hero_rect = hero_main.get_rect(center=(35, 48))
pygame.display.flip()

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        hero_rect.x += 10

    if keys[pygame.K_LEFT]:
        hero_rect.x -= 10

    if keys[pygame.K_UP]:
        hero_rect.y -= 10

    if keys[pygame.K_DOWN]:
        hero_rect.y += 10

    screen.fill((255, 255, 255))
    screen.blit(hero_main, hero_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)