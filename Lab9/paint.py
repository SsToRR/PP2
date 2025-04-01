import pygame
import sys

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PALETTE = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
ERASER_COLOR = WHITE

# Font
font = pygame.font.SysFont("Arial", 18)

# Brush settings
current_color = BLACK
brush_size = 5

# Canvas background
win.fill(WHITE)

# Drawing state
drawing = False
start_pos = None
current_shape = "free"  # Modes: "free", "square", "right_triangle", "equilateral_triangle", "rhombus"

# UI: Color palette
palette_rects = []
for i, color in enumerate(PALETTE):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    palette_rects.append((rect, color))

# Buttons
eraser_btn = pygame.Rect(10, 50, 80, 30)
save_btn = pygame.Rect(100, 50, 80, 30)

def draw_ui():
    # Clear the top UI area (prevent stacking)
    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, 100))

    # Draw color palette
    for rect, color in palette_rects:
        pygame.draw.rect(win, color, rect)
        if color == current_color:
            pygame.draw.rect(win, WHITE, rect, 3)  # Highlight selected color

    # Draw eraser button
    pygame.draw.rect(win, (200, 200, 200), eraser_btn)
    win.blit(font.render("Eraser", True, BLACK), (eraser_btn.x + 10, eraser_btn.y + 5))

    # Draw save button
    pygame.draw.rect(win, (200, 200, 200), save_btn)
    win.blit(font.render("Save", True, BLACK), (save_btn.x + 20, save_btn.y + 5))

    # Show current drawing mode
    shape_text = font.render(f"Mode: {current_shape}", True, BLACK)
    win.blit(shape_text, (200, 55))


def save_drawing():
    pygame.image.save(win, "drawing.png")
    print("Saved to drawing.png")

def draw_shape(shape, start, end):
    x1, y1 = start
    x2, y2 = end

    if shape == "square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(win, current_color, pygame.Rect(x1, y1, side, side))

    elif shape == "right_triangle":
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(win, current_color, points)

    elif shape == "equilateral_triangle":
        base = x2 - x1
        height = (3**0.5 / 2) * abs(base)
        if y2 < y1:
            points = [(x1, y1), (x2, y1), ((x1 + x2) // 2, y1 - int(height))]
        else:
            points = [(x1, y1), (x2, y1), ((x1 + x2) // 2, y1 + int(height))]
        pygame.draw.polygon(win, current_color, points)

    elif shape == "rhombus":
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [(center_x, y1), (x2, center_y), (center_x, y2), (x1, center_y)]
        pygame.draw.polygon(win, current_color, points)

# Main loop
run = True
while run:
    draw_ui()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_shape = "square"
            elif event.key == pygame.K_2:
                current_shape = "right_triangle"
            elif event.key == pygame.K_3:
                current_shape = "equilateral_triangle"
            elif event.key == pygame.K_4:
                current_shape = "rhombus"
            elif event.key == pygame.K_0:
                current_shape = "free"

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                drawing = True
                start_pos = mouse_pos

                # Check palette selection
                for rect, color in palette_rects:
                    if rect.collidepoint(mouse_pos):
                        current_color = color
                        drawing = False

                if eraser_btn.collidepoint(mouse_pos):
                    current_color = ERASER_COLOR
                    drawing = False

                if save_btn.collidepoint(mouse_pos):
                    save_drawing()
                    drawing = False

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = pygame.mouse.get_pos()
                if current_shape != "free":
                    draw_shape(current_shape, start_pos, end_pos)
                drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing and current_shape == "free":
            mx, my = pygame.mouse.get_pos()
            pygame.draw.circle(win, current_color, (mx, my), brush_size)

pygame.quit()
sys.exit()
