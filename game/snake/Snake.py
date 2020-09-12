import pygame
import random
import time     

class Snake:
    def __init__(self,):
        pygame.init()   # 初始化PyGame所需的模塊
        self.screen_width = 400
        self.screen_height = 400

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))    # 啟動所需大小的視窗
        self.clock = pygame.time.Clock() # 實例Clock物件

        self.done = False    # 作為判定是否關閉視窗使用
        self.die = False
        self.score = 0
        self.speed = 25
        self.direction = 'x+'

        self.player_x = 0
        self.player_y = 0
        self.player_size = 25   
        self.player_num = 1
        self.player = pygame.draw.rect(self.screen, (0, 128, 255), (self.player_x, self.player_y, self.player_size, self.player_size))     
        self.player_position_ls = [[0, 0]]

        self.food_x = random.randint(0, self.screen_width)
        self.food_y = random.randint(0, self.screen_height)
        self.food_size = 25
        self.food = pygame.draw.rect(self.screen, (100, 128, 255), (self.food_x, self.food_y, self.food_size, self.food_size))

        self.font = pygame.font.SysFont("comicsansms", 14)   # 設定字體樣式及大小
        self.text = self.font.render("Score:{}".format(self.score), True, (255, 255, 255))  

    def get_event(self,):
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:   # 點擊右上角關閉按鈕時，會觸發事件
                self.done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.player_y>=0 :
                self.direction = 'y-'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.player_y<self.screen_height-self.player_size:
                self.direction = 'y+'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and self.player_x>=0:
                self.direction = 'x-'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and self.player_x<self.screen_width-self.player_size:
                self.direction = 'x+'
                
    def move_player(self,):
        self.temp_x = self.player_x
        self.temp_y = self.player_y
        
        if self.direction == 'x+':
            self.player_x += self.speed
        elif self.direction == 'x-':
            self.player_x -= self.speed
        elif self.direction == 'y+':
            self.player_y += self.speed
        elif self.direction == 'y-':
            self.player_y -= self.speed

        self.player_position_ls.pop(0)
        self.player_position_ls.append([self.player_x, self.player_y ])

    def collide(self,):
        self.player = pygame.draw.rect(self.screen, (0, 128, 255), (self.player_x, self.player_y, self.player_size, self.player_size)) 
        if self.player.colliderect(self.food):    # draw物件碰撞指令
            self.change_food_position()
            self.player_position_ls.insert(0,[self.temp_x, self.temp_y])
            self.score+=10   # 加分數
            self.text = self.font.render("Score:{}".format(self.score), True, (255, 255, 255))

    def refresh_screen(self,):
        self.screen.fill((0, 0, 0)) # 設定螢幕顏色

    def set_player(self,):        
        for i in self.player_position_ls:  
            pygame.draw.rect(self.screen, (0, 128, 255), (i[0], i[1], self.player_size, self.player_size))
            # self.player = pygame.draw.rect(self.screen, (0, 128, 255), (self.player_x, self.player_y, self.player_size, self.player_size))
        
    def check_overlapping(self,):
        self.player = pygame.draw.rect(self.screen, (0, 128, 255), (self.player_x, self.player_y, self.player_size, self.player_size)) 
        if self.player.colliderect(self.food):
            return True
        else:
            return False

    def change_food_position(self,):  
        while self.check_overlapping():
            self.food_x = random.randint(0, self.screen_width)
            self.food_y = random.randint(0, self.screen_height)
            self.set_food()
        
    def set_food(self,):
        self.food = pygame.draw.rect(self.screen, (100, 128, 255), (self.food_x, self.food_y, self.food_size, self.food_size))

    def check_die(self,):
        if self.player_x > self.screen_width-self.player_size:
            self.die = True
        elif self.player_x < 0:
            self.die = True
        elif self.player_y > self.screen_height-self.player_size:
            self.die = True
        elif self.player_y < 0:
            self.die = True

        if self.player_position_ls.count([self.player_x, self.player_y]) == 2:
            # print([self.player_x, self.player_y])
            print(self.player_position_ls)
            self.die = True

    def run(self,):
        while not self.done:
            if self.die:
                self.text = self.font.render("Your Die, Score:{}".format(self.score), True, (255, 255, 255))  
                self.screen.blit(self.text, (self.screen_width/2, self.screen_height/2))
            else: 
                self.get_event()                
                self.move_player()
                
                self.collide()
                self.refresh_screen()

                self.set_player()
                self.set_food()

                self.check_die()
                
                self.screen.blit(self.text, (0, 0))   #   顯示文字在螢幕上(文字, 位置(x, y)))
            
            self.clock.tick(60)
            pygame.display.flip()   # 更新螢幕顯示畫面
            time.sleep(0.25)

if __name__ == '__main__':
    snake = Snake()
    snake.run()