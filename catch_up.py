import pygame

win_width = 700
win_height = 500
FPS = pygame.time.Clock()
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Доганялки")

class Settings(): #Клас налаштувань
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
        
    def move1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height-self.rect.height:
            self.rect.y += self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_width-self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x>0:
            self.rect.x -= self.speed  
        
            
    
                    

back = Settings("background.png", 0,0, win_width, win_height)
p1 = Player("sprite1.png", 0, win_height//2, 100, 100, 5)
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    back.draw()
    p1.move1()
    p1.draw()
    pygame.display.flip()
    FPS.tick(40)