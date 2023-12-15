import random
import time
import pygame

clock = pygame.time.Clock()
fps = 60  

COINS_DICTIONARY = {'1': 'coin_1.png', '2': 'coin_2.png'}

RED = (255, 0, 0)  # colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SPEED = 6  
SCORE = 0

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 393, 600 
pygame.init()  
screen = pygame.display.set_mode(WINDOW_SIZE) 

font = pygame.font.SysFont('Verdana', 63)  
font_small = pygame.font.SysFont('Verdana', 18)  
game_over_text_label = font.render('Game over!', True, WHITE) 
background = pygame.image.load('street.png')
pygame.mixer.init() 
pygame.mixer.music.set_volume(0.45)  
pygame.mixer.music.load('background.wav')  
pygame.mixer.music.play(loops=10 ** 9) 

pygame.display.set_caption('GAME')  

game_over = False  

class Coin(pygame.sprite.Sprite):
    
    def __init__(self, _image_name: str, _points=1):
        super().__init__()
        self.image = coin_1.jpeg (_image_name)  
        self.rect = self.image.get_rect() 
        self.radius = self.rect.width//2  
        self.set_random_position()  
        self.points = _points

    def move(self):
        self.rect.move_ip(0, 3) 
        if self.rect.top > WINDOW_HEIGHT: 
            self.set_random_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)  

    def set_random_position(self):
        self.rect.center = (random.randint(40+self.radius, WINDOW_WIDTH-40-self.radius), 0)
        self.rect.bottom = 0  

class Enemy(pygame.sprite.Sprite):
  
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')  
        self.rect = self.image.get_rect() 
        self.set_random_position()

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)  

        if self.rect.top > WINDOW_HEIGHT:  
            SCORE += 1 
            self.set_random_position()

    def set_random_position(self):
        self.rect.center = (random.randint(64, WINDOW_WIDTH - 64), 0)
        self.rect.bottom = 0  

    def draw(self, surface):
        surface.blit(self.image, self.rect)  

class Player(pygame.sprite.Sprite):  
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')  
        self.rect = self.image.get_rect() 
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)  
    def move(self):
        pressed_keys = pygame.key.get_pressed()  

        if self.rect.left > 43:  
            if pressed_keys[pygame.K_LEFT]:  
                self.rect.move_ip(-5, 0)
        if self.rect.right < WINDOW_WIDTH - 43:
            if pressed_keys[pygame.K_RIGHT]:  
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  


player = Player()  
enemy = Enemy() 
coin_1 = Coin(COINS_DICTIONARY['1'])  
coin_2 = None

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin_1)

enemies = pygame.sprite.Group()  
enemies.add(enemy)

coins = pygame.sprite.Group()  
coins.add(coin_1)

super_coin_group = pygame.sprite.Group()

simple_coins = 0 
super_coins = 0
is_super_coin_generated = False
is_speed_increased = False


def generate_coin(type=1):
    global coin_1, coin_2
    if type == 1:
        coin_1 = Coin(COINS_DICTIONARY['1'])
        coins.add(coin_1)
        all_sprites.add(coin_1)
    else:
        coin_2 = Coin(COINS_DICTIONARY['2'])
        super_coin_group.add(coin_2)
        all_sprites.add(coin_2)


while not game_over: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            game_over = True

    screen.blit(background, (0, 0)) 

    screen.blit(
        font_small.render(f'Score: {SCORE}', True, BLUE), (237, 9)
    )  

    screen.blit(
        font_small.render(f'Simple coins: {simple_coins}', True, BLUE), (237, 30)
    ) 
    screen.blit(
        font_small.render(f'Super coins: {super_coins}', True, BLUE), (237, 51)
    )  

    for sprite in all_sprites:
        sprite.move()  
        sprite.draw(screen)

    if SCORE % 12 == 0 and SCORE != 0:
        if not is_super_coin_generated:
            is_super_coin_generated = True
            generate_coin(type=2)
    elif SCORE % 12 == 1:
        is_super_coin_generated = False

    total_coins = simple_coins + super_coins

    if total_coins % 7 == 0 and total_coins != 0:
        if not is_speed_increased:
            is_speed_increased = True
            SPEED += 2
    elif total_coins % 7 == 1:
        is_speed_increased = False

    if coin_2:
        if pygame.sprite.spritecollideany(player, super_coin_group):
            coin_2.kill()
            super_coins += 1
            SCORE += 2

    if pygame.sprite.spritecollideany(player, coins):
        coin_1.kill()  
        SCORE += 1  
        simple_coins += 1 
        generate_coin() 

    if pygame.sprite.spritecollideany(player, enemies): 
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play() 
        time.sleep(1) 

        screen.fill((69, 172, 116))  
        screen.blit(game_over_text_label, (12, 190))
        screen.blit(font_small.render(f'Your score: {SCORE}', True, WHITE), (15, 270))  
        screen.blit(font_small.render(f'Simple coins: {simple_coins}', True, WHITE),
                    (15, 290))  
        screen.blit(font_small.render(f'Super coins: {super_coins}', True, WHITE),
                    (15, 311))  

        pygame.display.update() 

        for sprite in all_sprites:
            sprite.kill()  
        time.sleep(7)  

        game_over = True  
    pygame.display.update()  
    clock.tick(fps)  
pygame.quit()