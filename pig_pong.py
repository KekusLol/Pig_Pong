from pygame import *
from random import randint
from time import time as timer
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = self.speed
        self.speed_y = int(self.speed/2)
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_s] and self.rect.y<600:
            self.rect.y+=self.speed
class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_DOWN] and self.rect.y<600:
            self.rect.y+=self.speed
class Ball(GameSprite):
    def update(self):
        global ball
        global reket1
        global reket2
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y > 659:
            self.speed_y*=-1
        if sprite.collide_rect(ball, reket1) or sprite.collide_rect(ball, reket2):
            self.speed_x*=-1
        if self.rect.x<1 or self.rect.x > 1279:
            self.rect.x = 615
            self.rect.y = 335
#Игровая сцена:
bg= randint(0,255), randint(0,255), randint(0,255)
window = display.set_mode((1280, 720))
display.set_caption("PigPong")
window.fill(bg)

#переменные
lost = 0
score = 0
finish = False
run = True
clock = time.Clock()
ball_image = 'ball.png'
#создание спрайтов
reket1 = Player1('rocket.png', 15, 150, 5, 250, 5)
reket2 = Player2('rocket.png', 15, 150, 1260, 250, 5)
ball = Ball(ball_image, 50, 50, 615, 335, 8) 
#музыка
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#shot = mixer.Sound('fire.ogg')
#шрифты
font.init()
player1_score = font.SysFont('Arial', 70).render('0', 1, (255,0,255))
player2_score = font.SysFont('Arial', 70).render('0', 1, (255,0,255))
win = font.SysFont('Arial', 70).render('YOU WIN', 1, (0,255,0))
lose = font.SysFont('Arial', 70).render('GAME OVER', 1, (255,0,0))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(bg)
    window.blit(player1_score,(15,5))
    window.blit(player1_score,(1180,5))
    if not(finish):
        reket1.reset()
        reket1.update()
        reket2.reset()
        reket2.update()
        ball.update()
        ball.reset()
    display.update()
    clock.tick(60)