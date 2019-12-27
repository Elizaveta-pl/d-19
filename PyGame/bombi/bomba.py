import pygame
import random

class Bomb(pygame.sprite.Sprite):

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        print(group)
        self.image = pygame.image.load("bomb.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))

        self.image_boom = pygame.image.load("boom.png")
        self.image_boom = pygame.transform.scale(self.image_boom, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(430)
        self.rect.y = random.randrange(430)


    def update(self, *args):
        # print(args[0])
        # self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            print(f'image = {self.image} image_boom = {self.image_boom}')
            self.image = ''
            self.image = self.image_boom
            print(f'image = {self.image} image_boom = {self.image_boom}')
            print(bomb.groups())


pygame.init()

FPS = 60
size = (500, 500)
clock = pygame.time.Clock()

score = 0

screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
bomb = Bomb(all_sprites)

# all_sprites.add(bomb)
# all_sprites.draw(screen)
# pygame.display.flip()

play = True


for _ in range(2):
    Bomb(all_sprites)
    all_sprites.draw(screen)
    all_sprites.add(bomb)
    pygame.display.flip()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # screen.fill((255, 255, 255))
            all_sprites.update(event)
            all_sprites.draw(screen)
            # all_sprites.add(bomb)


            # screen.blit((255, 255, 255), (100, 100))

            # pygame.display.flip()
            pygame.display.update()
            clock.tick(6)

    #screen.fill((255, 255, 255))
#all_sprites.draw(screen)
pygame.quit()