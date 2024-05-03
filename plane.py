import pygame
import random
import math


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("无敌飞机✈")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
bgImg = pygame.image.load("bg.png")
playerImg = pygame.image.load("player.png")
playerX = 400
playerY = 500
playerStep = 2
number_of_enemies = 6

score = 0
font = pygame.font.Font('freesansbold.ttf',32)


def shou_score():
    text = f"Score:{score}"
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))


class Enemy:
    def __init__(self):
        self.img = pygame.image.load("enemy.png")
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(2, 4)

    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 200)


enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())


def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)
print(distance(1,1,4,5))


class Bullet:
    def __init__(self):
        self.img = pygame.image.load("bullet.png")
        self.x = playerX + 8
        self.y = playerY + 10
        self.step = 1

    def hit(self):
        global score
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                bullets.remove(self)
                e.reset()
                score += 1
                print(score)


bullets = []


def shou_bullet():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)



def shou_enemy():
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 736 or e.x < 0:
            e.step *= -1
            e.y += 40


def move_player():
    global playerX
    playerX += playerStep
    if playerX > 720:
        playerX = 720
    if playerX < 0:
        playerX = 0


running = True
screen.blit(bgImg, (0, 0))


def shou_bullets():
    pass


while running:
    screen.blit(bgImg, (0, 0))
    shou_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStep = 5
            elif event.key == pygame.K_LEFT:
                playerStep = -5
            elif event.key == pygame.K_SPACE:
                print('发射子弹...... ')
                bullets.append(Bullet())
        if event.type == pygame.KEYUP:
            playerStep = 0


    screen.blit(playerImg, (playerX, playerY))
    move_player()
    shou_enemy()
    shou_bullet()
    pygame.display.update()