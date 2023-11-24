import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

background = pygame.transform.scale(pygame.image.load("main-clock.png"), (width, height))
minutes_hand_image = pygame.transform.scale(pygame.image.load("left-hand.png"), (250, 100))
seconds_hand_image = pygame.transform.scale(pygame.image.load("right-hand.png"), (250, 100))

def draw_hands(minutes_angle, seconds_angle):
    minutes_hand_rotated = pygame.transform.rotate(minutes_hand_image, minutes_angle)
    seconds_hand_rotated = pygame.transform.rotate(seconds_hand_image, seconds_angle)

    minutes_rect = minutes_hand_rotated.get_rect(center=(width // 2, height // 2))
    seconds_rect = seconds_hand_rotated.get_rect(center=(width // 2, height // 2))

    screen.blit(background, (0, 0))
    screen.blit(minutes_hand_rotated, minutes_rect)
    screen.blit(seconds_hand_rotated, seconds_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.now().time()
    minutes = current_time.minute
    seconds = current_time.second

    minutes_angle = -(minutes * 6)
    seconds_angle = -(seconds * 6)

    screen.fill((255, 255, 255))
    draw_hands(minutes_angle, seconds_angle)

    pygame.display.flip()

    pygame.time.Clock().tick(1)
