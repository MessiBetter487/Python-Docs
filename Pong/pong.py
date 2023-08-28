import pygame
from random import randint
from math import sqrt
pygame.font.init()
pygame.init()
win=pygame.display.set_mode((740,500))
BXS=9
BYS=8
MYS=10
PS=6
x=400
y=246
i=0
z=randint(1,2)
sp=[]
f=pygame.font.Font('Cheesecake-EaOv8.ttf',28)
wf=pygame.font.Font('Cheesecake-EaOv8.ttf',50)
rscore=0
lscore=0
winnertext=''
def drawwin(paddle1, paddle2, bordert, borderb,keypressed):
    win.fill((0, 0, 0))
    global x
    global y
    global i
    global z
    global BXS
    global BYS
    global lscore
    global rscore
    global winnertext  
    win.blit(f.render(str(lscore),1,(255,255,255)),(345,5))
    win.blit(f.render(str(rscore),1,(255,255,255)),(385,5))
    win.blit(wf.render(str(winnertext),1,(255,255,255)),(250,200))
    pygame.draw.rect(win, (255, 255, 255), paddle1)
    pygame.draw.rect(win, (255, 255, 255), paddle2)
    
    if rscore>=10:
        winnertext='Player 2 Wins'
        BXS=0
    if lscore>=10:
        winnertext='Player 1 Wins'
        BXS=0
    ball = pygame.draw.circle(win, (255, 255, 255), (x, y), 7)
    if ball.x > 740:
        x = 400
        y = 246
        BXS=3
        lscore+=1
    if ball.x<0:
        rscore+=1
        x = 400
        y = 246
        BXS=3
    if ball.colliderect(paddle2):
        if BXS==3:
            BXS=7
        d=paddle2.centery-ball.y
        print(d)
        BYS=d/10
        BXS=-BXS 

    if ball.colliderect(paddle1):
        if BXS==3:
            BXS=7
        d=paddle1.centery-ball.y
        BYS=d/10
        print(BYS)
        BXS=sqrt((BXS**2))
    
    if ball.colliderect(bordert) or ball.colliderect(borderb):
        BYS*=-1
    y+=BYS
    x += BXS
    pygame.display.update()    
def lpaddlemovement(paddle1,paddle2,keypressed):
    if keypressed[pygame.K_w] and paddle1.y - PS>1:
        paddle1.y-=PS
    if keypressed[pygame.K_s] and paddle1.y + PS<399:
        paddle1.y+=PS
    if keypressed [pygame.K_UP] and paddle2.y - PS>1:
        paddle2.y-=PS
    if keypressed[pygame.K_DOWN] and paddle2.y + PS<399:
        paddle2.y+=PS
   
def main():
    FPS=60
    clock=pygame.time.Clock()
    paddle1=pygame.Rect(20,200,15,500//5)
    paddle2=pygame.Rect(705,200,15,500//5)
    bordert=pygame.Rect(0,0,740,1)
    borderb=pygame.Rect(0,499,740,1)
    
    run=True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        keypressed=pygame.key.get_pressed()
        lpaddlemovement(paddle1,paddle2,keypressed)
        drawwin(paddle1,paddle2,bordert,borderb,keypressed)
    pygame.quit()
if __name__ == '__main__':
    main() 
    