import pygame
pygame.mixer.init()
win_width = 1200
win_height = 700
FPS = pygame.time.Clock()
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Лабіринт")

class Settings(): #Клас налаштувань
    def __init__(self, image, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(image)
        self.image = pygam.transform.scale(self.image, (self.rect.width, self.rect.height))
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    
    
class Player(Settings):
    def __init__(self, image, x, y, w, h, s):
        super().__init__(image, x, y, w, h)
        self.speed = s
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.no_flip_image = self.image
        self.flip = True
        
    def move1(self):
        if self.flip:
            self.image = self.no_flip_image
        else:
            self.image = self.flipped_image
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[pygame._DOWN] and self.rect.y < win_height-self.rect.height:
            self.rect.y += self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_width-self.rect.width:
            self.flip = True
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x>0:
            self.flip = False
            self.rect.x -= self.speed  
            
class Enemy(Player):
    def __init__(self, image, x, y, w, h, s):
        super().__init__(image, x, y, w, h, s)
        self.direction = True  #Напрямок руху (Вправо)
    def move2(self, x1, x2):
        if self.rect.x < x1:
            self.direction = True
        eli self.rect.x > x2:
            self.direction = False
        
        if self.direction
            self.image = self.no_flip_image
            self.rect.x += self.speed
        else:
            self.image = self.flipped_image
            self.rect.x -= self.speed





back = Settings("BackFon.jpg", 0,0, win_widt, win_height)
p1 = Player("Ghosty.png", 0, win_height//2, 100, 100, 5)
enemy = Enemy("enemy.png", win_width//1.7, win_height//2, win_width//8, win_width//8, 4)
gold = Settings("gold.png", win_width-150, win_height-150, 100, 100)
game = False



pygame.mixer.music.load("FonMus.mp3")
pygame.mixer.music.play()



while game:
    for event in pygame.event.ge():
        if event.type == pygame.QUIT:
            game = False
    
    back.draw()
    p1.move1()
    p1.draw()
    enemy.move(win_width//1.7, win_width-enemy.rect.width)
    enemy.draw()
    gold.daw()
    pygame.display.flip()
    FPS.tick(40)