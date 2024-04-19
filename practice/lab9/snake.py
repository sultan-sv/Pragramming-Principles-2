import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up variables
fps = 10
width = 800
height = 800
snake_block = 40
speed = 40
clock = pygame.time.Clock()
x = [i for i in range(761) if i % 40 == 0]
sc = pygame.display.set_mode((width, height))
level = 0
text_font = pygame.font.SysFont('arial', 20)
level_font = pygame.font.SysFont('arial', 20)
score = 0
lib = {0: "black", 1: "yellow", 2: "cyan", 3: 'green', 4: 'violet', 5: 'blue'}

# Snake class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((snake_block, snake_block))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(random.choice(x) + 20, random.choice(x) + 20))
        self.tupl = (-speed, 0)  # Initial movement direction
        self.body_segments = [self.rect.copy()]  # List to store body segments of the snake

    def move(self, key_event):
        # Change direction based on key press
        if key_event.key == pygame.K_UP and self.tupl != (0, speed):
            self.tupl = (0, -speed)
        elif key_event.key == pygame.K_DOWN and self.tupl != (0, -speed):
            self.tupl = (0, speed)
        elif key_event.key == pygame.K_RIGHT and self.tupl != (-speed, 0):
            self.tupl = (speed, 0)
        elif key_event.key == pygame.K_LEFT and self.tupl != (speed, 0):
            self.tupl = (-speed, 0)

    def update(self):
        # Move the snake
        self.rect.move_ip(self.tupl)
        
        # Check for collision with itself
        if self.rect.collidelist(self.body_segments[1:]) != -1:
            pygame.quit()
            exit()
        
        # Insert new head position
        self.body_segments.insert(0, self.rect.copy())
        
        # Remove last segment to maintain size
        if len(self.body_segments) > 1:
            self.body_segments.pop()

    def resize(self):
        # Increase snake length randomly
        y = random.randint(1, 3)
        for i in range(y):
            self.body_segments.append(self.body_segments[-1])

    def draw_body(self, surface):
        # Draw each body segment
        for i in range(len(self.body_segments)):
            self.image.fill('white')
            surface.blit(self.image, self.body_segments[i])

    def bound(self):
        # Wrap around the screen if out of bounds
        if self.rect.top > height:
            self.rect.top = -40
        if self.rect.bottom < 0:
            self.rect.bottom = height + 40
        if self.rect.left > width:
            self.rect.left = -40
        if self.rect.right < 0:
            self.rect.right = width + 40


# Apple class
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((snake_block, snake_block))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(random.choice(x) + 20, random.choice(x) + 20))

# Create snake and apple instances
P = Snake()
A = Apple()
apple_group = pygame.sprite.Group(A)
snake_group = pygame.sprite.Group(P)
collided = False
run = True
seconds = 0

# Main game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            P.move(event)

    # Fill screen with background color based on level
    sc.fill(lib[level])
    
    # Check collision with apple
    if pygame.sprite.spritecollide(P, apple_group, True):
        # Generate new apple, increase snake length, update score and level
        A = Apple()
        apple_group.add(A)
        P.resize()
        collided = True
        seconds = 0
        score = len(P.body_segments)
        level = score // 5
    
    # Draw apple, snake, and display score and level
    apple_group.draw(sc)
    P.draw_body(sc)
    snake_group.draw(sc)
    text = text_font.render('score = ' + str(score), True, 'red')
    lev = level_font.render('level = ' + str(level), True, "red")
    sc.blit(text, (20, 20))
    sc.blit(lev, (20, 40))
    
    # Update snake movement and display
    snake_group.update()
    pygame.display.update()
    clock.tick(fps)

    # Handle apple disappearance and respawn after certain time
    if collided:
        if seconds > 10:
            A.kill()
            if seconds > 13:
                collided = False
                A = Apple()
                apple_group.add(A)
                seconds = 0
    # Handle snake boundaries
    P.bound()
