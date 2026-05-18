
from pygame import *
import time as tm
from random import random,randint
font.init()
clock = time.Clock()
window = display.set_mode((700, 500))
f1 = font.Font(None, 70)
text1 = f1.render('qweqwe', True, (123,123,123))
window.blit(text1, (100,100))
class GameSprite(sprite.Sprite):
    def __init__(self,img,player_x,player_y,player_speed=1,w=65,h=65,):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))    
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self, aboba):
        return sprite.collide_rect(self, aboba)
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 450:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect > 450:
            self.rect.y += self.speed
brbrbr = GameSprite("1.png", 0, 200,5)
a = GameSprite("2.png", 450, 200, 5)
Brag = GameSprite("3.png", 300, 200, 5)

game = True
finish = True
start = tm.time()
while game:
    if finish:
        window.fill((12,55,221))
    for e in event.get():
        if e.type == QUIT:
            game = False
#    keys = key.get_pressed()

  
        
        
    #if keys[K_q]:
        
        
    display.update()
    clock.tick(1488)