import pygame, sys
from pygame.locals import *
import PREVIEW


def ACT1():
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        playerR = pygame.image.load('персонаж.png')
        playerL = pygame.image.load('персонаж2.png')
        background = pygame.image.load('фон3.png')
        background_x = 0
        dedx = 2000
        playerDED = pygame.image.load('ГробовщикЛ.png')
        key = pygame.image.load('Гробовщик.png')

        x = 20
        speed = 20
        c = 0
        c1 = 0
        img_names = ('0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png')
        all_imgs = list()
        all_imgs2 = list()
        for img in img_names:
            all_imgs.append(pygame.image.load(img))

        img_names2 = (
            'кл1пр.png', 'кл2пр.png', 'кл3пр.png', 'кл4пр.png', 'кл5пр.png', 'кл6пр.png', 'кл7пр.png',
            'кл8пр.png',
            'кл9пр.png', 'кл10пр.png', 'кл11пр.png', 'кл12пр.png', 'кл13пр.png')
        for img2 in img_names2:
            all_imgs2.append(pygame.image.load(img2))
        clock = pygame.time.Clock()
        running = True
        fight = False
        grDead = False

        while running:
            player = playerR
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_menu()
                elif pygame.mouse.get_focused():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                        screen.blit(IMAGE, mouse_pos)
                        pygame.display.flip()
                else:
                    pygame.display.flip()
            move = pygame.key.get_pressed()
            y = 0
            if dedx != 1380:
                if move[pygame.K_LEFT] and x > 20:
                    x -= speed
                    player = playerL
                elif move[pygame.K_RIGHT] and x <= 1250:
                    x += speed
                    player = all_imgs2[c1]
                    c1 += 1
                elif move[pygame.K_RIGHT] and x >= 1250 and background_x != -1300:
                    background_x -= speed
                    dedx -= speed
                    player = all_imgs2[c1]
                    c1 += 1
                elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                    background_x += speed
                    dedx += speed
            elif x == 1260 and move[pygame.K_SPACE]:
                back = pygame.image.load('фон3.png')
                ded1 = pygame.transform.smoothscale(pygame.image.load('битваГ1.png'), (600, 600))
                ded2 = pygame.transform.smoothscale(pygame.image.load('битваГ2.png'), (600, 600))
                ded3 = pygame.transform.smoothscale(pygame.image.load('битваГ3.png'), (600, 600))
                p1 = pygame.transform.smoothscale(pygame.image.load('БитваП1.png'), (600, 600))
                p2 = pygame.transform.smoothscale(pygame.image.load('БитваП2.png'), (600, 600))
                p3 = pygame.transform.smoothscale(pygame.image.load('БитваП3.png'), (600, 600))
                battle = list()
                battle.append(p1)
                battle.append(p2)
                battle.append(p3)

                battle1 = list()
                battle1.append(ded1)
                battle1.append(ded2)
                battle1.append(ded3)

                grob = (
                'Полоска здоровья.png', 'Полоска здоровья1.png', 'Полоска здоровья2.png', 'Полоска здоровья3.png',
                'Полоска здоровья4.png', 'Полоска здоровья5.png', 'Полоска здоровья6.png', 'Полоска здоровья7.png',
                'Полоска здоровья8.png')
                grob1 = list()
                for img in grob:
                    grob1.append(pygame.image.load(img))

                grob2 = list()
                grob3 = (
                'Полоска здоровья.png', 'Полоска здоровья11.png', 'Полоска здоровья22.png', 'Полоска здоровья33.png',
                'Полоска здоровья44.png')
                for mgi in grob3:
                    grob2.append(pygame.image.load(mgi))
                j = 0
                g = 0
                kadrplayer = 0
                c = False
                c1 = False
                schetpi1 = 0
                schetpi = 0
                br = True
                while br:
                    screen.fill((0, 0, 0))
                    screen.blit(back, (0, 0))
                    screen.blit(pygame.transform.scale(grob1[g], (400, 50)), (300, 250))
                    screen.blit(pygame.transform.scale(grob2[kadrplayer], (400, 50)), (840, 250))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == KEYDOWN:
                            if event.key == K_SPACE and c != True:
                                c = True
                                if kadrplayer == 4:
                                    br = False
                                    grDead = True
                                    break
                                else:
                                    kadrplayer += 1
                            if event.key == K_ESCAPE:
                                sys.exit()
                    if c == True:
                        screen.blit(battle[j], (450, 300))
                        if j != 2:
                            j += 1
                        else:
                            c = False
                            screen.blit(battle[j], (450, 300))
                            j = 0

                    else:
                        screen.blit(battle[0], (450, 300))

                    if schetpi % 10 == 0:
                        c1 = True
                        if g == 8:
                            pass
                        else:
                            g += 1
                    if c1 == True:
                        screen.blit(battle1[schetpi1], (450, 300))
                        if schetpi1 != 2:
                            schetpi1 += 1
                        else:
                            c1 = False
                            screen.blit(battle1[schetpi1], (450, 300))
                            schetpi1 = 0
                    else:
                        screen.blit(battle1[0], (450, 300))
                    pygame.display.update()
                    mainClock.tick(10)
                    schetpi += 1

            if grDead == True:
                dedx -= speed

            if move[pygame.K_SPACE] and x > 1100 and dedx < 100:
                ACT1_5()
                pygame.quit()
            c += 1
            if c == 8:
                c = 0
            if c1 == 13:
                c1 = 0
            screen.blit(key, (x+10, y+10))
            screen.blit(background, (background_x, y))
            screen.blit(player, (x, y))
            screen.blit(playerDED, (dedx, y))
            screen.blit(all_imgs[c], (background_x, y))
            pygame.display.update()
        pygame.quit()


