import pygame
import time
import random

pygame.init()

# Window dimensions
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
RED = (213, 50, 80)
WHITE = (255, 255, 255)

# Display setup
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game with Images')

# Load images
snake_img = pygame.image.load("snake.png")  # Must be 20x20 or scaled
food_img = pygame.image.load("food.png")    # Optional

# Scale images to fit grid size
snake_img = pygame.transform.scale(snake_img, (CELL_SIZE, CELL_SIZE))
food_img = pygame.transform.scale(food_img, (CELL_SIZE, CELL_SIZE))

# Font and clock
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()
snake_speed = 15

def score_display(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    win.blit(value, [0, 0])

def draw_snake(snake_list):
    for x in snake_list:
        win.blit(snake_img, (x[0], x[1]))

def message(msg, color):
    mesg = font.render(msg, True, color)
    win.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - CELL_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - CELL_SIZE) / 20.0) * 20.0

    while not game_over:
        while game_close:
            win.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -CELL_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = CELL_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(BLACK)
        win.blit(food_img, (foodx, foody))
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        score_display(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - CELL_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - CELL_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
