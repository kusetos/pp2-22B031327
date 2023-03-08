import pygame as pg
pg.init()

sc = pg.display.set_mode((1000, 1000))
pg.display.set_caption("КРУТЫЕ ГОНКИ ИГРАТЬ ВМЕСТЕ 2 ИГРОКА")
clock = pg.time.Clock()

bgRoad = pg.image.load("bgRoad.png")
sharkIm = pg.image.load("shark.png").convert_alpha
sharkWidth = 160
sharkHeight = 240

def draw_obj(shark):
    sc.blit(bgRoad, (0, 0))
    sc.blit(sharkIm, (shark.x, shark.y))
    pg.display.update()

run = True
shark = pg.Rect(400, 600, sharkWidth, sharkHeight)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    draw_obj(shark)
    clock.tick(60)
    pg.display.flip()