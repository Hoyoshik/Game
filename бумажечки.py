import pygame, sys, os
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1600, 900), 0, 32)

def dispay_uptade_function():
    x1 = x2 = y_caset1 = y_caset2 = 0
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))
    screen.blit(papermain3, (0, y3))
    screen.blit(papermain2, (0, y2))
    screen.blit(papermain1, (0, y1))
    if take_caset == 1 and bomboxstep == 0:
        x1, y_caset1 = mouse_pos[0]- 230, mouse_pos[1] - 700
    if take_caset == 2 and bomboxstep == 0:
        x2, y_caset2 = mouse_pos[0] - 184, mouse_pos[1] - 200
    if the_late_is_installed == 1:
        screen.blit(bom[bomboxstep], (0, 0))
        screen.blit(maincaset2, (x2, y_caset2))
    if the_late_is_installed == 2:
        screen.blit(bom[bomboxstep], (0, 0))
        screen.blit(maincaset1, (x1, y_caset1))
    if the_late_is_installed == 0 and bomboxstep == 0:
        screen.blit(bom[bomboxstep], (0, 0))
        screen.blit(maincaset2, (x2, y_caset2))
        screen.blit(maincaset1, (x1, y_caset1))
    if c != 0:
        screen.blit(stal[int(c)], (0, 0))
    if ytext1 != -1000:
        screen.blit(text1, (0, ytext1))
    if ytext2 != -1000:
        screen.blit(text2, (0, ytext2))
    if ytext3 != -1000:
        screen.blit(text3, (0, ytext3))
    screen.blit(IMAGE, mouse_pos)
    pygame.display.update()
    mainClock.tick(120)

def paper_down(num):
    global y1, y2, y3, c, ytext1, ytext2, ytext3
    condition = False
    while True:
        if num == 1:
            if y1 != 0:
                y1 += 1
            if ytext1 != -1000:
                ytext1 -= 10
            elif y1 == 0 and ytext1 == -1000:
                condition = True
        if num == 2:
            if y2 != 0:
                y2 += 1
            if ytext2 != -1000:
                ytext2 -= 10
            elif y2 == 0 and ytext2 == -1000:
                condition = True
        if num == 3:
            if y3 != 0:
                y3 += 1
            if ytext3 != -1000:
                ytext3 -= 10
            elif y3 == 0 and ytext2 == -1000:
                condition = True
        if c > 0:
            c -= 0.5
        elif int(c) == 0 and condition:
            break
        dispay_uptade_function()

def paper_up(num):
    mouse = False
    global y1, y2, y3, c, ytext1, ytext2, ytext3
    condition = False
    while True:
        if num == 1:
            if y1 != -70:
                y1 -= 1
            if ytext1 != 0:
                ytext1 += 10
            elif y1 == -70 and ytext1 == 0:
                condition = True
        if num == 2:
            if y2 != -70:
                y2 -= 1
            if ytext2 != 0:
                ytext2 += 10
            elif y2 == -70 and ytext2 == 0:
                condition = True
        if num == 3:
            if y3 != -70:
                y3 -= 1
            if ytext3 != 0:
                ytext3 += 10
            elif y3 == -70 and ytext3 == 0:
                condition = True
        if c <= 9:
            c += 0.5
        if condition:
            if int(c) == 9:
                if mouse == False:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse = True
                if mouse:
                    paper_down(num)
                    break
        dispay_uptade_function()

def paper():
    global papermain1, papermain2, papermain3,\
        y1, y2, y3, ytext1, ytext2, ytext3,\
        c, maincaset1, maincaset2, take_caset, the_late_is_installed, \
        bomboxstep
    bomboxstep = 0
    c = 0
    take_caset = 0
    the_late_is_installed = 0
    ytext1 = -1000
    ytext2 = -1000
    ytext3 = -1000
    running = True
    while running:
        mouse_down = False
        y1 = y2 = y3 = 0
        maincaset1 = caset1
        maincaset2 = caset2
        papermain1 = paper1
        papermain2 = paper2
        papermain3 = paper3
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
        mx, my = pygame.mouse.get_pos()
        if mask1.collidepoint(mx, my) and take_caset == 0:
            papermain1 = paper11
            y1 -= 10
            if mouse_down:
                paper_up(1)
        if mask2.collidepoint(mx, my) and take_caset == 0:
            papermain2 = paper22
            y2 -= 10
            if mouse_down:
                paper_up(2)
        if mask3.collidepoint(mx, my) and take_caset == 0:
            papermain3 = paper33
            y3 -= 10
            if mouse_down:
                paper_up(3)
        if maskcaset1.collidepoint(mx, my) and take_caset == 0:
            maincaset1 = caset11
            if mouse_down:
                take_caset = 1
        if maskcaset2.collidepoint(mx, my) and take_caset == 0:
            maincaset2 = caset22
            if mouse_down:
                take_caset = 2
        if take_caset == 1:
            if boomboxrect.collidepoint(mx, my):
                if mouse_down:
                    take_caset = 0
                    the_late_is_installed = 1
                    bomboxstep = 1
        elif take_caset == 2:
            if boomboxrect.collidepoint(mx, my):
                if mouse_down:
                    take_caset = 0
                    the_late_is_installed = 2
                    bomboxstep = 1
        if boomboxplayrect.collidepoint(mx, my) and bomboxstep == 1 and mouse_down:
            bomboxstep = 9
        if boomboxstoprect.collidepoint(mx, my) and bomboxstep == 9 and mouse_down:
            bomboxstep = 0
            the_late_is_installed = 0
            take_caset = 0

        dispay_uptade_function()


