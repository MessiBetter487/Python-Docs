import pygame
import os
pygame.font.init()
win=pygame.display.set_mode((1050,600))
pygame.display.set_caption('SpaceShooters')
limgi=pygame.image.load(os.path.join('SpaceShooter','yellowss.png'))
limg=pygame.transform.rotate(pygame.transform.scale(limgi,(55,45)),270)
rimgi=pygame.image.load(os.path.join('SpaceShooter','redss.png'))
rimg=pygame.transform.rotate(pygame.transform.scale(rimgi,(55,45)),90)
spaceimg=pygame.image.load(os.path.join('SpaceShooter','3137991.jpg'))
VEL=4
BVEL=8
lbullet=[]
rbullet=[]
maxbullets=2
healthfont=pygame.font.Font('publicpixel.ttf',40)
winnerfont=pygame.font.Font('publicpixel.ttf',75)
lhit=pygame.USEREVENT +1
rhit=pygame.USEREVENT +2
x=1
def drawwin(left,right,border,border2,rbullet,lbullet,llives,rlives):
    win.fill((255,255,255))
    win.blit(spaceimg,(0,0))
    win.blit(healthfont.render('Health: '+ str(llives),1,(0,255,0)),(10,10))
    rhealthtext='Health: '+ str(rlives)
    win.blit(healthfont.render(rhealthtext,1,(0,255,0)),(640,10))
    pygame.draw.rect(win,(0,255,0),border)
    pygame.draw.rect(win,(0,255,0),border2)
    for bullet in lbullet:
        pygame.draw.rect(win,(255,0,0),bullet)
    for bullet in rbullet:
        pygame.draw.rect(win,(255,255,0),bullet)
    win.blit(limg,(left.x,left.y))
    win.blit(rimg,(right.x,right.y))
    winner=''
    if llives <= 0:
        winner='Yellow Wins!'
        win.blit(winnerfont.render(winner,1,(0,255,0)),(80,200))
    if rlives <= 0:
        winner='Red Wins!'
        win.blit(winnerfont.render(winner,1,(0,255,0)),(175,200))
    pygame.display.update()
def handlebullets(left,right,lbullet,rbullet):
    for bullet in lbullet:
        bullet.x +=BVEL
        if right.colliderect(bullet):
            pygame.event.post(pygame.event.Event(rhit))
            lbullet.remove(bullet)
        elif bullet.x>1050:
            lbullet.remove(bullet)
    for bullet in rbullet:
        bullet.x -=BVEL
        if left.colliderect(bullet):
            pygame.event.post(pygame.event.Event(lhit))
            rbullet.remove(bullet)
        elif bullet.x<0:
            rbullet.remove(bullet)            
def leftmovement(keypressed,left,border,border2):
    if keypressed[pygame.K_w] and left.y - VEL>border2.y:
        left.y-=VEL
    if keypressed[pygame.K_s] and left.y + VEL< 555:
        left.y+=VEL
    if keypressed[pygame.K_a] and left.x - VEL>0:
        left.x-=VEL
    if keypressed[pygame.K_d] and left.x + VEL<border.x-55:
        left.x+=VEL
def rightmovement(keypressed,right,border,border2):
    if keypressed[pygame.K_UP] and right.y - VEL>border2.y:
        right.y-=VEL
    if keypressed[pygame.K_DOWN] and right.y + VEL< 555:
        right.y+=VEL
    if keypressed[pygame.K_LEFT] and right.x - VEL>border.x:
        right.x-=VEL
    if keypressed[pygame.K_RIGHT] and right.x + VEL<995:
        right.x+=VEL
def main():
    lbullet=[]
    rbullet=[]
    llives=10
    rlives=10
    left=pygame.Rect(250,300,55,45)
    right=pygame.Rect(755,300,55,45)
    border=pygame.Rect(520,0,10,600)
    border2=pygame.Rect(0,55,1050,6)
    FPS=60
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and len(lbullet)<= maxbullets:
                    bullet=pygame.Rect(left.x+54,left.y+ 45//2+4,7,3)
                    lbullet.append(bullet)
                if event.key==pygame.K_SPACE and len(rbullet)<= maxbullets:
                    bullet=pygame.Rect(right.x,right.y+ 45//2+2,7,3)
                    rbullet.append(bullet)
            if event.type==lhit:
                    llives =int(llives)- 1
            if event.type==rhit:
                    rlives =int(rlives)- 1
        keypressed=pygame.key.get_pressed()
        leftmovement(keypressed,left,border,border2)
        rightmovement(keypressed,right,border,border2)
        drawwin(left,right,border,border2,rbullet,lbullet,llives,rlives)      
        handlebullets(left,right,lbullet,rbullet)
    pygame.quit()
if __name__ == '__main__':
    main()