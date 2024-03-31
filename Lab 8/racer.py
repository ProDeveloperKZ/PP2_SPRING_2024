
#Imports
import pygame, sys
from pygame.locals import *
import random, time

from pygame.sprite import Group

pygame.init()
 
#Setting up FPS 
fps = 120
timer = pygame.time.Clock()
 
#Creating colors and variables
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
width = 400
height = 600
SPEED = 2.5
SCORE = 0
COINS = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("street.png")

pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
 
#Create a white screen 
screen = pygame.display.set_mode((400,600))
screen.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("delorian.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if (pressed_keys[K_UP] or pressed_keys[K_w]) and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if (pressed_keys[K_DOWN] or pressed_keys[K_s]) and self.rect.bottom < height:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), random.randint(40, height-40))

    def update(self):
        global COINS
        if pygame.sprite.collide_rect(self, P1):  # Check for collision with player
            COINS += 1  # Increase coin count
            self.rect.center = (random.randint(40, width-40), random.randint(40, height-40))
            pygame.mixer.Sound("coin_collect.mp3").play()

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.25     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    screen.blit(background, (0,0))
    scores_car = font_small.render("Cars: " + str(SCORE), True, BLACK)
    scores_coin = font_small.render("Coins: " + str(COINS), True, BLACK)
    screen.blit(scores_car, (10,10))
    screen.blit(scores_coin, (300,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    for entity in coins:
        screen.blit(entity.image, entity.rect)
        entity.update()
    #To be run if collision occurs between player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound("crash.wav").play()
          time.sleep(0.5)
                    
          screen.fill(RED)
          screen.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit() 
         
    pygame.display.update()
    timer.tick(fps)