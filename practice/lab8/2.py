import pygame
import random,time

pygame.init()

fps = 10
width = 800
height = 800
snake_block = 40
speed = 40
clock = pygame.time.Clock()
x = [i for i in range(761) if i % 40 == 0]
sc = pygame.display.set_mode((width, height))
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((snake_block, snake_block))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(random.choice(x) + 20, random.choice(x) + 20))
        self.tupl = (-speed, 0)
        self.body_segments = [self.rect.copy()]

    def move(self, key_event):
        if key_event.key == pygame.K_UP and self.tupl != (0, speed):
            self.tupl = (0, -speed)
        elif key_event.key == pygame.K_DOWN and self.tupl != (0, -speed):
            self.tupl = (0, speed)
        elif key_event.key == pygame.K_RIGHT and self.tupl != (-speed, 0):
            self.tupl = (speed, 0)
        elif key_event.key == pygame.K_LEFT and self.tupl != (speed, 0):
            self.tupl = (-speed, 0)

    def update(self):
            self.rect.move_ip(self.tupl)
            if self.rect.collidelist(self.body_segments[1:]) != -1:
                pygame.quit()
                exit()
            self.body_segments.insert(0, self.rect.copy())
            if len(self.body_segments) > 1:
                self.body_segments.pop()
    def resize(self):
        for i in range(random.randint(1,3)):
            self.body_segments.append(self.body_segments[-1])

    def draw_body(self, surface):
        for segment in self.body_segments:
            surface.blit(self.image, segment)

    def bound(self):
        if self.rect.top > height:
            self.rect.top = -40
        if self.rect.bottom < 0:
            self.rect.bottom = height + 40
        if self.rect.left > width:
            self.rect.left = -40
        if self.rect.right < 0:
            self.rect.right = width + 40


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((snake_block, snake_block))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(random.choice(x) + 20, random.choice(x) + 20))
P = Snake()
A = Apple()
apple_group = pygame.sprite.Group(A)
snake_group = pygame.sprite.Group(P)
collided = False
run = True
seconds = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            P.move(event)

    sc.fill('black')
    if pygame.sprite.spritecollide(P, apple_group, True):
        A = Apple()
        apple_group.add(A)
        P.resize()
        collided = True
        seconds = 0
    apple_group.draw(sc)
    P.draw_body(sc)
    snake_group.draw(sc)
    seconds += 1/fps
    if collided:
        if seconds > 10:
            A.kill()
            if seconds > 13:
                collided = False
                A = Apple()
                apple_group.add(A)
                seconds = 0
    P.bound()
    snake_group.update()

    pygame.display.update()
    clock.tick(fps)
