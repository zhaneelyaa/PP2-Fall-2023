import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))

ball_radius = 25
ball_pos = [screen_width // 2, screen_height // 2]
ball_speed = 20
ball_color = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] = max(ball_pos[1] - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_pos[1] = min(ball_pos[1] + ball_speed, screen_height - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_pos[0] = max(ball_pos[0] - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] = min(ball_pos[0] + ball_speed, screen_width - ball_radius)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.flip()

pygame.quit()
