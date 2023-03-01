import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
done = False

# paddle_a coords
x = 10
y = 230

# paddle_b coords
a = 775
b = 230

# ball coords
posX_ball = 300
posY_ball = 200
ball_right = True
ball_top = True
speed = 3


FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

surface = pygame.image.load('art.jpg')
pygame.display.set_icon(surface)
pygame.display.set_caption("колобок повесился")

# Paddle A
paddle_a = pygame.Rect(50, 50, 15, 140)
# Paddle wB
paddle_b = pygame.Rect(50, 50, 15, 140)
# Ball
ball = pygame.Rect(50, 50, 15, 15)
# 50, 50 xy во всех не важны и потом все равно изменятся

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# moving paddle_a
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 0:
        y -= 5
    if pressed[pygame.K_DOWN] and y < 600 - 140:
        y += 5
    if pressed[pygame.K_LEFT] and x > 0:
        x -= 5
    if pressed[pygame.K_RIGHT] and x < 800 - 15:
        x += 5
# moving paddle_b
    if pressed[pygame.K_w] and b > 0:
        b -= 5
    if pressed[pygame.K_s] and b < 600 - 140:
        b += 5
    if pressed[pygame.K_a] and a > 0:
        a -= 5
    if pressed[pygame.K_d] and a < 800 - 15:
        a += 5

    paddle_a.x, paddle_a.y = x, y
    paddle_b.x, paddle_b.y = a, b

    # ball moving
    if posY_ball - 20 <= 0:
        ball_right = True
    if posY_ball - 20 <= 0:
        ball_top = False

    elif posY_ball + 20 >= 600:
        ball_top = True

    if ball_right:
        posX_ball += speed
    else:
        posX_ball -= speed

    if ball_top:
        posY_ball -= speed
    else:
        posY_ball += speed

# когда шар отталкивается от блоков/ вылетает за пределы карты
    if paddle_b.y <= posY_ball <= paddle_b.y + 140 and paddle_b.x <= posX_ball + 15 <= 800:
        ball_right = False
    elif posX_ball - 20 > 800:
        pygame.quit()
        sys.exit()
    if paddle_a.y <= posY_ball <= paddle_a.y + 140 and paddle_a.x >= posX_ball + 15 >= 40:
        ball_right = True
    if posX_ball + 820 < 800:
        pygame.quit()
        sys.exit()

    color = (0, 0, 0)
    screen.fill(color)

    color = (255, 255, 255)
    pygame.draw.rect(screen, color, paddle_a)
    pygame.draw.rect(screen, color, paddle_b)
    pygame.draw.circle(screen, color, (posX_ball, posY_ball), 15)

    pygame.display.flip()
    clock.tick(FPS)
