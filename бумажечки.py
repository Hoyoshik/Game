import pygame, sys, os
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1600, 900), 0, 32)

def paper():
    pygame.mixer.init()
    hellsing = pygame.mixer.Sound('Звуки и музыка\Хеллсинг.ogg')
    deathnote = pygame.mixer.Sound('Звуки и музыка\Тетрадь смерти.ogg')
    hellsing.set_volume(0.2)
    deathnote.set_volume(0.2)

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

    st = (
        'т5.png', 'т10.png', 'т15.png',
        'т20.png', 'т25.png', 'т30.png',
        'т35.png', 'т40.png', 'т45.png',
        'т50.png')

    stal = list()
    for i in st:
        fullname = os.path.join('Спрайты\Темный фон', i)
        stal.append(pygame.image.load(fullname).convert_alpha())

    bomname = ('Бумбоксина2.png', 'Бумбоксина3.png', 'Бумбоксина4.png',
               'Бумбоксина5.png', 'Бумбоксина6.png', 'Бумбоксина7.png',
               'Бумбоксина8.png', 'Бумбоксина9.png')
    bom = list()
    for img in bomname:
        fullname1 = os.path.join('Спрайты\Бумбокс', img)
        bom.append(pygame.image.load(fullname1).convert_alpha())

    mousexcaset1 = False
    mousexcaset2 = False

    pg = 0
    playmusic = False
    j = 0
    while True:
        caset1main = caset1
        caset2main = caset2
        papermain1 = paper1
        papermain2 = paper2
        papermain3 = paper3

        y1 = 0
        y2 = 0
        y3 = 0

        mx, my = pygame.mouse.get_pos()
        if mask1.collidepoint(mx, my) and mousexcaset1 == False and mousexcaset2 == False:
            papermain1 = paper11
            y1 -= 10
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    g = True
                    while g:
                        if y1 != -70:
                            y1 -= 1
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            pygame.display.update()
                        else:
                            g = False
                    g1 = True
                    c = 0
                    while g1:
                        if c <= 9:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(c)], (0, 0))
                            pygame.display.update()
                            c += 0.5
                        else:
                            g1 = False
                    rung = True
                    ytext1 = -1000
                    while rung:
                        while ytext1 != 0:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(c)], (0, 0))
                            ytext1 += 10
                            screen.blit(text1, (0, ytext1))
                            pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                rung1 = True
                                while rung1:
                                    while ytext1 != -1000:
                                        screen.fill((0, 0, 0))
                                        screen.blit(back, (0, 0))
                                        screen.blit(papermain3, (0, y3))
                                        screen.blit(papermain2, (0, y2))
                                        screen.blit(papermain1, (0, y1))
                                        if pg == 1:
                                            screen.blit(caset2, (0, 0))
                                            if playmusic:
                                                screen.blit(bom[4], (0, 0))
                                            else:
                                                screen.blit(boomboxina, (0, 0))
                                        elif pg == 2:
                                            screen.blit(caset1, (0, 0))
                                            if playmusic:
                                                screen.blit(bom[4], (0, 0))
                                            else:
                                                screen.blit(boomboxina, (0, 0))
                                        elif pg == 0 and playmusic == False:
                                            screen.blit(boombox, (0, 0))
                                            screen.blit(caset2, (0, 0))
                                            screen.blit(caset1, (0, 0))
                                        screen.blit(stal[int(c)], (0, 0))
                                        ytext1 -= 10
                                        screen.blit(text1, (0, ytext1))
                                        pygame.display.update()
                                    rung = False
                                    rung1 = False
                    sra = True
                    while sra:
                        if c != 0:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(c)], (0, 0))
                            pygame.display.update()
                            c -= 0.5
                        else:
                            sra = False
                    sra1 = True
                    while sra1:
                        if y1 != 0:
                            y1 += 1
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            pygame.display.update()
                        else:
                            sra1 =  False
                    g = False
        elif mask2.collidepoint(mx, my) and mousexcaset2 == False and mousexcaset1 == False:
            papermain2 = paper22
            y2 -= 20
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gg = True
                    while gg:
                        if y2 != -70:
                            y2 -= 1
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            pygame.display.update()
                        else:
                            gg = False
                    gg1 = True
                    cc = 0
                    while gg1:
                        if cc <= 9:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(cc)], (0, 0))
                            pygame.display.update()
                            cc += 0.5
                        else:
                            gg1 = False
                    rungg = True
                    ytextt1 = -1000
                    while rungg:
                        while ytextt1 != 0:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(cc)], (0, 0))
                            ytextt1 += 10
                            screen.blit(text2, (0, ytextt1))
                            pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                rungg1 = True
                                while rungg1:
                                    while ytextt1 != -1000:
                                        screen.fill((0, 0, 0))
                                        screen.blit(back, (0, 0))
                                        screen.blit(papermain3, (0, y3))
                                        screen.blit(papermain2, (0, y2))
                                        screen.blit(papermain1, (0, y1))
                                        if pg == 1:
                                            screen.blit(caset2, (0, 0))
                                            if playmusic:
                                                screen.blit(bom[4], (0, 0))
                                            else:
                                                screen.blit(boomboxina, (0, 0))
                                        elif pg == 2:
                                            screen.blit(caset1, (0, 0))
                                            if playmusic:
                                                screen.blit(bom[4], (0, 0))
                                            else:
                                                screen.blit(boomboxina, (0, 0))
                                        elif pg == 0 and playmusic == False:
                                            screen.blit(boombox, (0, 0))
                                            screen.blit(caset2, (0, 0))
                                            screen.blit(caset1, (0, 0))
                                        screen.blit(stal[int(cc)], (0, 0))
                                        ytextt1 -= 10
                                        screen.blit(text2, (0, ytextt1))
                                        pygame.display.update()
                                    rungg = False
                                    rungg1 = False
                    sraa = True
                    while sraa:
                        if cc != 0:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(cc)], (0, 0))
                            pygame.display.update()
                            cc -= 0.5
                        else:
                            sraa = False
                    sraa1 = True
                    while sraa1:
                        if y2 != 0:
                            y2 += 1
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            pygame.display.update()
                        else:
                            sraa1 =  False
                    gg = False
        elif mask3.collidepoint(mx, my) and mousexcaset2 == False and mousexcaset1 == False:
            papermain3 = paper33
            y3 -= 30
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ggg = True
                    while ggg:
                        if y3 != -70:
                            y3 -= 1
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            pygame.display.update()
                        else:
                            ggg = False
                    ggg1 = True
                    ccc = 0
                    while ggg1:
                        if ccc <= 9:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(ccc)], (0, 0))
                            pygame.display.update()
                            ccc += 0.5
                        else:
                            ggg1 = False
                    runggg = True
                    ytexttt1 = -1000
                    while runggg:
                        while ytexttt1 != 0:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(ccc)], (0, 0))
                            ytexttt1 += 10
                            screen.blit(text3, (0, ytexttt1))
                            pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                runggg1 = True
                                while runggg1:
                                    while ytexttt1 != -1000:
                                        screen.fill((0, 0, 0))
                                        screen.blit(back, (0, 0))
                                        screen.blit(papermain3, (0, y3))
                                        screen.blit(papermain2, (0, y2))
                                        screen.blit(papermain1, (0, y1))
                                        if pg == 1:
                                            screen.blit(caset2, (0, 0))
                                            if playmusic:
                                                screen.blit(bom[4], (0, 0))
                                            else:
                                                screen.blit(boomboxina, (0, 0))
                                        elif pg == 2:
                                            screen.blit(caset1, (0, 0))
                                            if playmusic:
                                                screen.blit(bom[4], (0, 0))
                                            else:
                                                screen.blit(boomboxina, (0, 0))
                                        elif pg == 0 and playmusic == False:
                                            screen.blit(boombox, (0, 0))
                                            screen.blit(caset2, (0, 0))
                                            screen.blit(caset1, (0, 0))
                                        screen.blit(stal[int(ccc)], (0, 0))
                                        ytexttt1 -= 10
                                        screen.blit(text3, (0, ytexttt1))
                                        pygame.display.update()
                                    runggg = False
                                    runggg1 = False
                    sraaa = True
                    while sraaa:
                        if ccc != 0:
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            screen.blit(stal[int(ccc)], (0, 0))
                            pygame.display.update()
                            ccc -= 0.5
                        else:
                            sraaa = False
                    sraaa1 = True
                    while sraaa1:
                        if y3 != 0:
                            y3 += 1
                            screen.fill((0, 0, 0))
                            screen.blit(back, (0, 0))
                            screen.blit(papermain3, (0, y3))
                            screen.blit(papermain2, (0, y2))
                            screen.blit(papermain1, (0, y1))
                            if pg == 1:
                                screen.blit(caset2, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 2:
                                screen.blit(caset1, (0, 0))
                                if playmusic:
                                    screen.blit(bom[4], (0, 0))
                                else:
                                    screen.blit(boomboxina, (0, 0))
                            elif pg == 0 and playmusic == False:
                                screen.blit(boombox, (0, 0))
                                screen.blit(caset2, (0, 0))
                                screen.blit(caset1, (0, 0))
                            pygame.display.update()
                        else:
                            sraaa1 =  False
                    ggg = False

        if maskcaset1.collidepoint(mx, my) and mousexcaset1 == False and mousexcaset2 == False and pg == 0:
            caset1main = caset11
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and mousexcaset2 == False:
                    mousexcaset1 = True
        elif maskcaset2.collidepoint(mx, my) and mousexcaset2 == False and mousexcaset1 == False and pg == 0:
            caset2main = caset22
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and mousexcaset1 == False:
                    mousexcaset2 = True
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if boomboxrect.collidepoint(mx, my) and (mousexcaset1 or mousexcaset2):
                    if mousexcaset1:
                        mousexcaset1 = False
                        pg = 1
                    else:
                        mousexcaset2 = False
                        pg = 2
                if boomboxplayrect.collidepoint(mx, my) and pg != 0:
                    playmusic = True
                if boomboxstoprect.collidepoint(mx, my):
                    while j != 0:
                        screen.fill((0, 0, 0))
                        screen.blit(back, (0, 0))
                        screen.blit(papermain3, (0, y3))
                        screen.blit(papermain2, (0, y2))
                        screen.blit(papermain1, (0, y1))
                        screen.blit(bom[j], (0, 0))
                        j -= 1
                        if pg == 1:
                            screen.blit(caset2main, (0, 0))
                        else:
                            screen.blit(caset1main, (0, 0))
                        pygame.display.update()
                    mousexcaset1 = False
                    mousexcaset2 = False
                    pg = 0
                    playmusic = False
                    j = 0
                    hellsing.stop()
                    deathnote.stop()

        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        screen.blit(papermain3, (0, y3))
        screen.blit(papermain2, (0, y2))
        screen.blit(papermain1, (0, y1))
        if playmusic:
            while j != 4:
                screen.fill((0, 0, 0))
                screen.blit(back, (0, 0))
                screen.blit(papermain3, (0, y3))
                screen.blit(papermain2, (0, y2))
                screen.blit(papermain1, (0, y1))
                screen.blit(bom[j], (0, 0))
                if pg == 1:
                    screen.blit(caset2main, (0, 0))
                    hellsing.play()
                else:
                    screen.blit(caset1main, (0, 0))
                    deathnote.play()
                j += 1
                pygame.display.update()
                mainClock.tick(60)
                print(j)
            if j == 4:

                screen.fill((0, 0, 0))
                screen.blit(back, (0, 0))
                screen.blit(papermain3, (0, y3))
                screen.blit(papermain2, (0, y2))
                screen.blit(papermain1, (0, y1))
                screen.blit(bom[j], (0, 0))
                if pg == 1:
                    screen.blit(caset2main, (0, 0))
                else:
                    screen.blit(caset1main, (0, 0))
        else:
            if pg == 0:
                screen.blit(boombox, (0, 0))
            else:
                screen.blit(boomboxina, (0, 0))
            if mousexcaset1:
                screen.blit(caset2main, (0, 0))
                screen.blit(caset1main, (mx - 230, my - 700))
            elif mousexcaset2:
                screen.blit(caset1main, (0, 0))
                screen.blit(caset2main, (mx - 184, my - 200))
            if pg == 1:
                screen.blit(caset2main, (0, 0))
            elif pg == 2:
                screen.blit(caset1main, (0, 0))
            elif pg == 0 and mousexcaset1 == False and mousexcaset2 == False:
                screen.blit(caset2main, (0, 0))
                screen.blit(caset1main, (0, 0))

        #pygame.draw.rect(screen, pygame.Color('red'), boomboxstoprect)
        #pygame.draw.rect(screen, pygame.Color('blue'), mask1)
        #pygame.draw.rect(screen, pygame.Color('magenta'), mask3)
        pygame.display.update()
        mainClock.tick(60)
paper()