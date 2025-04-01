import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Setup
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Sounds
eat_sound = pygame.mixer.Sound("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/crash.mp3")
crash_sound = pygame.mixer.Sound("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/coin.mp3")

# Snake and food setup
snake = [(5, 5)]
direction = (1, 0)
score = 0
speed = 10
game_over = False

# Food values and timers
food_weights = [1, 2, 3]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
food_value = random.choice(food_weights)
food_timer = time.time()  # Start timer when food spawns
FOOD_LIFETIME = 5  # Food disappears after 5 seconds

def draw_grid():
    win.fill(GREEN)

    # Draw food
    pygame.draw.rect(win, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    food_text = font.render(str(food_value), True, BLACK)
    win.blit(food_text, (food[0]*CELL_SIZE + 5, food[1]*CELL_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(win, BLACK, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))
    pygame.display.update()

def reset_game():
    global snake, direction, food, food_value, score, speed, game_over, food_timer
    snake = [(5, 5)]
    direction = (1, 0)
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    food_value = random.choice(food_weights)
    food_timer = time.time()
    score = 0
    speed = 10
    game_over = False

def update_snake():
    global food, food_value, score, speed, game_over, food_timer
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # Check wall collision
    if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
        crash_sound.play()
        game_over = True
        return

    # Check self collision
    if new_head in snake:
        crash_sound.play()
        game_over = True
        return

    # Move snake
    snake.insert(0, new_head)

    # Check food collision
    if new_head == food:
        eat_sound.play()
        score += food_value
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food_value = random.choice(food_weights)
        food_timer = time.time()

        if score % 5 == 0:
            speed += 2
    else:
        snake.pop()

    # If food timer expires
    if time.time() - food_timer > FOOD_LIFETIME:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food_value = random.choice(food_weights)
        food_timer = time.time()

# ===================
# ====== GAME LOOP
# ===================
while True:
    clock.tick(speed)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Direction control
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        update_snake()
        draw_grid()

    else:
        # Game Over screen
        win.fill(BLACK)
        over_text = font.render("Game Over! Press R to Restart", True, YELLOW)
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        win.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 20))
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 20))
        pygame.display.update()

        # Wait for R to restart
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
