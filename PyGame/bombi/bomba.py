import pygame
import random

class Bomb(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("bomb.png").convert_alpha()
        self.image_boom = pygame.image.load("boom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(430)
        self.rect.y = random.randrange(430)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.image_boom = pygame.transform.scale(self.image_boom, (70, 70))

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom

pygame.init()

FPS = 60
size = (500, 500)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
bomb = Bomb(all_sprites)
all_sprites.add(bomb)
all_sprites.draw(screen)
pygame.display.flip()

play = True


for _ in range(10):
    Bomb(all_sprites)
    all_sprites.add(bomb)
    all_sprites.draw(screen)
    pygame.display.flip()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            all_sprites.update(event)
            all_sprites.draw(screen)
            pygame.display.flip()

pygame.quit()