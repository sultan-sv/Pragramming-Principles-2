import pygame 
import random
import time
pygame.init()
width = 700
height = 600
score = 0
text_font = pygame.font.SysFont('arial',30)
text_font2 = pygame.font.SysFont('arial',90)
sc = pygame.display.set_mode((width,height))
background = pygame.image.load(r"C:\Users\User\Downloads\PygameTutorial_3_0\AnimatedStreet.png")
background = pygame.transform.scale(background,(700,600))
car_width = 50
car_height = 100
clock = pygame.time.Clock()
fps = 60
speed = [7,8,9,9,8.5]
speed_player = 10
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((car_width,car_height))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = (random.randint(car_width//2,width - car_width//2),height-car_height-25))
    def move(self):
        press = pygame.key.get_pressed()
        if self.rect.left > 0:
              if press[pygame.K_LEFT]:
                  self.rect.move_ip(-speed_player, 0)
        if self.rect.right < width:        
              if press[pygame.K_RIGHT]:
                  self.rect.move_ip(speed_player, 0)
class opponent(pygame.sprite.Sprite):
    def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface((car_width,car_height))
          self.image.fill(('red'))
          self.rect = self.image.get_rect(center = (random.randint(car_width//2,width - car_width//2),-100))
    def move(self):
         if self.rect.top <= height :
              self.rect.move_ip(0,random.choice(speed))
         if self.rect.top >= height:
              self.rect.bottom = 0
              self.rect = self.image.get_rect(center = (random.randint(car_width//2,width - car_width//2),-100))
class coin(pygame.sprite.Sprite):
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface((25,25))
          self.image.fill('gold')
          self.rect = self.image.get_rect(center = (random.randint(25,width - 25),0))
     def move(self):
          self.rect.move_ip(0,6)
          if self.rect.top > height:
               self.rect.top = 0
               self.rect = self.image.get_rect(center = (random.randint(25,width - 25),0))
P = player()
O = opponent()
O2 = opponent()
O3 = opponent()
C = coin()
opponents = pygame.sprite.Group()
opponents.add(O) 
opponents.add(O2)
opponents.add(O3)
sprites = pygame.sprite.Group()
sprites.add(P)
sprites.add(O)
sprites.add(O2)
sprites.add(O3)
sprites.add(C)
coins = pygame.sprite.Group()
coins.add(C)
while 1:
    clock.tick(fps)
    sc.blit(background,(0,0))
    text = text_font.render('score = '+str(score),True,'gold')
    sc.blit(text,(20,10))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()                
    for i in sprites:                           
         i.move()
         sc.blit(i.image,i.rect)
    if pygame.sprite.spritecollideany(P,opponents):
         time.sleep(1)
         sc.fill('red')
         text2 = text_font2.render('game over',True,'black')
         sc.blit(text2,(width//2-180,height//2-45))
         pygame.display.update()
         time.sleep(2)
         exit()
    if pygame.sprite.collide_rect(P,C):
        C.kill()
        score = score + random.randint(1,4)
        C = coin()
        sprites.add(C)
    for i in speed:
          i = i +score//5
    pygame.display.update()




