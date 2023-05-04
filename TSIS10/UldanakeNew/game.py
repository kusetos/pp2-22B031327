import pygame as pg
import pygame.image
import pygame_menu as pg_menu
from pygame.math import Vector2
import sys, random, time, os

from pygame_menu import themes
pg.init()

print("nickname")
nickname = 'boyyy' #input()
#face = pg.image.load("face_left.png")
tail_right = pg.image.load("rainbow_tial.png")
tail_up = pg.transform.rotate(tail_right, 90)
tail_left = pg.transform.rotate(tail_up, 90)
tail_down = pg.transform.rotate(tail_left, 90)

body_horizontal = pg.image.load("rainbow_body.png")
body_vertical = pg.transform.rotate(body_horizontal, 90)

body_tl = pg.image.load("body_tl.png")
body_tr = pg.image.load("body_tr.png")

body_bl = pg.image.load("body_bl.png")
body_br =pg.image.load("body_br.png")

brokoli = pg.image.load("brokoli.png")
brokoli = pg.transform.scale(brokoli, (50, 50))

cherry = pg.image.load("cherry.png")
cherry = pg.transform.scale(cherry, (50, 50))
fruit_list = [brokoli, cherry]

bang = pg.image.load("real_bang.png")
bang = pg.transform.scale(bang, (50, 50))

dimond = pg.image.load("diamond_ore.png")
dimond = pg.transform.scale(dimond, (50, 50))


def menu():
    mainmenu.mainloop(sc)

class Wall:
    def __init__(self):
        self.respawn()
        #random gen
    def draw_wall(self):
        for i in range(self.walls_number):
            wall_rect = pg.Rect(int(self.pos[i][0] * cell_size), int(self.pos[i][1] * cell_size), cell_size, cell_size)
            sc.blit(dimond, wall_rect)
    def respawn(self):

        self.walls_number = random.randint(1, 50)
        self.pos = []
        x = []
        y = []
        #empty_block = []
        for i in range(self.walls_number):
            x.append(random.randint(1, cell_number-2))
            y.append(random.choice([x for x  in range(1, cell_number-2) if x != 9]))      # random.randint(1, cell_number-2) )
            self.pos.append(pg.math.Vector2(x[len(x)-1], y[len(y)-1]))

        for i in range(cell_number-2):
            for j in range(cell_number-2):
                empty_rect = pg.math.Vector2(i, j)
                flag = 0
                for block in self.pos:
                    relation = block - empty_rect
                    if relation == Vector2(0, -1):
                        flag += 1

                    if relation == Vector2(-1, 0):
                        flag += 1

                    if relation == Vector2(0, 1):
                        flag += 1

                    if relation == Vector2(1, 0):
                        flag += 1
                if flag > 2:
                    self.pos.append(pg.math.Vector2(i, j))


