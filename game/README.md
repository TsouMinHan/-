## 作品介紹 - 吃東西
玩家操作方塊吃東西來獲得分數

## 使用套件
`pygame`
`random`

## 程式架構
* 製作玩家方塊(按鍵操作)
* 製作球體(食物)
* 分數計算

## 安裝套件
pygame
開啟 Anaconda prompt 輸入:
```bash
pip install pygame
```
py檔輸入:
```python
import pygame
```
https://pypi.org/project/pygame/

## 建立視窗
```python
import pygame

pygame.init()   # 初始化PyGame所需的模塊
screen = pygame.display.set_mode((400, 300))    # 啟動所需大小的視窗

done = False    # 作為判定是否關閉視窗使用

while not done:
     # pygame.event.get() 清空事件隊列。
     # 如果不這樣做，則視窗訊息將開始堆積，並且您的遊戲將因操作系統而變得無響應。
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:   # 點擊右上角關閉按鈕時，會觸發事件
            done = True

    pygame.display.flip()   # 更新螢幕顯示畫面
pygame.quit()  # 關閉pygame
```

## 建立方塊
```python
# 畫一個四方型(要畫在哪, RGB, 大小(x位置, y位置, 長度, 長度))
pygame.draw.rect(screen, (0, 128, 255), (30, 30, 60, 60))
```
目前程式碼:
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300)) 

done = False

while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
# =========HERE==========
    pygame.draw.rect(screen, (0, 128, 255), (30, 30, 60, 60))

    pygame.display.flip()
pygame.quit()
```

## 變更方塊顏色
按下空白鍵會換顏色
```python
is_blue = True # 作為判斷方塊顏色使用
# 按下按鍵，並且是空白鍵
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    is_blue = not is_blue

if is_blue: color = (0, 128, 255)
else: color = (255, 100, 0)

pygame.draw.rect(screen, color, (30, 30, 60, 60))
```
目前程式碼:
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300)) 
# =========HERE========== 
is_blue = True
done = False

while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
# =========HERE==========        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:    # 按下按鍵，並且是空格鍵
            is_blue = not is_blue
# =========HERE==========        
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
# =========HERE==========        
    pygame.draw.rect(screen, color, (30, 30, 60, 60))

    pygame.display.flip()
pygame.quit()
```

## 方塊移動

```python
# 方塊位置
x = 30
y = 30
pygame.draw.rect(screen, color, (x, y, 60, 60))

pressed = pygame.key.get_pressed() # 取得所有鍵盤的狀態
if pressed[pygame.K_UP]: y -= 4
if pressed[pygame.K_DOWN]: y += 4
if pressed[pygame.K_LEFT]: x -= 4
if pressed[pygame.K_RIGHT]: x += 4

screen.fill((0, 0, 0)) # 設定螢幕顏色

clock = pygame.time.Clock() # 實例Clock物件
clock.tick(60) # 幀數設為60
```
目前程式碼:
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300)) 
# =========HERE==========  
clock = pygame.time.Clock()
x = 30
y = 30
is_blue = True
done = False

while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
# =========HERE==========  
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 4
    if pressed[pygame.K_DOWN]: y += 4
    if pressed[pygame.K_LEFT]: x -= 4
    if pressed[pygame.K_RIGHT]: x += 4

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
# =========HERE==========  
    screen.fill((0, 0, 0))      
    pygame.draw.rect(screen, color, (x, y, 60, 60))

    pygame.display.flip()
# =========HERE==========        
    clock.tick(60)
pygame.quit()
```

## 設定邊界
```python
if pressed[pygame.K_UP] and y>0: y -= 4
if pressed[pygame.K_DOWN] and y<screen.get_height()-60: y += 4
if pressed[pygame.K_LEFT] and x>0: x -= 4
if pressed[pygame.K_RIGHT] and x<screen.get_width()-60: x += 4
```
目前程式碼:
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300)) 
clock = pygame.time.Clock()
x = 30
y = 30
is_blue = True
done = False

while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
# =========HERE==========  
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>0: y -= 4
    if pressed[pygame.K_DOWN] and y<screen.get_height()-60: y += 4
    if pressed[pygame.K_LEFT] and x>0: x -= 4
    if pressed[pygame.K_RIGHT] and x<screen.get_width()-60: x += 4

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    
    screen.fill((0, 0, 0))      
    pygame.draw.rect(screen, color, (x, y, 60, 60))

    pygame.display.flip()     
    clock.tick(60)
pygame.quit()
```

## 建立圓形
```python
import random
cx = random.randint(0, 300) # 圓形的位置
cy = random.randint(0, 300)
# 畫一個圓形型(要畫在哪, RGB, (x位置, y位置), 半徑)
pygame.draw.circle(screen, color, (cx, cy), 30)
```
目前程式碼:
```python
import pygame
# =========HERE==========
import random
pygame.init()
screen = pygame.display.set_mode((400, 300)) 
clock = pygame.time.Clock()
x = 30
y = 30
# =========HERE==========
cx = random.randint(0, 300)
cy = random.randint(0, 300)
is_blue = True
done = False

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
    pygame.draw.rect(screen, color, (x, y, 60, 60))
# =========HERE==========
    pygame.draw.circle(screen, color, (cx, cy), 30)

    pygame.display.flip()     
    clock.tick(60)
pygame.quit()
```

## 碰撞偵測
```python
score = 0   # 設定分數初始值
player = pygame.draw.rect(screen, color, (x, y, 60, 60))
food = pygame.draw.circle(screen, color, (cx, cy), 30)

if player.colliderect(food):    # draw物件碰撞指令
    cx = random.randint(0, 300) # 重新設定food的x,y位置
    cy = random.randint(0, 300)
```
目前程式碼:
```python
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
# =========HERE==========
score = 0

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
# =========HERE==========
    if player.colliderect(food):
        cx = random.randint(0, 300)
        cy = random.randint(0, 300)
        score+=10

    pygame.display.flip()     
    clock.tick(60)
pygame.quit()
```

## 顯示分數

```python
font = pygame.font.SysFont("comicsansms", 14)   # 設定字體樣式及大小
# (文字, 是否開啟抗鋸齒, 字體顏色)
text = font.render("Score:{}".format(score), True, (255, 255, 255))  

screen.blit(text, (0, 0))   # 顯示文字在螢幕上(文字, 位置(x, y)))
```
目前程式碼:
```python
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
pygame.quit()
```
