import pygame as pg
import random, time, sys
from pygame.locals import *

pg.init()

font = pg.font.SysFont("Areal", 60)
font_small = pg.font.SysFont("Verdana", True, 20)


sc = pg.display.set_mode((1000, 1000))
W, H = 1000, 1000
pg.display.set_caption("КРУТЫЕ ГОНКИ ИГРАТЬ ВМЕСТЕ 2 ИГРОКА")
clock = pg.time.Clock()

bgRoad = pg.image.load("bgRoad.png")
#sharkIm = pg.image.load("shark.png")
#rocketIm = pg.image.load("rocket.png")
bombIm = pg.image.load("bomb.png")


speed = 5
game_over = font.render("Game Over", True, (0, 0, 0))
score = 100
money = 0
index = 0
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.speed = 7
    def move(self):
        global money
        self.rect.move_ip(0, 3)
        if self.rect.top > 1000:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 200)
    def draw(self):
        sc.blit(self.image, self.rect)
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("bomb.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)
    def move(self):
        global score
        global index
        self.rect.move_ip(0, speed)
        if self.rect.top > 1000:
            index += 1
            score += 100 * index*0.1
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 200)
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
        if self.rect.top > 5:
            if pressed_keys[pg.K_UP]:
                self.rect.move_ip(0, -15)
        if self.rect.bottom < 1000:
            if pressed_keys[pg.K_DOWN]:
                self.rect.move_ip(0, 15)
        if self.rect.left > 0:
            if pressed_keys[pg.K_LEFT]:
                self.rect.move_ip(-15, 0)
        if self.rect.right < 1000:
            if pressed_keys[pg.K_RIGHT]:
                self.rect.move_ip(15, 0)

rocket = Enemy()
shark = Shark()
coin = Coin()


coins = pg.sprite.Group()
coins.add(coin)
rockets = pg.sprite.Group()
rockets.add(rocket)
group = pg.sprite.Group()
group.add(rocket, shark, coin)

speed_incr = pg.USEREVENT + 1
pg.time.set_timer(speed_incr, 2000)


run = True
while True:
    for event in pg.event.get():
        if event.type == speed_incr:
            speed *= 1.01
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    sc.blit(bgRoad, (0, 0))
    scores = font.render(str(int(score)), True, (0, 0, 0))
    sc.blit(scores, (20, 20))
    monCount = font.render(str(money), True, (255, 200, 50))

    sc.blit(monCount, (800, 10))

    for entity in group:
        sc.blit(entity.image, entity.rect)
        entity.move()

    if pg.sprite.spritecollideany(shark, coins):
        money += 1
        coin.rect.top = 1000



    for rocket in rockets:
        if shark.rect.collidepoint(rocket.rect.center):
            pg.mixer.Sound('whopee.mp3').play()
            time.sleep(0.5)

            sc.fill((9, 1, 1))
            sc.blit(pg.image.load("superScary.jpg"), (00, 0))

            pg.display.update()
            for entity in group:
                entity.kill()
            time.sleep(3)
            pg.quit()
            sys.exit()

    pg.display.update()
    clock.tick(60)