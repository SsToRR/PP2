import pygame
import random
import sys
import time
import psycopg2

########################
#  1. POSTGRES SETUP   #
########################

def connect_db():
    """Connect to PostgreSQL. Update credentials if needed."""
    return psycopg2.connect(
        host="localhost",
        dbname="snake",    # <-- or your DB name
        user="postgres",
        password="MirasPP2"  # <-- replace with your password
    )

def get_user_id(username):
    """Return user_id from 'users' table; create if not exist."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user:
                return user[0]
            else:
                # Create new user
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                new_id = cur.fetchone()[0]
                conn.commit()
                return new_id

def load_progress(user_id):
    """Return last known score & level for user, or (0,0) if none."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level 
                FROM user_score 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            row = cur.fetchone()
            return row if row else (0, 0)

def save_progress(user_id, score, level):
    """Insert current score & level into 'user_score'."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))
            conn.commit()
    print(f"Progress saved: user_id={user_id}, score={score}, level={level}")

########################
#  2. GAME CONSTANTS   #
########################

USERNAME = input("Enter your username: ")
USER_ID = get_user_id(USERNAME)
score, level = load_progress(USER_ID)

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (80, 80, 80)
YELLOW = (255, 255, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Optional sounds
eat_sound = None
crash_sound = None
try:
    eat_sound = pygame.mixer.Sound("eat.mp3")
    crash_sound = pygame.mixer.Sound("crash.mp3")
except:
    print("Optional: place 'eat.wav' and 'crash.wav' in the same folder if you want sound.")

########################
#  3. LEVEL & WALLS    #
########################

def get_level(score):
    """Returns the level based on the player's score."""
    if score < 5:
        return 0
    elif score < 10:
        return 1
    else:
        return 2

def get_speed(level):
    """Base speed for each level."""
    if level == 0:
        return 8
    elif level == 1:
        return 12
    else:
        return 15

def get_walls_for_level(level):
    """Generate a set of wall coordinates for each level."""
    walls = set()
    # Level 0: border only
    if level >= 0:
        for x in range(GRID_WIDTH):
            walls.add((x, 0))
            walls.add((x, GRID_HEIGHT - 1))
        for y in range(GRID_HEIGHT):
            walls.add((0, y))
            walls.add((GRID_WIDTH - 1, y))

    # Level 1: add a simple diagonal
    if level >= 1:
        for i in range(5, 15):
            walls.add((i, i))

    # Level 2: add some extra blocks in the center
    if level >= 2:
        for i in range(10, 20):
            walls.add((i, GRID_HEIGHT - i))

    return walls

########################
#  4. GAME VARIABLES   #
########################

snake = [(5, 5)]
direction = (1, 0)
game_over = False

food = (0, 0)
food_timer = time.time()
FOOD_LIFETIME = 5
food_value = 1

# We'll define a function to spawn food NOT on wall or snake
def spawn_food():
    global food, food_value, food_timer
    while True:
        candidate = (
            random.randint(1, GRID_WIDTH - 2),
            random.randint(1, GRID_HEIGHT - 2)
        )
        if candidate not in walls and candidate not in snake:
            food = candidate
            break
    food_value = random.choice([1, 2, 3])
    food_timer = time.time()

level = get_level(score)
speed = get_speed(level)
walls = get_walls_for_level(level)
spawn_food()

########################
#  5. CORE FUNCTIONS   #
########################

def draw_all():
    """Draw the entire game scene."""
    win.fill(GREEN)

    # Draw walls
    for wx, wy in walls:
        pygame.draw.rect(win, GRAY, (wx*CELL_SIZE, wy*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(win, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    txt = font.render(str(food_value), True, BLACK)
    win.blit(txt, (food[0]*CELL_SIZE + 5, food[1]*CELL_SIZE))

    # Draw snake
    for sx, sy in snake:
        pygame.draw.rect(win, BLACK, (sx*CELL_SIZE, sy*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Score & level
    s1 = font.render(f"User: {USERNAME}", True, WHITE)
    s2 = font.render(f"Score: {score}", True, WHITE)
    s3 = font.render(f"Level: {level}", True, WHITE)
    win.blit(s1, (10, 10))
    win.blit(s2, (10, 40))
    win.blit(s3, (10, 70))

    pygame.display.update()

def update_snake():
    """Moves snake, checks collisions, spawns new food, updates global score/level/walls/speed if needed."""
    global game_over, score, level, speed, walls

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # Check self collision or wall collision
    if new_head in snake or new_head in walls:
        if crash_sound: crash_sound.play()
        game_over = True
        return

    # Check boundary
    if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
        if crash_sound: crash_sound.play()
        game_over = True
        return

    # Add new head
    snake.insert(0, new_head)

    # If we got the food
    if new_head == food:
        if eat_sound: eat_sound.play()
        global food_value
        score += food_value
        spawn_food()
        # Possibly update level/speed/walls
        new_level = get_level(score)
        if new_level != level:
            level = new_level
            speed = get_speed(level)
            walls = get_walls_for_level(level)
    else:
        snake.pop()

    # Food lifetime
    if time.time() - food_timer > FOOD_LIFETIME:
        spawn_food()

def pause_game():
    """Pause the game, save to DB, wait for user input (resume or quit)."""
    save_progress(USER_ID, score, level)

    paused_text = font.render("Paused: Press C to continue, Q to quit", True, YELLOW)
    paused = True
    while paused:
        win.fill(BLACK)
        win.blit(paused_text, (WIDTH//2 - paused_text.get_width()//2, HEIGHT//2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    save_progress(USER_ID, score, level)
                    pygame.quit()
                    sys.exit()

########################
#  6. MAIN GAME LOOP   #
########################

while True:
    clock.tick(speed)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_p:
                    pause_game()

        update_snake()
        draw_all()
    else:
        # Game Over state
        win.fill(BLACK)
        go_text = font.render("Game Over! Press R to Restart", True, YELLOW)
        sc_text = font.render(f"Final Score: {score}", True, WHITE)
        win.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2 - 30))
        win.blit(sc_text, (WIDTH//2 - sc_text.get_width()//2, HEIGHT//2 + 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset
                    snake = [(5,5)]
                    direction = (1,0)
                    score, level = 0, 0
                    speed = get_speed(level)
                    walls = get_walls_for_level(level)
                    spawn_food()
                    game_over = False
