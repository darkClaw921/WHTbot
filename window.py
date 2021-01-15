# Подключение библиотеки PyGame
import pygame
import whtBot
import time
from threading import Thread
# Инициализация PyGame
pygame.init()

# Окно игры: размер, позиция
gameScreen = pygame.display.set_mode((1250, 750))

# Модуль os - позиция окна
import os
x = 0
y = 0
os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# Параметры окна
X = 1250
Y = 750
size = [X, Y]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test drawings")
gameScreen.fill((0,0,0))
color = [255,255,255]
TYR = 1
# pygame.draw.rect(screen, color, [0,0,X/3,Y/5],1 )

# totalComand = 20
# S = X * Y

# Srect = S / 20
font = pygame.font.SysFont('couriernew', 40)

def draw_rects(tyr: int):
    global X,Y,screen,TYR
    while True:
        x1 = 0
        y1 = 0
        x2 = X/3
        y2 = Y/8
        count = 0
        comands = whtBot.who_end(TYR,1)
        
        gameScreen.fill((0,0,0))
        
        for comand in comands:
            if count == 8:
                x1 += X/3
                y1 = 0
                # x2 += (X/3) - 500
                count = 0

            if comands[comand] == 'OK':
                pygame.draw.rect(screen, 'green', [x1,y1,x2,y2],0 )
            else:
                pygame.draw.rect(screen, color, [x1,y1,x2,y2],1 )
                text = font.render(comand, True, 'green')
                screen.blit(text, (x1, y1))
                # text1 = font.render(f'{x1} {x2}', True, 'green')
                # screen.blit(text1, (x1, y1))

            y1 += y2
            count += 1
            print('Данные получены')
        time.sleep(10)
        

Thread(target=draw_rects, args=(str(TYR))).start()
Thread(target=draw_rects, args=(str(TYR)))
# Цикл игры
runGame = True # флаг выхода из цикла игры
clock = pygame.time.Clock()

while runGame:
    # Отслеживание события: "закрыть окно"
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT: 
            runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                TYR -= 1
            elif event.key == pygame.K_RIGHT:
                TYR += 1

    pygame.display.flip()
    time.sleep(0.1)
    print('new iteration')
# Выход из игры: 
pygame.quit()