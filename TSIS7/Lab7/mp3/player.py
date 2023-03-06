import time
import pygame as pg
pg.init()

despacito = "/Users/kuset/Documents/Codes/python/pp2-22B031327/TSIS7/Lab7/mp3/Despacito.mp3"
mozzart = "/Users/kuset/Documents/Codes/python/pp2-22B031327/TSIS7/Lab7/mp3/DrillRemix.mp3"
boom = "/Users/kuset/Documents/Codes/python/pp2-22B031327/TSIS7/Lab7/mp3/3NBSQ2N-explosions.mp3"
sc = pg.display.set_mode((900, 500))
pg.display.set_caption("ЭМ ПЕ ТРИ ПЛЕЙЕР")
clock = pg.time.Clock()
#pg.mixer.music.load(mozzart)
pg.mixer.music.load(despacito)
pg.mixer.music.play(-1)
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    pg.display.flip()
    clock.tick(60)