def ACT1_5():
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        playerR = pygame.image.load('персонаж.png')
        playerL = pygame.image.load('персонаж2.png')
        background = pygame.image.load('фон2.png')
        background_x = 0
        x = 20
        speed = 20
        c = 0
        c1 = 0
        all_imgs2 = list()

        img_names2 = (
            'кл1пр.png', 'кл2пр.png', 'кл3пр.png', 'кл4пр.png', 'кл5пр.png', 'кл6пр.png', 'кл7пр.png',
            'кл8пр.png',
            'кл9пр.png', 'кл10пр.png', 'кл11пр.png', 'кл12пр.png', 'кл13пр.png')
        for img2 in img_names2:
            all_imgs2.append(pygame.image.load(img2))
        clock = pygame.time.Clock()
        running = True
        while running:
            player = playerR
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_menu()
                elif pygame.mouse.get_focused():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                        screen.blit(IMAGE, mouse_pos)
                        pygame.display.flip()
                else:
                    pygame.display.flip()
            move = pygame.key.get_pressed()
            y = 0
            if move[pygame.K_LEFT] and x > 20:
                x -= speed
                player = playerL
            elif move[pygame.K_RIGHT] and x <= 1250:
                x += speed
                player = all_imgs2[c1]
                c1 += 1
            elif move[pygame.K_RIGHT] and x >= 1250:
                player = all_imgs2[c1]
                c1 += 1
            c += 1
            if c == 8:
                c = 0
            if c1 == 13:
                c1 = 0

            screen.blit(background, (background_x, y))
            screen.blit(player, (x, y))
            pygame.display.update()
        pygame.quit()


IMAGE = pygame.image.load('курсор2.png')

