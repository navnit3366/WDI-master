import pygame
import time

pygame.init
display=pygame.display.set_mode((695,400))
pygame.display.set_caption("WSZYSTKIEGO NAJLEPSZEGO<3")

black=(0,0,0)
green=(0,204,0)
white=(255,255,255)
pink=(255,0,255)
red=(255,51,153)
etap=0
os_xkaktus=32
os_ykaktus=180

os_x=50
os_y=50
szerliter=30
grubliter=10
wysliter=20
wysbelki=50
wyjscie=1
def kaktus1(a):
    pygame.draw.rect(display,green, [os_xkaktus+a,os_ykaktus+80,30,130])
    pygame.draw.rect(display, green, [os_xkaktus + a-25, os_ykaktus+55 + 50, 15, 60])
    pygame.draw.rect(display, green, [os_xkaktus + a-25, os_ykaktus +165, 30, 10])
    pygame.draw.rect(display, green, [os_xkaktus + a +25, os_ykaktus + 135, 30, 10])
    pygame.draw.rect(display, green, [os_xkaktus + a +40, os_ykaktus + 110, 15, 30])
    pygame.draw.rect(display, black, [os_xkaktus + a+5, os_ykaktus +95, 5, 5])
    pygame.draw.rect(display, black, [os_xkaktus + a+ 20, os_ykaktus + 95, 5, 5])
    pygame.draw.rect(display, red, [os_xkaktus + a+9, os_ykaktus + 105, 12, 8])

def kaktus2(a):
    pygame.draw.rect(display, green, [os_xkaktus + a, os_ykaktus + 80, 30, 130])
    pygame.draw.rect(display, green, [os_xkaktus + a +40, os_ykaktus + 105, 15, 60])
    pygame.draw.rect(display, green, [os_xkaktus + a + 25, os_ykaktus + 165, 30, 10])
    pygame.draw.rect(display, green, [os_xkaktus + a -25, os_ykaktus + 135, 30, 10])
    pygame.draw.rect(display, green, [os_xkaktus + a -25, os_ykaktus + 110, 15, 30])
    pygame.draw.rect(display, black, [os_xkaktus + a + 5, os_ykaktus + 95, 5, 5])
    pygame.draw.rect(display, black, [os_xkaktus + a + 20, os_ykaktus + 95, 5, 5])
    pygame.draw.rect(display, red, [os_xkaktus + a + 8, os_ykaktus + 105, 14, 8])
def napis():
    #s
    pygame.draw.rect(display, pink, [os_x, os_y, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x, os_y, grubliter, wysliter])
    pygame.draw.rect(display, pink, [os_x, os_y+wysliter, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x+wysliter, os_y+wysliter, grubliter, wysliter])
    pygame.draw.rect(display, pink, [os_x, os_y+2*wysliter, szerliter, grubliter])

    #t
    pygame.draw.rect(display, pink, [os_x+50, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 35, os_y, szerliter+10, grubliter])

    #o
    pygame.draw.rect(display, pink, [os_x + 80, os_y, grubliter, wysbelki])
    pygame.draw.rect(display, pink, [os_x + 85, os_y, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 110, os_y, grubliter, wysbelki])
    pygame.draw.rect(display, pink, [os_x + 85, os_y+40, szerliter, grubliter])

    #l
    pygame.draw.rect(display, pink, [os_x + 150, os_y, grubliter, wysbelki])
    pygame.draw.rect(display, pink, [os_x + 150, os_y+40, szerliter, grubliter])
    #a
    pygame.draw.rect(display, pink, [os_x+190, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 220, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 190, os_y, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 190, os_y+20, szerliter, grubliter])
    #t
    pygame.draw.rect(display, pink, [os_x + 250, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 235, os_y, szerliter + 10, grubliter])

    #k
    pygame.draw.rect(display, pink, [os_x + 310, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 340, os_y, grubliter, 20])
    pygame.draw.rect(display, pink, [os_x + 340, os_y+30, grubliter, 20])
    pygame.draw.rect(display, pink, [os_x + 310, os_y+20, szerliter, grubliter])

    #a
    pygame.draw.rect(display, pink, [os_x + 360, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 390, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 360, os_y, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 360, os_y + 20, szerliter, grubliter])

    #r
    pygame.draw.rect(display, pink, [os_x + 410, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 410, os_y, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 410, os_y + 20, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 435, os_y, grubliter, 20])
    pygame.draw.rect(display, pink, [os_x + 435, os_y+40, grubliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 435, os_y + 30, grubliter, grubliter])

    #o
    pygame.draw.rect(display, pink, [os_x + 455, os_y, grubliter, wysbelki])
    pygame.draw.rect(display, pink, [os_x + 460, os_y, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 485, os_y, grubliter, wysbelki])
    pygame.draw.rect(display, pink, [os_x + 460, os_y + 40, szerliter, grubliter])

    #l
    pygame.draw.rect(display, pink, [os_x + 505, os_y, grubliter, wysbelki])
    pygame.draw.rect(display, pink, [os_x + 505, os_y + 40, szerliter, grubliter])

    #a
    pygame.draw.rect(display, pink, [os_x + 545, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 575, os_y, grubliter, 50])
    pygame.draw.rect(display, pink, [os_x + 545, os_y, szerliter, grubliter])
    pygame.draw.rect(display, pink, [os_x + 545, os_y + 20, szerliter, grubliter])

    #!
    pygame.draw.rect(display, pink, [os_x + 595, os_y, grubliter, 35])
    pygame.draw.rect(display, pink, [os_x + 595, os_y+40, grubliter, 10])
while wyjscie<100:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            wyjscie=101



    if etap%2==0:
        for i in range(0,11):

            display.fill(white)
            napis()
            for a in range(0,700,100):
                kaktus1(a)

            pygame.display.update()
            os_y=os_y+10
            time.sleep(0.15)
            etap=etap+1
            wyjscie=wyjscie+1
    else:
        for i in range(0, 11):
            display.fill(white)
            napis()
            for a in range(0,700,100):
                kaktus2(a)

            pygame.display.update()
            os_y = os_y - 10
            time.sleep(0.15)
            etap=etap+1
            wyjscie = wyjscie + 1


pygame.quit()
quit()

