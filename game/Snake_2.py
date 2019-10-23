import pygame
import random
import time  

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

global player_x, player_y, food_x, food_y, food, score, temp_x, temp_y, font, text, die
done = False
die = False
SPEED = 25
score = 0
direction = 'x+'

player_x, player_y = 0, 0
temp_x, temp_y = 0, 0
player_SIZE = 25   
player_position_ls = [[0, 0]]

food_SIZE = 25
food_x = random.randint(0, SCREEN_WIDTH-food_SIZE)
food_y = random.randint(0, SCREEN_HEIGHT-food_SIZE)
food = pygame.draw.rect(screen, (100, 128, 255), (food_x, food_y, food_SIZE, food_SIZE))

font = pygame.font.SysFont("comicsansms", 14)
text = font.render("Score:{}".format(score), True, (255, 255, 255))

def move_player():
    global player_x, player_y, temp_x, temp_y
    temp_x = player_x
    temp_y = player_y
    
    if direction == 'x+':
        player_x += SPEED
    elif direction == 'x-':
        player_x -= SPEED
    elif direction == 'y+':
        player_y += SPEED
    elif direction == 'y-':
        player_y -= SPEED

    player_position_ls.pop(0)
    player_position_ls.append([player_x, player_y ])

def set_player():     
    for i in player_position_ls:  
        pygame.draw.rect(screen, (0, 128, 255), (i[0], i[1], player_SIZE, player_SIZE))

def check_overlapping():
    global food
    player = pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_SIZE, player_SIZE)) 
    if player.colliderect(food):
        return True
    else:
        return False

def change_food_position(): 
    global food_x, food_y,food 
    while check_overlapping():
        food_x = random.randint(0, SCREEN_WIDTH-food_SIZE)
        food_y = random.randint(0, SCREEN_HEIGHT-food_SIZE)
        food = pygame.draw.rect(screen, (100, 128, 255), (food_x, food_y, food_SIZE, food_SIZE))

def collide():
    global food, score, player_position_ls, temp_x, temp_y, text
    player = pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_SIZE, player_SIZE)) 
    if player.colliderect(food):    # draw物件碰撞指令
        change_food_position()
        player_position_ls.insert(0,[temp_x, temp_y])
        score+=10   # 加分數
        text = font.render("Score:{}".format(score), True, (255, 255, 255))  

def check_die():
    global die, player_position_ls
    if player_x > SCREEN_WIDTH-player_SIZE:
        die = True
    elif player_x < 0:
        die = True
    elif player_y > SCREEN_HEIGHT-player_SIZE:
        die = True
    elif player_y < 0:
        die = True
        
    if player_position_ls.count([player_x, player_y]) == 2:
        # print([player_x, player_y])
        die = True

while not done:
    while die:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                die = False
                score = 0
                direction = 'x+'

                player_x, player_y = 0, 0
                temp_x, temp_y = 0, 0
                player_position_ls = [[0, 0]]

                food_x = random.randint(0, SCREEN_WIDTH-food_SIZE)
                food_y = random.randint(0, SCREEN_HEIGHT-food_SIZE)
                food = pygame.draw.rect(screen, (100, 128, 255), (food_x, food_y, food_SIZE, food_SIZE))


    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 點擊右上角關閉按鈕時，會觸發事件
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and player_y>=0 and direction != 'y+':
            direction = 'y-'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and player_y<SCREEN_HEIGHT-player_SIZE  and direction != 'y-':
            direction = 'y+'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and player_x>=0 and direction != 'x+':
            direction = 'x-'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and player_x<SCREEN_WIDTH-player_SIZE and direction != 'x-':
            direction = 'x+'
    
    move_player()
    
    collide()

    check_die()
    set_player()
    food = pygame.draw.rect(screen, (100, 128, 255), (food_x, food_y, food_SIZE, food_SIZE))

    
    
    screen.blit(text, (0, 0))   #   顯示文字在螢幕上(文字, 位置(x, y)))
    clock.tick(60)
    pygame.display.flip()
    time.sleep(0.25)