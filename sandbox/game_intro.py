import pygame
from random import randint
 
pygame.init()
 
# Set up the drawing window
screen = pygame.display.set_mode([800, 500])
                               
# pygame clock object controls tick rate
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
p1: pygame.Rect = pygame.Rect(20, 150, 50, 50)
p2: pygame.Rect = pygame.Rect(500, 150, 50, 50)
coins: list[pygame.Rect] = [pygame.Rect(420, 60, 50, 50), pygame.Rect(200, 120, 50, 50)]

while running:
    clock.tick(60)
 
    # Fill background
    screen.fill((120, 200, 255))
 
    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), p1)
    pygame.draw.rect(screen, (150, 10, 245), p2)

    # move the rectangle
    p1.x = pygame.mouse.get_pos()[0] - 25
    p1.y = pygame.mouse.get_pos()[1] - 25

    # draw coins and do collisions
    for coin in coins:
        pygame.draw.circle(screen, (235, 162, 52), (coin.centerx, coin.centery), 15)
        hit = coin.colliderect(p1)
        if hit:
            coins.remove(coin)

    # Checks every frame for any user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                coins.append(pygame.Rect(randint(0, 800), randint(0, 500), 25, 25))
   
    pygame.display.flip()
 
# Done! Time to quit.
pygame.quit()