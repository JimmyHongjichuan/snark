import random

import pygame

SCREEN_SIZE = [1000,800]
WHITE = (255,255,255)

CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0)


UPDATE = pygame.USEREVENT + 1
FOOD = pygame.USEREVENT + 2


def init_game() -> object:
    pygame.init()
    pygame.display.set_caption("贪吃蛇")
    pygame.time.set_timer(UPDATE, 500)
    pygame.time.set_timer(FOOD, 3000)
class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()
        self.food = None



class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x,self.y

    def copy(self):
        return Cell(self.x, self.y)

    def update(self, direction):
        if direction == "U":
            self.y -= CELL_RADIUS * 2
        elif direction == "D":
            self.y += CELL_RADIUS * 2
        elif direction == "L":
            self.x -= CELL_RADIUS * 2
        elif ddirection == "R":
            self.x += CELL_RADIUS * 2
class Snake:
    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = (SCREEN_SIZE[0]/cell_diameter//2)*cell_diameter
        y = (SCREEN_SIZE[1]/cell_diameter//2)*cell_diameter

        self.body = [Cell(x, y),Cell(x+40, y),Cell(x+80, y)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR
        self.direction = "L"

    def update(self):
        head = self.body[0].copy()
        self.body.pop()
        head.update(self.direction)
        self.body.insert(0, head)





def update():
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             game.running = False
         if event.type == UPDATE:
             game.snake.update()
         if event.type == FOOD:
             generate_food()


def generate_food():
    while game.food is None:
        cell_diameter = CELL_RADIUS * 2
        rand_x = random.randint(1, (SCREEN_SIZE[0] / cell_diameter) - 1) * cell_diameter
        rand_y = random.randint(1, (SCREEN_SIZE[1] / cell_diameter) - 1) * cell_diameter
        if (rand_x, rand_y) not in [cell.to_tuple() for cell in game.snake.body]:
            game.food = (rand_x, rand_y)


def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen, game.snake.color, cell.to_tuple(), game.snake.cell_size)

def draw():
    game.screen.fill(WHITE)
    draw_snake()
    draw_food()
    pygame.display.flip()


def draw_food():
    if game.food is not None:
        pygame.draw.circle(game.screen, (0, 100, 0), game.food, FOOD_RADIUS)


if __name__ == "__main__":
    init_game()
    game = Game()
    while game.running:
        update()
        draw()
    pygame.quit()

