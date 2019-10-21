import pygame
import random

pygame.init()   # 初始化PyGame所需的模塊
screen = pygame.display.set_mode((400, 300))    # 啟動所需大小的視窗
clock = pygame.time.Clock() # 實例Clock物件

done = False    # 作為判定是否關閉視窗使用
is_blue = True  # 作為判斷方塊顏色使用
x = 30 # 方塊位置
y = 30
cx = random.randint(0, 300) # 圓形的位置
cy = random.randint(0, 300)
score = 0   # 設定分數初始值

font = pygame.font.SysFont("comicsansms", 14)   # 設定字體樣式及大小
# (文字, 是否開啟抗鋸齒, 字體顏色)
text = font.render("Score:{}".format(score), True, (255, 255, 255))  

while not done:
     # pygame.event.get() 清空事件隊列。
     # 如果不這樣做，則視窗訊息將開始堆積，並且您的遊戲將因操作系統而變得無響應。
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:   # 點擊右上角關閉按鈕時，會觸發事件
            done = True
    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:    # 按下按鍵，並且是空格鍵
            is_blue = not is_blue
    
    pressed = pygame.key.get_pressed() # 取得所有鍵盤的狀態
    if pressed[pygame.K_UP] and y>0: y -= 4
    if pressed[pygame.K_DOWN] and y<screen.get_height()-60: y += 4
    if pressed[pygame.K_LEFT] and x>0: x -= 4
    if pressed[pygame.K_RIGHT] and x<screen.get_width()-60: x += 4

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)

    screen.fill((0, 0, 0)) # 設定螢幕顏色
    # 畫一個四方型(要畫在哪, RGB, 大小(x位置, y位置, 長度, 長度))
    player = pygame.draw.rect(screen, color, (x, y, 60, 60))
    # 畫一個圓形型(要畫在哪, RGB, (x位置, y位置), 半徑)
    food = pygame.draw.circle(screen, color, (cx, cy), 30)

    if player.colliderect(food):    # draw物件碰撞指令
        cx = random.randint(0, 300) # 重新設定food的x,y位置
        cy = random.randint(0, 300)
        score+=10   # 加分數
        text = font.render("Score:{}".format(score), True, (255, 255, 255))

    
    screen.blit(text, (0, 0))   #   顯示文字在螢幕上(文字, 位置(x, y)))

    pygame.display.flip()   # 更新螢幕顯示畫面
    clock.tick(60)  # 幀數設為60