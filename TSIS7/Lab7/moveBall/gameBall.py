import pygame as pg
pg.init()
sc = pg.display.set_mode((700, 700))
sideRes = 700
R = 25
pg.display.set_caption("SUPER COOL GAME FOR FREE...")

x = 350
y = 350
ball = pg.draw.circle(sc, (250, 10, 10), (x, y), 25, 3)

clock = pg.time.Clock()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                if x >= sideRes - R:
                    x = x
                else:
                    x += 20
            elif event.key == pg.K_LEFT:
                if x <= R:
                    x = x
                else:
                    x -= 20
            elif event.key == pg.K_UP:
                if y <= R:
                    y = y
                else:
                    y -= 20 
            elif event.key == pg.K_DOWN:
                if y >= sideRes - R:
                    y = y
                else:
                    y += 20
    sc.fill((0, 0, 0))
    pg.draw.circle(sc, (250, 10, 10), (x, y), 25)
    clock.tick(60)
    pg.display.flip()