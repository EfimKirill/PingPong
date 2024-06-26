from pygame import *


WIN_WIDTH = 700
WIN_HEIGHT = 500
FPS = 40

class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.x -= self.speed
        elif keys[K_DOWN] and self.rect.y <= 495:
            self.rect.x += self.speed
    
class Player2(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.x -= self.speed
        elif keys[K_s] and self.rect.y <= 495:
            self.rect.x += self.speed

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption('PingPong')

clock = time.Clock()

background =  transform.scale(image.load("77-Tennis-Courts-Doubles.jpg"), (700, 500))

game = True
finish = False

player1 = Player1('racket.png', 5, WIN_HEIGHT - 100, 80, 100, 10)
player2 = Player2('racket.png', 5, WIN_HEIGHT - 100, 80, 100, 10)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))

        Player1.reset()
        Player1.update()
        Player2.reset()
        Player2.update()

    display.update()
    clock.tick(FPS)
