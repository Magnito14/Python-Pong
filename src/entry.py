import pygame # Where all the magic happens...
from sys import exit
from ball import Ball
from paddle import Paddle

pygame.init()
programIcon = pygame.image.load("data/res/gfx/ico.png")
pygame.display.set_icon(programIcon)
pygame.display.set_caption("Pong in Pygame")

WIDTH, HEIGHT = 600, 450
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
BALL_RADIUS = 8

def draw(win, paddles, ball, left_score, right_score):
    font = pygame.font.Font('data/res/font/font.otf', 75)
    left_score_text = font.render(f"{left_score}", 1, WHITE)
    right_score_text = font.render(f"{right_score}", 1, WHITE)

    win.fill(BLACK)
    win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width() // 2, 20))

    for paddle in paddles:
        paddle.draw_paddle(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 3, i, 6, HEIGHT//20))

    ball.draw_ball(win)
    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move_paddle(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move_paddle(up=False)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move_paddle(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move_paddle(up=False)

def handle_collision(ball, left_paddle, right_paddle):
    collidefx = pygame.mixer.Sound("data/res/sfx/collide.wav")
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1
                pygame.mixer.Sound.play(collidefx)
    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1
                pygame.mixer.Sound.play(collidefx)

def main():
    clock = pygame.time.Clock()
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
    left_score = 0
    right_score = 0
    losefx = pygame.mixer.Sound("data/res/sfx/lose.wav")

    while True:
        clock.tick(64)
        draw(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()     
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball.move_ball()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset_ball()
            pygame.mixer.Sound.play(losefx)
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset_ball()
            pygame.mixer.Sound.play(losefx)

    pygame.quit()

if __name__ == "__main__":
    main()