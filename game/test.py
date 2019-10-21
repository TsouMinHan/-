import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400, 300)) 
clock = pygame.time.Clock()
x = 30
y = 30
cx = random.randint(0, 300)
cy = random.randint(0, 300)
is_blue = True
done = False
score = 0
# =========HERE==========
font = pygame.font.SysFont("comicsansms", 14)  
text = font.render("Score:{}".format(score), True, (255, 255, 255))  

while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
  
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>0: y -= 4
    if pressed[pygame.K_DOWN] and y<screen.get_height()-60: y += 4
    if pressed[pygame.K_LEFT] and x>0: x -= 4
    if pressed[pygame.K_RIGHT] and x<screen.get_width()-60: x += 4

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    
    screen.fill((0, 0, 0))  
# =========HERE==========    
    player = pygame.draw.rect(screen, color, (x, y, 60, 60))
    food = pygame.draw.circle(screen, color, (cx, cy), 30)

    if player.colliderect(food):
        cx = random.randint(0, 300)
        cy = random.randint(0, 300)
        score+=10
# =========HERE==========
        text = font.render("Score:{}".format(score), True, (255, 255, 255))


# =========HERE==========
    screen.blit(text, (0, 0))
    pygame.display.flip()     
    clock.tick(60)