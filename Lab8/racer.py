import pygame
import random
import sys

# Initialize
pygame.init()
pygame.mixer.init()

# Window setup
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Clock
FPS = 60
clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/player_car.png")
enemy_img = pygame.image.load("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/enemy_car.png")
coin_img = pygame.image.load("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/coin.png")
road_img = pygame.image.load("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/road.png")

# Resize images
player_img = pygame.transform.scale(player_img, (60, 100))
enemy_img = pygame.transform.scale(enemy_img, (60, 100))
coin_img = pygame.transform.scale(coin_img, (40, 40))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Load sounds
crash_sound = pygame.mixer.Sound("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/crash.mp3")
coin_sound = pygame.mixer.Sound("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/coin.mp3")
drive_sound = pygame.mixer.Sound("C:/Users/Miras/Desktop/Projects/PP2/Lab8/assets/drive.mp3")
drive_sound.play(-1)  # Loop driving sound

# Lanes
lanes = [60, 170, 280]  # x positions for 3 lanes

# Player setup
player_x = lanes[1]
player_y = HEIGHT - 120
player_speed = 5

# Coin counter
collected_coins = 0
font = pygame.font.SysFont("Arial", 24)

# Game state
game_over = False

# Coin setup
coin = {"x": random.choice(lanes), "y": -50}

# Multiple enemies
def create_enemy():
    return {"x": random.choice(lanes), "y": random.randint(-600, -100)}

enemies = [create_enemy() for _ in range(3)]
enemy_speed = 5
coin_speed = 4

def draw_window():
    win.blit(road_img, (0, 0))
    win.blit(player_img, (player_x, player_y))
    for enemy in enemies:
        win.blit(enemy_img, (enemy["x"], enemy["y"]))
    win.blit(coin_img, (coin["x"], coin["y"]))

    # Draw coin count
    coin_text = font.render(f"Coins: {collected_coins}", True, (255, 255, 255))
    win.blit(coin_text, (WIDTH - coin_text.get_width() - 10, 10))

    pygame.display.update()

def reset_game():
    global player_x, collected_coins, enemies, coin, game_over
    player_x = lanes[1]
    collected_coins = 0
    enemies = [create_enemy() for _ in range(3)]
    coin = {"x": random.choice(lanes), "y": -50}
    game_over = False
    drive_sound.play(-1)

# Main loop
while True:
    clock.tick(FPS)

    if not game_over:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            index = lanes.index(player_x)
            if index > 0:
                player_x = lanes[index - 1]
                pygame.time.delay(100)  # Prevent fast multiple moves
        if keys[pygame.K_RIGHT]:
            index = lanes.index(player_x)
            if index < len(lanes) - 1:
                player_x = lanes[index + 1]
                pygame.time.delay(100)

        # Move enemies
        for enemy in enemies:
            enemy["y"] += enemy_speed
            if enemy["y"] > HEIGHT:
                enemy["x"] = random.choice(lanes)
                enemy["y"] = random.randint(-600, -100)

            # Collision
            player_rect = pygame.Rect(player_x, player_y, 60, 100)
            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 60, 100)
            if player_rect.colliderect(enemy_rect):
                crash_sound.play()
                drive_sound.stop()
                game_over = True

        # Move coin
        coin["y"] += coin_speed
        if coin["y"] > HEIGHT:
            coin["y"] = -50
            coin["x"] = random.choice(lanes)

        coin_rect = pygame.Rect(coin["x"], coin["y"], 40, 40)
        if player_rect.colliderect(coin_rect):
            collected_coins += 1
            coin_sound.play()
            coin["y"] = -50
            coin["x"] = random.choice(lanes)

        # Draw
        draw_window()

    else:
        # Game Over screen
        win.fill((0, 0, 0))
        over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        win.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
