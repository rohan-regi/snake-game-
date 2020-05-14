import pygame
import random
import time
import math

pygame.init()
screen = pygame.display.set_mode((640 + 32, 640 + 32))
delay = .15

segmentX = []
segmentY = []
body = 0
out = 0
score_high = 0

# player
snekimg = pygame.image.load('rectangle.png')
snekX = 0
snekY = 640
snekX_change = 0
snekY_change = 0

# food
gridX = random.randint(0, 20)
gridY = random.randint(0, 20)
foodimg = pygame.image.load('square.png')
foodX = 32 * gridX
foodY = 32 * gridY

# Game over text
over_font = pygame.font.Font('game_over.ttf', 300)
continuetext = pygame.font.Font('game_over.ttf', 150)

# Score
score_value = 0
font = pygame.font.Font('game_over.ttf', 100)

textX = 0
textY = 10


def show_score(x, y):
    score = font.render("SCORE :" + str(score_value), True, (0, 0, 225))
    screen.blit(score, (x, y))


def high_score(x, y):
    high = font.render("HIGHEST :" + str(score_high), True, (0, 0, 225))
    screen.blit(high, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (-10, 150))


def continue_text():
    continueText = continuetext.render("To continue press space", True, (0, 0, 0))
    screen.blit(continueText, (0, 20))


def Delay():
    time.sleep(2)


def snek(x, y):
    screen.blit(snekimg, (x, y))


def food(x, y):
    screen.blit(foodimg, (x, y))


# game loop
running = True
while running:
    # rgb
    screen.fill((128, 128, 128))
    # movement
    out = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if a keystroke is pressed check whether right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snekX_change == 0:
                snekY_change = 0
                snekX_change = -32
            elif event.key == pygame.K_RIGHT and snekX_change == 0:
                snekY_change = 0
                snekX_change = 32
            elif event.key == pygame.K_UP and snekY_change == 0:
                snekX_change = 0
                snekY_change = -32
            elif event.key == pygame.K_DOWN and snekY_change == 0:
                snekX_change = 0
                snekY_change = 32
    # High score
    if score_value > score_high:
        score_high = score_value
    # body snake
    segmentX.insert(0, snekX)
    segmentY.insert(0, snekY)
    del segmentY[body:len(segmentY)]
    del segmentX[body:len(segmentX)]

    for index in range(0, body, 1):
        snek(segmentX[index], segmentY[index])
        if out:
            segmentX.clear()
            segmentY.clear()
            body = 0
            break

    # Body collision
    for index in range(1, body, 1):
        if snekX == segmentX[index] and snekY == segmentY[index]:
            snekX = 0
            snekY = 0
            snekX_change = 0
            snekY_change = 0
            out = True
            score_value = 0
        if foodX == segmentX[index] and foodY == segmentY[index]:
            gridX = random.randint(0, 20)
            gridY = random.randint(0, 20)
            foodX = 32 * gridX
            foodY = 32 * gridY
    snekX += snekX_change
    snekY += snekY_change
    # Boundary snek
    if snekX < 0:
        snekX = 0
        snekY = 0
        snekX_change = 0
        snekY_change = 0
        segmentY.clear()
        segmentX.clear()
        body = 0
        game_over_text()
        out = True
        score_value = 0
    elif snekX > 640:
        snekX = 0
        snekY = 0
        snekX_change = 0
        snekY_change = 0
        segmentY.clear()
        segmentX.clear()
        body = 0
        game_over_text()
        out = True
        score_value = 0
    if snekY < 0:
        snekX = 0
        snekY = 0
        snekX_change = 0
        snekY_change = 0
        segmentY.clear()
        segmentX.clear()
        body = 0
        game_over_text()
        out = True
        score_value = 0
    elif snekY > 640:
        snekX = 0
        snekY = 0
        snekX_change = 0
        snekY_change = 0
        segmentY.clear()
        segmentX.clear()
        body = 0
        game_over_text()
        out = True
        score_value = 0
    # Game over screen
    while out:
        screen.fill((255, 255, 255))
        game_over_text()
        continue_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    out = False
        pygame.display.update()

    # Food collision
    if math.sqrt(math.pow((snekX - foodX), 2) + math.pow((snekY - foodY), 2)) == 0:
        gridX = random.randint(0, 20)
        gridY = random.randint(0, 20)
        foodX = 32 * gridX
        foodY = 32 * gridY
        food(foodX, foodY)
        body += 1
        score_value += 1

    high_score(400, 10)
    food(foodX, foodY)
    snek(snekX, snekY)
    show_score(textX, textY)
    time.sleep(delay)
    pygame.display.update()