class Fruit:
    def __init__(self):
        self.respawn()
        self.rand_fruit = random.randint(0, 1)
    def draw_fruits(self):
        fruit_rect = pg.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        current_time = pg.time.get_ticks()
        #picture of bang at las 400 milisec
        if current_time - self.time_of_spawn < 4600:
            sc.blit(self.fruit_list[self.rand_fruit], fruit_rect)
        else:
            sc.blit(bang, fruit_rect)

        #pg.draw.rect(sc, (200, 50, 0), fruit_rect)
        if current_time - self.time_of_spawn > 5000:
           self.respawn()

        #fruits became smaller and smaller
        if (current_time - self.time_of_spawn) % 10 == 0:
            if self.x > 10:
                self.x = (5000 - (current_time - self.time_of_spawn) )/100-1
            self.fruit_list = [self.brokoli, self.cherry]
            self.fruit_list[self.rand_fruit] = pg.transform.scale(self.fruit_list[self.rand_fruit], (self.x, self.x))

    def respawn(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pg.math.Vector2(self.x, self.y)
        self.rand_fruit = random.randint(0, 1)
        self.time_of_spawn = pg.time.get_ticks()
        self.brokoli = brokoli
        self.cherry = cherry
        self.fruit_list = [self. brokoli, self.cherry]
        self.x = 50



class Snake:
    def __init__(self):
        self.body = [Vector2(5, 9), Vector2(4, 9), Vector2(3, 9)]
        self.direction = Vector2(1, 0)
        self.new_body = False

        self.face_left = pg.image.load("face_left.png")
        self.face_right = pg.image.load("face_right.png")
        self.face_down = pg.image.load("face_down.png")
        self.face_up = pg.image.load("face_up.png")

        self.tail_up = tail_up.convert_alpha()
        self.tail_down = tail_down.convert_alpha()
        self.tail_right = tail_right.convert_alpha()
        self.tail_left = tail_left.convert_alpha()

        self.body_vertical = body_vertical.convert_alpha()
        self.body_horizontal = body_horizontal.convert_alpha()

        self.body_tl = body_tl.convert_alpha()
        self.body_tr = body_tr.convert_alpha()
        self.body_br = body_br.convert_alpha()
        self.body_bl = body_bl.convert_alpha()



    def draw_snake(self):

        self.face = self.face_up
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.face = self.face_left
        elif head_relation == Vector2(-1, 0):
            self.face = self.face_right
        elif head_relation == Vector2(0, 1):
            self.face = self.face_up
        elif head_relation == Vector2(0, -1):
            self.face = self.face_down

        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up

        for i, body in enumerate(self.body):
            posX = int(body.x * cell_size)
            posY = int(body.y * cell_size)
            snake_body = pg.Rect(posX, posY, cell_size, cell_size)

            if i == 0:
                sc.blit(self.face, snake_body)

            elif i == len(self.body)-1:
                sc.blit(self.tail, snake_body)

            else:
                previous_block = self.body[i+1] - body
                next_block = self.body[i-1] - body
                if previous_block.x == next_block.x:
                    sc.blit(self.body_vertical, snake_body)
                elif previous_block.y == next_block.y:
                    sc.blit(self.body_horizontal, snake_body)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        sc.blit(self.body_bl, snake_body)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y ==  1 and next_block.x == 1:
                        sc.blit(self.body_tl, snake_body)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y ==  1 and next_block.x == -1:
                        sc.blit(self.body_br, snake_body)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        sc.blit(self.body_tr, snake_body)



    def snake_move(self):
        if self.new_body == True:
            body_head = self.body[:]
            body_head.insert(0, body_head[0] + self.direction)
            self.body = body_head[:]
            self.new_body = False
        else:
            body_head = self.body[:-1]
            body_head.insert(0, body_head[0] + self.direction)
            self.body = body_head[:]
    def add_body(self):
        self.new_body = True
    def rest(self):
        self.body = [Vector2(5, 9), Vector2(4, 9), Vector2(3, 9)]
        self.direction = Vector2(1, 0)


class MAIN():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.wall = Wall()
        #self.alive = True

    def snake_update(self):
        self.snake.snake_move()
        self.collision()
        self.fail_cheker()
    def draw_all(self):
        self.snake.draw_snake()
        self.fruit.draw_fruits()
        self.wall.draw_wall()
    def collision(self):
        global score
        if self.fruit.pos == self.snake.body[0]:
            if self.fruit.rand_fruit == 0:
                score += 1
            elif self.fruit.rand_fruit == 1:
                score += 2
            self.fruit.respawn()
            self.snake.add_body()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.respawn()
        for block in self.wall.pos:
            if block == self.fruit.pos:
                self.fruit.respawn()

    def fail_cheker(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            #self.alive = False
            self.game_end()

        for body in self.snake.body[1:]:
            if body == self.snake.body[0]:
                #self.alive = False
                self.game_end()
            for i in range(self.wall.walls_number):
                if self.snake.body[0] == self.wall.pos[i]:
                    self.game_end()


    def game_end(self):

        global score
        score = 0

        sc.fill((0, 0, 0))
        game_over = restart_font.render("GAME OVER", True, (220, 0, 0))
        press_space = normal_font.render("PRESS SPACE TO RESTART", True,(200, 0, 0))
        sc.blit(game_over, (400, 400))
        sc.blit(press_space, (400, 500))
        self.wall.respawn()
        self.snake.rest()
        menu()




pg.init()

restart_font = pg.font.SysFont("Areal", 60)


cell_number = 20
cell_size = 50


big_font = pg.font.SysFont("Areal", 60)
normal_font = pg.font.SysFont("Areal", 60)


clock = pg.time.Clock()
FPS = 60
sc = pg.display.set_mode((int(cell_number * cell_size), int(cell_size* cell_number)))

chessBG = pg.image.load("pgSnake.png")



speed = 150

MAIN_GAME = MAIN()
Snake = Snake()

screen_update = pg.USEREVENT
pg.time.set_timer(screen_update, speed)



score = 0
pg.time.set_timer(screen_update, speed)
def incrSpeed():
    if score == 5:
        global speed
        speed = 100
    pg.time.set_timer(screen_update, speed)

#menu settings



run = True
i = 0
def start_the_game():
    def moves_binds():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                if MAIN_GAME.snake.direction.y != -1:
                    MAIN_GAME.snake.direction = Vector2(0, 1)
            if event.key == pg.K_LEFT:
                if MAIN_GAME.snake.direction.x != 1:
                    MAIN_GAME.snake.direction = Vector2(-1, 0)
            if event.key == pg.K_UP:
                if MAIN_GAME.snake.direction.y != 1:
                    MAIN_GAME.snake.direction = Vector2(0, -1)
            if event.key == pg.K_RIGHT:
                if MAIN_GAME.snake.direction.x != -1:
                    MAIN_GAME.snake.direction = Vector2(1, 0)
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == screen_update:
                MAIN_GAME.snake_update()
            moves_binds()


        sc.blit(chessBG, (0, 0))


        # score of fruits cherry - 2, brokoli - 1
        score_fruits = normal_font.render(str(score), True, (200, 200, 200))
        sc.blit(score_fruits, (0, 0))

       # incrSpeed()
        speed = 1
        MAIN_GAME.draw_all()
        pg.display.update()
        clock.tick(60)





mainmenu = pg_menu.Menu("Salamaleikum", 1000, 1000, theme=themes.THEME_DARK)
mainmenu.add.text_input("Name: ", default=nickname, maxchar=20)

mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Quit', pg_menu.events.EXIT)
# with open('names', 'r') as file:
#     for line in file:
#         if nickname in line:
#             print("eto basa")
#             break
#         else:
#             with open("names", "a") as file:
#                 file.write("\n"+ nickname)
# file.close()

menu()

