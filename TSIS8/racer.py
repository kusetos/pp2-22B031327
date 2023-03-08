import pygame as pg
import random, time, sys
from pygame.locals import *

pg.init()

font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

sc = pg.display.set_mode((1000, 1000))
W, H = 1000, 1000
pg.display.set_caption("КРУТЫЕ ГОНКИ ИГРАТЬ ВМЕСТЕ 2 ИГРОКА")
clock = pg.time.Clock()

bgRoad = pg.image.load("bgRoad.png")
#sharkIm = pg.image.load("shark.png")
#rocketIm = pg.image.load("rocket.png")
sharkWidth = 240
sharkHeight = 360
speed = 20
game_over = font.render("Game Over", True, (0, 0, 0))
score = 1


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)
    def move(self):
        global score
        self.rect.move_ip(0, 5)
        if self.rect.top > 1000:
            score += 1.2
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 0)
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Shark(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("shark.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 700)

    def move(self):
        pressed_keys = pg.key.get_pressed()
        # if pressed_keys[pg.K_UP]:
        #     self.rect.y -= 15
        # if pressed_keys[pg.K_DOWN]:
        #     self.rect += 15
        if self.rect.left > 0:
            if pressed_keys[pg.K_LEFT]:
                self.rect.move_ip(-15, 0)
        if self.rect.right < 1000:
            if pressed_keys[pg.K_RIGHT]:
                self.rect.move_ip(15, 0)

rocket = Enemy()
shark = Shark()


rockets = pg.sprite.Group()
rockets.add(rocket)
all_sprites = pg.sprite.Group()
all_sprites.add(rocket)
all_sprites.add(shark)

speed_incr = pg.USEREVENT + 1
pg.time.set_timer(speed_incr, 1000)

run = True
while True:
    for event in pg.event.get():
        if event.type == speed_incr:
            speed += 0.5
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    sc.blit(bgRoad, (0, 0))
    scores = font_small.render(str(score), True, (0, 0, 0))
    sc.blit(scores, (20, 20))

    for entity in all_sprites:
        sc.blit(entity.image, entity.rect)
        entity.move()

    if pg.sprite.spritecollideany(shark, rockets):
        pg.mixer.Sound('whopee.mp3').play()
        time.sleep(0.5)

        sc.fill((129, 1, 1))
        sc.blit(pg.image.load("face.jpg"), (00, 0))

        pg.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pg.quit()
        sys.exit()


    pg.display.update()
    clock.tick(60)