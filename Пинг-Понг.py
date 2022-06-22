from pygame import *
from random import *
from time import time as timer
window = display.set_mode((700, 500))
font.init()
lost = 0
font1 = font.SysFont(None, 80)
win = font1.render('You win!', True, (255, 255, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, wight, height, player_speed):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
       keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):
       keys = key.get_pressed()
        if keys[K_w] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
win_height = 500
win_width = 700       
FPS = 60
racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png.png', 200, 200, 4, 50, 50)
display.set_caption('')
display.update()
    clock.tick(FPS)



