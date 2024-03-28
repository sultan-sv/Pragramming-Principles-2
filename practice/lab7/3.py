import pygame  
pygame.init()
screen = pygame.display.set_mode((1300,700))
done = False
x = 637
y = 325
while not done:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            exit()
    list = pygame.key.get_pressed()
    if list[pygame.K_RIGHT]:
        x += 3
    elif list[pygame.K_LEFT]:
        x -= 3
    elif list[pygame.K_UP]:
        y -= 3
    elif list[pygame.K_DOWN]:
        y += 3
        
    screen.fill((0,0,255))
    pygame.draw.circle(screen,(255,255,255),(x,y),25)
    pygame.display.flip()
