import pygame
from random import randrange

SCREEN_SIZE = 600
SNAKE_SIZE = 25

pygame.init()
screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
pygame.display.set_caption('змейка')
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 16, bold=True)
font_end = pygame.font.SysFont('Arial', 36, bold=True)

x, y = randrange(0, SCREEN_SIZE - SNAKE_SIZE, SNAKE_SIZE), randrange(0, SCREEN_SIZE - SNAKE_SIZE, SNAKE_SIZE)
apple = randrange(0, SCREEN_SIZE - SNAKE_SIZE, SNAKE_SIZE), randrange(0, SCREEN_SIZE - SNAKE_SIZE, SNAKE_SIZE)
snake_length = 1
snake = [(x, y)]
dx, dy = 0, 0
snake_speed = 10
score = 0

while True:
    screen.fill('black')

    # отображаем змейку и яблоко
    for x, y in snake:
        pygame.draw.rect(screen, 'green', (x, y, SNAKE_SIZE - 2, SNAKE_SIZE - 2))
    pygame.draw.rect(screen, 'red', (*apple, SNAKE_SIZE, SNAKE_SIZE))

    # отображение счета
    render_score = font_score.render(f'SCORE: {score}', 1, 'orange')
    screen.blit(render_score, (5, 5))

    # передвижение змейки
    x += dx * SNAKE_SIZE
    y += dy * SNAKE_SIZE
    snake.append((x, y))
    snake = snake[-snake_length:]

    # поедание яблока
    if snake[-1] == apple:
        apple = randrange(0, SCREEN_SIZE - SNAKE_SIZE, SNAKE_SIZE), randrange(0, SCREEN_SIZE - SNAKE_SIZE, SNAKE_SIZE)
        snake_length += 1
        snake_speed += 0.5
        score += 1

    # конец игры
    if x < 0 or x > SCREEN_SIZE - SNAKE_SIZE or y < 0 or y > SCREEN_SIZE - SNAKE_SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, 'orange')
            screen.blit(render_end, (190, 270))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    # управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dx, dy = 0, -1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dx, dy = 0, 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx, dy = -1, 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx, dy = 1, 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
    clock.tick(snake_speed)