def fight():
    back = pygame.image.load('фон3.png')
    ded1 = pygame.transform.smoothscale(pygame.image.load('битваГ1.png'), (600, 600))
    ded2 = pygame.transform.smoothscale(pygame.image.load('битваГ2.png'), (600, 600))
    ded3 = pygame.transform.smoothscale(pygame.image.load('битваГ3.png'), (600, 600))
    p1 = pygame.transform.smoothscale(pygame.image.load('БитваП1.png'), (600, 600))
    p2 = pygame.transform.smoothscale(pygame.image.load('БитваП2.png'), (600, 600))
    p3 = pygame.transform.smoothscale(pygame.image.load('БитваП3.png'), (600, 600))
    battle = list()
    battle.append(p1)
    battle.append(p2)
    battle.append(p3)

    battle1 = list()
    battle1.append(ded1)
    battle1.append(ded2)
    battle1.append(ded3)

    grob = ('Полоска здоровья.png', 'Полоска здоровья1.png', 'Полоска здоровья2.png', 'Полоска здоровья3.png',
            'Полоска здоровья4.png', 'Полоска здоровья5.png', 'Полоска здоровья6.png', 'Полоска здоровья7.png', 'Полоска здоровья8.png')
    grob1 = list()
    for img in grob:
        grob1.append(pygame.image.load(img))

    grob2 = list()
    grob3 = ('Полоска здоровья.png', 'Полоска здоровья11.png', 'Полоска здоровья22.png', 'Полоска здоровья33.png',
            'Полоска здоровья44.png')
    for mgi in grob3:
        grob2.append(pygame.image.load(mgi))
    j = 0
    g = 0
    kadrplayer = 0

    c = False
    c1 = False
    schetpi1 = 0
    schetpi = 0
    while True:
        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        screen.blit(pygame.transform.scale(grob1[g], (400, 50)), (300, 250))
        screen.blit(pygame.transform.scale(grob2[kadrplayer], (400, 50)), (840, 250))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and c != True:
                    c = True
                    if kadrplayer == 4:
                        pygame.quit()
                        fight = True
                        ACT1()
                    else:
                         kadrplayer += 1

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if c == True:
            screen.blit(battle[j], (450, 300))
            if j != 2:
                j += 1
            else:
                c = False
                screen.blit(battle[j], (450, 300))
                j = 0
        else:
            screen.blit(battle[0], (450, 300))

        if schetpi % 10 == 0:
            c1 = True
            if g == 8:
                pass
            else:
                g += 1
        if c1 == True:
            screen.blit(battle1[schetpi1], (450, 300))
            if schetpi1 != 2:
                schetpi1 += 1
            else:
                c1 = False
                screen.blit(battle1[schetpi1], (450, 300))
                schetpi1 = 0
        else:
            screen.blit(battle1[0], (450, 300))
        pygame.display.update()
        mainClock.tick(10)
        schetpi += 1

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:
        screen.fill((pygame.Color('Black')))
        screen.blit(background, (0, 0))
        draw_text('главное меню', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 20, 20)
        button_1 = pygame.Rect(94, 200, 395, 90)
        button_2 = pygame.Rect(94, 350, 395, 90)
        button_3 = pygame.Rect(94, 500, 395, 90)

        mx, my = pygame.mouse.get_pos()

        screen.blit(but, (90, 195))
        screen.blit(but, (90, 345))
        screen.blit(but, (90, 495))

        if button_1.collidepoint((mx, my)):
            screen.blit(but1, (90, 195))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ACT1()
                    pygame.quit()
        if button_2.collidepoint((mx, my)):
            screen.blit(but1, (90, 345))
        draw_text('начать игру', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 120, 224)
        draw_text('продолжить игру', pygame.font.Font('20031 (1).otf', 38), (255, 255, 255), screen, 105, 376)
        draw_text('настройки', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 130, 520)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(IMAGE, mouse_pos)
        pygame.display.flip()

        pygame.display.update()
        mainClock.tick(60)


pygame.mouse.set_visible(False)
a, b = 1600, 900
size = width, height = a, b
screen = pygame.display.set_mode(size)
mainClock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)

click = False
background = pygame.image.load('фон3.png')

but = pygame.transform.scale(pygame.image.load('кнопка.png').convert_alpha(), (400, 100))
but1 = pygame.transform.scale(pygame.image.load('кнопка1.png').convert_alpha(), (400, 100))
#PREVIEW.p()
main_menu()
