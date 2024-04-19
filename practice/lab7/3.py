import pygame  
pygame.init()
screen = pygame.display.set_mode((1300,700))
clock = pygame.time.Clock()
fps = 60
done = False
x = 637
y = 325
while not done:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            exit()
    list = pygame.key.get_pressed()
    if y >= 30:
        if list[pygame.K_UP]:
            y -= 10
    if y <= 665:
        if list[pygame.K_DOWN]:
            y += 10
    if x <= 1275:
        if list[pygame.K_RIGHT]:
            x += 10
    if x >= 25:
        if list[pygame.K_LEFT]:
            x -= 10
    
    screen.fill((0,0,255))
    pygame.draw.circle(screen,(255,255,255),(x,y),25)
    pygame.display.flip()