pygame.mixer.init()
hellsing = pygame.mixer.Sound('Звуки и музыка\Хеллсинг.ogg')
deathnote = pygame.mixer.Sound('Звуки и музыка\Тетрадь смерти.ogg')
hellsing.set_volume(0.2)
deathnote.set_volume(0.2)

pygame.mixer.music.load('Звуки и музыка\дождьдом.mp3')

IMAGE = pygame.image.load('курсор2.png').convert_alpha()

back = pygame.image.load('фон для бумажек.png').convert_alpha()
paper11 = pygame.image.load('бумага 11.png').convert_alpha()
paper22 = pygame.image.load('бумага 22.png').convert_alpha()
paper33 = pygame.image.load('бумага 33.png').convert_alpha()

paper1 = pygame.image.load('бумага 1.png').convert_alpha()
paper2 = pygame.image.load('бумага 2.png').convert_alpha()
paper3 = pygame.image.load('бумага 3.png').convert_alpha()

mask1 = pygame.Rect(625, 175, 410, 550)
mask2 = pygame.Rect(590, 175, 34, 550)
mask3 = pygame.Rect(555, 175, 34, 550)

boombox = pygame.image.load('Спрайты\Бумбокс\Бумбоксина0.png').convert_alpha()
caset1 = pygame.image.load('Спрайты\Бумбокс\пластинка1.png').convert_alpha()
caset2 = pygame.image.load('Спрайты\Бумбокс\пластинка2.png').convert_alpha()
caset11 = pygame.image.load('Спрайты\Бумбокс\пластинка11.png').convert_alpha()
caset22 = pygame.image.load('Спрайты\Бумбокс\пластинка22.png').convert_alpha()
boomboxina = pygame.image.load('Спрайты\Бумбокс\Бумбоксина.png').convert_alpha()

maskcaset1 = pygame.Rect(70, 550, 320, 310)
maskcaset2 = pygame.Rect(30, 40, 310, 320)
boomboxrect = pygame.Rect(1150, 500, 310, 320)
boomboxplayrect = pygame.Rect(1194, 800, 20, 30)
boomboxstoprect = pygame.Rect(1225, 800, 20, 30)

text1 = pygame.image.load('Спрайты\Текст\Записка 1.png').convert_alpha()
text2 = pygame.image.load('Спрайты\Текст\Записка 2.png').convert_alpha()
text3 = pygame.image.load('Спрайты\Текст\Записка 3.png').convert_alpha()

textlist = list()
textlist.append(text1)
textlist.append(text2)
textlist.append(text3)

st = (
    'т5.png', 'т10.png', 'т15.png',
    'т20.png', 'т25.png', 'т30.png',
    'т35.png', 'т40.png', 'т45.png',
    'т50.png')

stal = list()
for i in st:
    fullname = os.path.join('Спрайты\Темный фон', i)
    stal.append(pygame.image.load(fullname).convert_alpha())

bomname = ('Бумбоксина0.png', 'Бумбоксина.png', 'Бумбоксина2.png', 'Бумбоксина3.png',
           'Бумбоксина4.png', 'Бумбоксина5.png', 'Бумбоксина6.png', 'Бумбоксина7.png',
           'Бумбоксина8.png', 'Бумбоксина9.png')
bom = list()
for img in bomname:
    fullname1 = os.path.join('Спрайты\Бумбокс', img)
    bom.append(pygame.image.load(fullname1).convert_alpha())

mousexcaset1 = False
mousexcaset2 = False

schet = 0
pg = 0
j = 0
paper()