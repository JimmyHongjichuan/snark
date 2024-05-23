
import random

import pygame

SCREEN_SIZE = [1000, 800]
WHITE = (255, 255, 255)

CELL_RADIUS = 20
SNAKE_COLOR = (0, 0, 0)

FOOD_COLOR = (0, 70, 39)
FOOD_RADIUS = 20

UPDATE = pygame.USEREVENT + 1
Food = pygame.USEREVENT + 2

LIGHT_GREY = (100, 100, 100)
MSG_POSITION = (300, 500)


def init_game():
    pygame.init()
    pygame.display.set_caption("snake 贪吃蛇")
    pygame.time.set_timer(UPDATE, 500)
    pygame.time.set_timer(Food, 3000)


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()
        self.food = None
        self.message = None


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y

    def copy(self):
        return Cell(self.x, self.y)

    def update(self, direction):
        if direction == "U":
            self.y -= CELL_RADIUS * 2
        elif direction == "D":
            self.y += CELL_RADIUS * 2
        elif direction == "L":
            self.x -= CELL_RADIUS * 2
        elif direction == "R":
            self.x += CELL_RADIUS * 2


class Snake:
    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = (SCREEN_SIZE[0] / cell_diameter // 2) * cell_diameter
        y = (SCREEN_SIZE[1] / cell_diameter // 2) * cell_diameter

        self.body = [Cell(x, y)]
        self.cell_size = CELL_RADIUS
        self.color = SNAKE_COLOR
        self.direction = "L"

    def update(self):
        head = self.body[0].copy()
        self.body.pop()
        head.update(self.direction)
        self.body.insert(0, head)


def is_snake_food_collide():
    head = game.snake.body[0].copy()
    head.update(game.snake.direction)
    return (game.food[0] - head.x) == 0 and (game.food[1] - head.y) == 0


def update():
    check_snake_dir()
    check_food()
    check_head_body_collision()
    check_out_boundary()
    check_win()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == UPDATE:
            game.snake.update()
        if event.type == Food:
            generate_food()


def check_win():
    length = len(game.snake.body)
    cell_diameter = CELL_RADIUS * 2
    max_cell_x = SCREEN_SIZE[0] // cell_diameter
    max_cell_y = SCREEN_SIZE[1] // cell_diameter
    if length == 15:  # max_cell_x * max_cell_y:
        game.running = False
        game.message = "You WIN the game. Should restart? y/n"


def check_out_boundary():
    cell_diameter = 2 * CELL_RADIUS
    out_boundary_x_cells = [cell for cell in game.snake.body if
                            cell.x < cell_diameter or cell.x > SCREEN_SIZE[0] - cell_diameter]
    out_boundary_y_cells = [cell for cell in game.snake.body if
                            cell.y < cell_diameter or cell.y > SCREEN_SIZE[1] - cell_diameter]
    if len(out_boundary_x_cells) > 0 or len(out_boundary_y_cells) > 0:
        game.running = False
        game.message = "Snake is out of boundary. Should restart? y/n"


def check_head_body_collision():
    head = game.snake.body[0]
    body = game.snake.body
    try:
        index = [cell.to_tuple() for cell in body[1:]].index(head.to_tuple())
    except ValueError:
        index = -1
    if len(game.snake.body) > 1 and index > -1:
        game.snake.body = game.snake.body[:index]


def check_food():
    if game.food is not None and is_snake_food_collide():
        cell = Cell(game.food[0], game.food[1])
        game.snake.body.insert(0, cell)
        game.food = None


def check_snake_dir():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] and not game.snake.direction == "D":
        game.snake.direction = "U"
    if pressed_keys[pygame.K_DOWN] and not game.snake.direction == "U":
        game.snake.direction = "D"
    if pressed_keys[pygame.K_LEFT] and not game.snake.direction == "R":
        game.snake.direction = "L"
    if pressed_keys[pygame.K_RIGHT] and not game.snake.direction == "L":
        game.snake.direction = "R"


def generate_food():
    while game.food is None:
        cell_diameter = CELL_RADIUS * 2
        rand_x = random.randint(1, (SCREEN_SIZE[0] / cell_diameter) - 1) * cell_diameter
        rand_y = random.randint(1, (SCREEN_SIZE[1] / cell_diameter) - 1) * cell_diameter
        if (rand_x, rand_y) not in [cell.to_tuple() for cell in game.snake.body]:
            game.food = (rand_x, rand_y)


def draw():
    game.screen.fill(WHITE)
    if game.running:
        draw_snake()
        draw_food()
    else:
        draw_restart()
    pygame.display.flip()


def draw_restart():
    font = pygame.font.Font(None, 30)
    restart_msg = font.render(game.message, True, LIGHT_GREY)
    game.screen.blit(restart_msg, MSG_POSITION)


def draw_food():
    if game.food is not None:
        pygame.draw.circle(game.screen, FOOD_COLOR, game.food, FOOD_RADIUS)


def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen, game.snake.color, cell.to_tuple(), game.snake.cell_size)


def check_reatart():
    while not game.running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_y:
                game.snake = Snake()
                game.running = True
            if event.type == pygame.KEYUP and event.key == pygame.K_n:
                return


if __name__ == "__main__":
    init_game()
    game = Game()
    while game.running:
        update()
        draw()
        check_reatart()

    pygame.quit()
