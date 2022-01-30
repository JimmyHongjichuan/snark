import pygame

SCREEN_SIZE = [1000,800]
WHITE = (255,255,255)

CELL_RADIUS = 20
SNAKE_COLOR = (0,0,0)

def init_game() -> object:
    pygame.init()
    pygame.display.set_caption("贪吃蛇")


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.snake = Snake()



class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x,self.y


class Snake:
    def __init__(self):
        cell_diameter = CELL_RADIUS * 2
        x = (SCREEN_SIZE[0]/cell_diameter//2)*cell_diameter
        y = (SCREEN_SIZE[1]/cell_diameter//2)*cell_diameter

        self.body = [Cell(x, y)]
        self.cell_size = CELL_RADIUS

        self.color = SNAKE_COLOR


def update():
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             game.running = False


def draw_snake():
    for cell in game.snake.body:
        pygame.draw.circle(game.screen, game.snake.color, cell.to_tuple(), game.snake.cell_size)

def draw():
    game.screen.fill(WHITE)
    draw_snake()
    pygame.display.flip()


if __name__ == "__main__":
    init_game()
    game = Game()
    while game.running:
        update()
        draw()
    pygame.quit()