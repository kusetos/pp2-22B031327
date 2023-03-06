import time
import pygame as pg
pg.init()

despacitoPath = "/Users/kuset/Documents/Codes/python/pp2-22B031327/TSIS7/Lab7/mp3/Despacito.mp3"
mozzartPath = "/Users/kuset/Documents/Codes/python/pp2-22B031327/TSIS7/Lab7/mp3/DrillRemix.mp3"
boomPath = "/Users/kuset/Documents/Codes/python/pp2-22B031327/TSIS7/Lab7/mp3/3NBSQ2N-explosions.mp3"
sc = pg.display.set_mode((480, 360))
pg.display.set_caption("ЭМ ПЕ ТРИ ПЛЕЙЕР")
clock = pg.time.Clock()
# mozzart = pg.mixer.music.load(mozzartPath)
# boom = pg.mixer.music.load(boomPath)
despacito = pg.mixer.music.load(despacitoPath)
musicList = [despacitoPath, mozzartPath, boomPath]
pg.mixer.music.play(-1)
monkey = pg.image.load("/Users/kuset/Documents/Codes/python/pp2-22B031327/TSIS7/Lab7/mp3/monkey.jpeg")

sc.blit(monkey, (0, 0))
flPlay = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)

