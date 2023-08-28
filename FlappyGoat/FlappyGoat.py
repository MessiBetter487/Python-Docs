import pygame
import os
import sys
from random import randint
pygame.font.init()
win=pygame.display.set_mode((800,600))
pygame.display.set_caption('Flappy Goat')
JH=90
DS=4
sfont=pygame.font.Font('Cheesecake-EaOv8.ttf',30)
pfont=pygame.font.Font('Cheesecake-EaOv8.ttf',100)
gfont=pygame.font.Font('Cheesecake-EaOv8.ttf',100)
spfont=pygame.font.Font('Cheesecake-EaOv8.ttf',20)
birdimg=pygame.transform.scale(pygame.image.load(os.path.join('FlappyGoat','flappygoat.png')),(130,100))
bgimg=pygame.transform.scale(pygame.image.load(os.path.join('FlappyGoat','stadium-grandstand-wallpaper-sports-wallpapers.jpg')),(800,600))
def drawwin(goat,pipet1,pipet2,pipet3,pipet4,piped1,piped2,piped3,piped4,out,paused,gameover):
    win.blit(bgimg,(0,0))
    
    pygame.draw.rect(win,(255,255,255),pipet1)
    pygame.draw.rect(win,(255,255,255),piped1)
    pygame.draw.rect(win,(255,255,255),pipet2)
    pygame.draw.rect(win,(255,255,255),piped2)
    pygame.draw.rect(win,(255,255,255),pipet3)
    pygame.draw.rect(win,(255,255,255),piped3)
    pygame.draw.rect(win,(255,255,255),pipet4)
    pygame.draw.rect(win,(255,255,255),piped4)
    win.blit(birdimg,(345,goat.y))
    if not gameover :
        win.blit(sfont.render(out,1,(0,0,0)),(380,30))
    if gameover:
        win.blit(gfont.render(out,1,(0,0,0)),(280,230))
    
    pygame.display.update()
def main():
    FPS=60
    clock=pygame.time.Clock()
    run=True
    hval1=randint(50,350)
    hval2=randint(50,350)
    hval3=randint(50,350)
    hval4=randint(50,350)
    gameover=False
    paused=False
    q=800
    w=1000
    e=1200
    r=1400
    goat=pygame.Rect(345,210,65,35)
    keypressed=pygame.key.get_pressed()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and goat.y+JH>150 and not gameover and not paused:
                    goat.y-=JH
                if event.key == pygame.K_ESCAPE:
                    paused=True
                if event.key == pygame.K_c:
                    paused=False
                    
        if goat.y+DS>500:
            goat.y+=0
        else:
            goat.y+=DS
        if not gameover and not paused:
            ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        if not gameover and not paused:
            q-=3
            w-=3
            e-=3
            r-=3
        pipet1=pygame.Rect(q,0,45,hval1)
        piped1=pygame.Rect(q,hval1+230,45,540)
        pipet2=pygame.Rect(w,0,45,hval2)
        piped2=pygame.Rect(w,hval2+230,45,540)
        pipet3=pygame.Rect(e,0,45,hval3)
        piped3=pygame.Rect(e,hval3+230,45,540)
        pipet4=pygame.Rect(r,0,45,hval4)
        piped4=pygame.Rect(r,hval4+230,45,540)
        l=[pipet1,pipet2,pipet3,pipet4,piped1,piped2,piped3,piped4]
        for item in l:
            if goat.colliderect(item):
                gameover=True
        if q-10<=0:
            q=800
            hval1=randint(50,400)
        if w-10<=0:
            w=800
            hval2=randint(50,400)
        if e-10<=0:
            e=800
            hval3=randint(50,400)
        if r-10<=0:
            r=800
            hval4=randint(50,400)
        drawwin(goat,pipet1,pipet2,pipet3,pipet4,piped1,piped2,piped3,piped4,out,paused,gameover)
    pygame.quit()
if __name__=='__main__':
    main()