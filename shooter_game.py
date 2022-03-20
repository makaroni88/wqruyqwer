from pygame import *
from random import randint
from time import sleep
lostenemy = 0
killingenemy = 0
zad_bullet = 0
zad_max_bullet = 5
score = 10
font.init()
font = font.Font(None,25)
lose = font.render('eofjkij', True, (255, 255,255))
finish = ''
asd = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,scale_x,scale_y):
        super().__init__()
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = transform.scale(image.load(player_image), (self.scale_x, self.scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def shot(self):
        keys_pressed = key.get_pressed()
        global zad_bullet
        if zad_bullet == zad_max_bullet :
            if keys_pressed[K_SPACE]:
                bullet =  Bullet('bullet.png',player.rect.x + 18,player.rect.y -10,6,20,40)
                bullets.add(bullet)
                fire.play()
                zad_bullet = 0
        else:
            zad_bullet +=1
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]and self.rect.x >5:
            self.rect.x -= self.speed
        if keys_pressed[K_d]and self.rect.x <win_x-self.scale_y:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.y <= win_y+100:
            self.rect.y += self.speed
        if self.rect.y >= 800:
            global lostenemy
            self.rect.y = -20
            self.rect.x = randint(100,win_x-100)
            lostenemy += 1
class Bullet(GameSprite):
    def update(self):
        if self.rect.y != 0:
            self.rect.y -= self.speed
win_x = 900
win_y = 700
window = display.set_mode((win_x, win_y))
display.set_caption("Maze")

#Surface
surf1 = Surface((win_x,win_y))
surf1.fill((255,255,255))

surf2 = Surface((win_x-20,win_y-20))
surf2.fill((101, 157, 187))

player = Player('aaa.png',80,625,7,65,85)
galaxy = GameSprite('xxx.jpg',0,0,0,win_x,win_y)
bullets = sprite.Group()
monsters = sprite.Group()
for i in range(9):
    enemy = Enemy('ap.png',randint(100,win_x-100),-20,randint(2,6),65,65)
    monsters.add(enemy)

mixer.init()
mixer.music.load('jjjjjjjj.ogg')
mixer.music.play()
fire = mixer.Sound('ooo.ogg')


win1 = font.render('TYGYGuysgabHUD', True, (255, 255, 255))
run = True
game = True
menu = False
clock = time.Clock()
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if game and not(menu):
        if not finish:
            if sprite.groupcollide(monsters,bullets,True,True):
                killingenemy += 1
                enemy = Enemy('ap.png',randint(100,win_x-100),-20,randint(2,6),65,65)
                monsters.add(enemy)

            keys_pressed = key.get_pressed()
            if keys_pressed[K_ESCAPE] and game == True and menu == False:
                game = False
                menu = True

            if killingenemy >= score:
                window.blit(win1, (200, 200))
                finish = True
                
            if lostenemy >= asd:
                window.blit(lose, (200, 200))
                finish = True            


            galaxy.reset()
            player.update()
            monsters.update()
            monsters.draw(window)
                                
            bullets.update()
            bullets.draw(window)

            text = font.render('werqteqert: ' + str(killingenemy), 1, (255, 255, 255))
            window.blit(text, (10, 20))


            text = font.render('ccacac' + str(lostenemy), 1, (255, 255, 255))
            window.blit(text, (10, 50))
            
            player.shot()
            player.reset()

            display.update()
            clock.tick(FPS) 