import pygame as pg
import random
import math
pg.init()
sc = pg.display.set_mode((1600, 900))
pg.display.set_caption("РИСОВАЛКА ОФЛАЙН ИГРА ТВОРЧЕСТВО")
clock = pg.time.Clock()


niceFont = pg.font.Font("tupo-vyaz_regular.ttf", 40)
#blueBind = niceFont.render("press B for blue colour", True, (200, 200, 200))
blue = (0, 0, 100)
red = (100, 0, 0)
black = (20, 20, 20)
pink = (200, 0, 200)

redRect = pg.Rect(0, 0, 50, 50)
blueRect = pg.Rect(50, 0, 50, 50)
blackRect = pg.Rect(150, 0, 50, 50)
pinkRect = pg.Rect(100, 0, 50, 50)

squareR = pg.Rect(0, 50, 50, 50)
circleR = pg.Rect(0, 100, 50, 50)
sqrIcon = pg.draw.rect(sc, (220, 222, 222), (5, 55, 40, 40), 2)
circleIcon = pg.draw.circle(sc, (200, 200, 200), (25, 125), 20, 2)
triangleIcon = pg.draw.polygon(sc, (200, 200, 200), [[10, 160], [40, 190], [10, 190]], 2)

moi_grib = pg.image.load("moi_grib.png")
chad_stand = pg.image.load("chad_stand.png")
chad_face = pg.image.load("gigachad.jpg")
chad_face = pg.transform.scale(chad_face, (200, 220))
ronaldo = pg.image.load("ronaldo_5.jpg")
ronaldo = pg.transform.scale(ronaldo, (200, 120))
uldan = pg.image.load("Uldana_face.png").convert_alpha()
random_icon = pg.image.load("random_ic.png")
random_icon = pg.image.load("random_ic.png")
random_icon = pg.transform.scale(random_icon, (100, 100))
randRect = random_icon.get_rect()

posXA, posYA = 0, 0
posXB, posYB = 0, 0
posXC, posYC = 0, 0
posX1, posY1 = 0, 0
posX2, posY2 = 0, 0
posX3, posY3 = 0, 0
images = [ronaldo, uldan, chad_face, chad_stand, moi_grib]
rects = [[red, redRect], [blue, blueRect], [black, blackRect], [pink, pinkRect]]
shapes = [sqrIcon, circleIcon, triangleIcon]
        #self.colour = colour
colour = (100, 120, 140)
def colour_pick():
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    global colour
    if clik[0]:
        if posX < 50 and posY < 50:
            colour = red
        elif posX < 100 and posX > 50 and posY < 50:
            colour = blue
        elif posX < 150 and posX > 100 and posY < 50:
            colour = pink
        elif posX < 200 and posX > 150 and posY < 50:
            colour = (0, 0, 0)


def shape_pick():
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    global flag
    if clik[0]:
        if posX < 50 and posY > 50 and posY < 100:
            flag = 2
        elif posX < 50 and posY > 100 and posY < 160:
            flag = 3
        elif posX < 50 and posY > 150 and posY < 200:
            flag = 4
def draw():

    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    if clik[0]:
         pg.draw.circle(sc, colour, (posX, posY), 30)
def clear_all():
        key = pg.key.get_pressed()
        if key[pg.K_LCTRL] and key[pg.K_c]:
            sc.fill((0, 0, 0))
def random_pict():

    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    if clik[0]:
        sc.blit(images[pict], (posX, posY))
def square():
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    key = pg.key.get_pressed()
    global posXA, posXB, posYB, posYA

    if key[pg.K_LCTRL] and key[pg.K_a]:
        posXA, posYA = pg.mouse.get_pos()
    if key[pg.K_LCTRL] and key[pg.K_b]:
        posXB, posYB = pg.mouse.get_pos()

    squareX, squareY = posXB - posXA, posYB - posYA
    if key[pg.K_SPACE]:
        pg.draw.rect(sc, colour, (posXA, posYA, squareX, squareY), 5)
def circle():
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    key = pg.key.get_pressed()
    global posXA, posXB, posYB, posYA

    if key[pg.K_LCTRL] and key[pg.K_a]:
        posXA, posYA = pg.mouse.get_pos()
    if key[pg.K_LCTRL] and key[pg.K_r]:
        posXB, posYB = pg.mouse.get_pos()

    lineX, lineY = posXB - posXA, posYB - posYA
    R = math.sqrt(lineX**2 + lineY**2)    #math.sqrt(lineX**2 + lineY**2)
    if key[pg.K_SPACE]:
        pg.draw.circle(sc, colour, (posXA, posYA), int(R), 5)
def triangle():
    #posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    key = pg.key.get_pressed()
    global posX1, posY1, posX2, posY2, posX3, posY3

    if key[pg.K_LCTRL] and key[pg.K_1]:
        posX1, posY1 = pg.mouse.get_pos()
    if key[pg.K_LCTRL] and key[pg.K_2]:
        posX2, posY2 = pg.mouse.get_pos()
    if key[pg.K_LCTRL] and key[pg.K_3]:
        posX3, posY3 = pg.mouse.get_pos()

    if key[pg.K_SPACE]:
        pg.draw.polygon(sc, colour, [[posX1, posY1], [posX2, posY2], [posX3, posY3]], 5)
        #pg.draw.polygon(sc, (200, 200, 200), [[200, 300], [200, 500], [700, 200]])
flag = 0
RUN = True
while RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            RUN = False

    for colrs in rects:
        pg.draw.rect(sc, colrs[0], colrs[1])
    sc.blit(random_icon, (1500, 0))
    sqrIcon = pg.draw.rect(sc, (220, 222, 222), (5, 55, 40, 40), 2)
    circleIcon = pg.draw.circle(sc, (200, 200, 200), (25, 125), 20, 2)
    triangleIcon = pg.draw.polygon(sc, (200, 200, 200), [[10, 160], [40, 190], [10, 190]], 2)



    clik = pg.mouse.get_pressed()
    posX, posY = pg.mouse.get_pos()
    if clik[0]:
        if posX > 1500 and posY < 100:
            pict = random.randint(0, len(images)-1)
            flag = 1
        elif posX < 200 and posY < 50:
            flag = 0
        elif posY > 50 and posX < 50 and posY < 300:
            flag = 2

    if flag == 1:
        random_pict()
    elif flag == 0:
        draw()
    elif flag == 2:
        square()
    elif flag == 3:
        circle()
    elif flag == 4:
        triangle()


    shape_pick()
    colour_pick()
    clear_all()
    clock.tick(244)
    pg.display.update()