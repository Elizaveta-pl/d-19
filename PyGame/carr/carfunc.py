import pygame

class Car(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('car2.png').convert_alpha()
        self.car_surf = self.image
        self.car_rect = self.image.get_rect(center=(75, 47))
        sc.blit(self.image, self.car_rect)

    def update(self,):

        if self.car_rect.x != 550:
            print(self.car_rect)
            self.car_rect.x += 50
        else:
            self.car_surf = pygame.transform.flip(self.image, True, False)

pygame.init()

FPS = 60
screen = (600, 95)

sc = pygame.display.set_mode(screen)
sc.fill((255,255,255))
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
car = Car(all_sprites)
all_sprites.add(car)
#all_sprites.draw(sc)
pygame.display.flip()

play = True

while play:
    clock.tick(1)
    sc.fill((255,255,255))
    all_sprites.update()
    #all_sprites.add(car)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    sc.fill((255,255,255))
    #sc.blit(car_surf, car_rect)
    pygame.display.update()

    pygame.time.Clock().tick(FPS)