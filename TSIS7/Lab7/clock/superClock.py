import pygame as pg
import datetime, math
pg.init()

res = height, width = 1000, 1000
midle = height//2, width//2
screen = pg.display.set_mode(res)
radius = 400
putin = pg.image.load("putin.jpg")
pg.display.set_caption("ЛЮТЫЕ ЧАСЫ СКОРОХОДЫ БЕСПЛАТНО ИГРАТЬ ОНЛАЙН...")
pg.display.set_icon(putin)

clock = pg.time.Clock()

#pictures
sec = pg.image.load("rightLeg.png").convert_alpha()
minute = pg.image.load("leftLeg.png").convert_alpha()
rectsec = sec.get_rect()
rectmin = minute.get_rect()
rectmin.center = rectmin.center = midle


background = pg.image.load("backGround.jpg")


run = True
angle1 = 0
angle2 = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    #system time
    time = datetime.datetime.now()
    minuteTime = time.minute
    secondTime = time.second

    #minute
    angle1 = -minuteTime*6 #6 is degree
    leg1 = pg.transform.rotate(minute, angle1)
    rect1 = leg1.get_rect()
    rect1.center = rectmin.center

    #second
    angle2 = -secondTime*6 #6 is degree
    leg2 = pg.transform.rotate(sec, angle2)
    rect2 = leg2.get_rect()
    rect2.center = rectsec.center

    #output
    screen.blit(background, (0, 0))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)


    #screen.blit(background, (0, 0))
    #pg.draw.circle(screen, (0, 0, 0), (500, 500), 490, 5)
    pg.display.flip()
    clock.tick(60)
