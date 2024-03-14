import pygame

FPS = pygame.time.Clock()
win_width = 1200
win_height = 620
p_size = 40


window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Лабіринт")

class Settings():
    def __init__(self, image, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Settings):
    def __init__(self, image, x, y, w, h, s):
        super().__init__(image, x, y, w, h)
        self.speed = s
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.no_flip_image = self.image
        self.flip = True

    def move(self):
        if self.flip:
            self.image = self.no_flip_image
        else:
            self.image = self.flipped_image
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y<win_height-self.rect.height:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x>0:
            self.rect.x -= self.speed
            self.flip = False
        if keys[pygame.K_RIGHT] and self.rect.x<win_width-self.rect.width:
            self.rect.x += self.speed 
            self.flip = True




class Enemy(Player):
    def __init__(self, image, x, y, w, h, s):
        super().__init__(image, x, y, w, h, s)
        self.direction = True #right

    def move(self, x1, x2):
        if self.rect.x<x1:
            self.direction = True
        elif self.rect.x>x2:
            self.direction = False

        if self.direction:
            self.image = self.no_flip_image
            self.rect.x += self.speed
        else:
            self.image = self.flipped_image
            self.rect.x -= self.speed

class Wall:
    def __init__ (self, x,y,w,h, color):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
    def draw(self):
        pygame.draw.rect(window ,self.color, self.rect)
        
        
        

color = (255, 255, 0)
bg = Settings("BackFon.jpg", 0, 0, win_width, win_height)
p1 = Player("Ghosty.png", 0, win_height//2, p_size, p_size, 5)
enemy = Enemy("enemy.png", win_width//1.3, win_height//2.3, p_size*1.5, p_size*1.5, 2)
gold = Settings("gold.png", win_width//1.15, win_height//1.5, p_size, p_size)
walls = [
    Wall(70, 10 , win_width-140, 3, color),
    Wall(70, win_height-10 , win_width-140, 3, color),
    Wall(70, 80 , 3, win_height-90, color),
    Wall(win_width-70, 10 , 3, win_height-17, color),
    

]    

game = True
finish = False

pygame.mixer.init()
pygame.mixer.music.load("FonMusik.mp3")
pygame.mixer.music.play()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if finish != True:
        bg.draw()
        for w in walls:
            if p1.rect.colliderect(w.rect):
                finish = True
            w.draw()
        p1.move()
        p1.draw()

        enemy.move(win_width//1.3, win_width//1.12)
        enemy.draw()
        gold.draw()
    pygame.display.flip()
    FPS.tick(40)