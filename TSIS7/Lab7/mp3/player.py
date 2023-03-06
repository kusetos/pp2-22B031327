import time

import pygame as pg
pg.init()


sc = pg.display.set_mode((900, 500))
pg.display.set_caption("ЭМ ПЕ ТРИ ПЛЕЙЕР")
clock = pg.time.Clock()
pg.mixer.music.load("despacito.mp3")
pg.mixer.music.play(-1)
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    #pg.display.update()
    clock.tick(60)

