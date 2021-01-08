import pygame, sys
from pygame.locals import *
import PREVIEW


def ACT1():
    playerR = pygame.image.load('персонаж.png').convert_alpha()
    playerL = pygame.image.load('персонаж2.png').convert_alpha()
    background = pygame.image.load('фон3.png').convert_alpha()
    playerDED = pygame.image.load('ГробовщикЛ.png').convert_alpha()
    key = pygame.transform.smoothscale(pygame.image.load('Ключ.png').convert_alpha(), (50, 50))
    img_names = ('0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png')
    img_names2 = (
        'кл1пр.png', 'кл2пр.png', 'кл3пр.png', 'кл4пр.png', 'кл5пр.png', 'кл6пр.png', 'кл7пр.png',
        'кл8пр.png',
        'кл9пр.png', 'кл10пр.png', 'кл11пр.png', 'кл12пр.png', 'кл13пр.png')

    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        background_x = 0
        dedx = 2000

        keyx = 2000
        keyshow = False

        inventarkey = False

        textstart = True

        x = 20
        speed = 20
        c = 0
        c1 = 0
        all_imgs = list()
        all_imgs2 = list()
        for img in img_names:
            all_imgs.append(pygame.image.load(img).convert_alpha())
        for img2 in img_names2:
            all_imgs2.append(pygame.image.load(img2).convert_alpha())
        clock = pygame.time.Clock()
        running = True
        grDead = False
        hp1ded = False
        flag = False
        mainloop = True
        chis = 0
        schetpi = 0
        while running:
            player = playerR
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_menu()
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
                    keyx -= speed
                    player = all_imgs2[c1]
                    c1 += 1
                elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                    background_x += speed
                    dedx += speed
                    keyx += speed
            elif x == 1260 and schetpi < 1:
                screen.fill((0, 0, 0))
                pygame.display.update()
                schetpi += 1
                BATTLE_DED()
            elif schetpi > 0:
                grDead = True
                keyshow = True
            if grDead == True:
                dedx -= speed

            if move[pygame.K_SPACE] and x < 1260 and keyshow:
                inventarkey = True
                keyshow = False
                textstart = False

            if move[pygame.K_SPACE] and x == 1260 and dedx < 100 and inventarkey == True:
                ACT1_5()
                pygame.quit()

            c += 1
            if c == 8:
                c = 0
            if c1 == 13:
                c1 = 0
            screen.blit(background, (background_x, y))
            if keyshow:
                screen.blit(key, (keyx, 800))
            screen.blit(player, (x, y))
            screen.blit(playerDED, (dedx, y))
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            screen.blit(all_imgs[c], (background_x, y))
            if textstart:
                draw_text('попадите в Дом', pygame.font.Font('20031 (1).otf', 20), (255, 255, 255), screen, 20, 20)
            if x == 1260 and inventarkey:
                draw_text('откройте дверь', pygame.font.Font('20031 (1).otf', 20), (255, 255, 255), screen, 20, 20)
            pygame.display.update()
            print(x)
        pygame.quit()


def ACT1_5():
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        playerR = pygame.image.load('персонаж.png').convert_alpha()
        playerL = pygame.image.load('персонаж2.png').convert_alpha()
        background = pygame.image.load('фон2.png').convert_alpha()
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
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(background, (background_x, y))
            screen.blit(player, (x, y))
            screen.blit(IMAGE, mouse_pos)
            pygame.display.update()
        pygame.quit()


IMAGE = pygame.image.load('курсор2.png')


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    pygame.mixer.init()
    pygame.mixer.music.load('МЕЛОДИЯ.mp3')
    pygame.mixer.music.play(-1)
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
                    pygame.mixer.music.stop()
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

def BATTLE_DED():
    global chis
    back = pygame.image.load('фон3.png').convert_alpha()
    ded1 = pygame.transform.smoothscale(pygame.image.load('битваГ1.png').convert_alpha(), (600, 600))
    ded2 = pygame.transform.smoothscale(pygame.image.load('битваГ2.png').convert_alpha(), (600, 600))
    ded3 = pygame.transform.smoothscale(pygame.image.load('битваГ3.png').convert_alpha(), (600, 600))
    deda = pygame.transform.smoothscale(pygame.image.load('битваГ4.png').convert_alpha(), (600, 600))
    deda2 = pygame.transform.smoothscale(pygame.image.load('битваГ5.png').convert_alpha(), (600, 600))
    dedl = pygame.transform.smoothscale(pygame.image.load('битваГ6.png').convert_alpha(), (600, 600))
    dedl2 = pygame.transform.smoothscale(pygame.image.load('битваГ7.png').convert_alpha(), (600, 600))
    dedl3 = pygame.transform.smoothscale(pygame.image.load('битваГ8.png').convert_alpha(), (600, 600))
    dedl4 = pygame.transform.smoothscale(pygame.image.load('битваГ9.png').convert_alpha(), (600, 600))
    dedl5 = pygame.transform.smoothscale(pygame.image.load('битваГ10.png').convert_alpha(), (600, 600))
    p1 = pygame.transform.smoothscale(pygame.image.load('БитваП1.png').convert_alpha(), (600, 600))
    p2 = pygame.transform.smoothscale(pygame.image.load('БитваП2.png').convert_alpha(), (600, 600))
    p3 = pygame.transform.smoothscale(pygame.image.load('БитваП3.png').convert_alpha(), (600, 600))

    battle = list()
    battle.append(p1)
    battle.append(p2)
    battle.append(p3)

    battle1 = list()
    battle1.append(ded1)
    battle1.append(ded2)
    battle1.append(ded3)

    anim = list()
    anim.append(deda)
    anim.append(deda2)
    anim.append(dedl)

    battlelopata = list()
    battlelopata.append(dedl)
    battlelopata.append(dedl2)
    battlelopata.append(dedl3)
    battlelopata.append(dedl4)
    battlelopata.append(dedl5)

    grob = (
        'Полоска здоровья.png', 'Полоска здоровья1.png', 'Полоска здоровья2.png', 'Полоска здоровья3.png',
        'Полоска здоровья4.png', 'Полоска здоровья5.png', 'Полоска здоровья6.png', 'Полоска здоровья7.png',
        'Полоска здоровья8.png')
    playerFight = list()
    for img in grob:
        playerFight.append(pygame.image.load(img).convert_alpha())

    grobovshik = list()
    grob3 = (
        'Полоска здоровья.png', 'Полоска здоровья11.png', 'Полоска здоровья22.png',
        'Полоска здоровья33.png',
        'Полоска здоровья44.png')

    for mgi in grob3:
        grobovshik.append(pygame.image.load(mgi).convert_alpha())
    j = 0
    g = 0
    kadrplayer = 0
    c = False
    c1 = False
    schetpi1 = 0
    schetpi = 0
    br = True
    anima = False
    dedSt1 = True
    dead = True
    screen.fill((0, 0, 0))
    pygame.display.update()
    while br:
        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        screen.blit(pygame.transform.scale(playerFight[g], (400, 50)), (300, 250))
        screen.blit(pygame.transform.scale(grobovshik[kadrplayer], (400, 50)), (840, 250))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and c != True:
                    c = True
                    if kadrplayer == 4:
                        for i in range(1):
                            dedSt1 == False
                            dead == False
                            anima = True
                            br = False
                    else:
                        kadrplayer += 1
                if event.key == K_ESCAPE:
                    sys.exit()
        if anima:
            for i in range(2):
                screen.blit(anim[i], (450, 300))
                pygame.display.update()
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
                PREVIEW.death()
                break
            else:
                g += 1

        if c1 == True and anima == False:
            screen.blit(battle1[schetpi1], (450, 300))
            if schetpi1 != 2 and anima == False:
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
    chis = 1

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
# PREVIEW.p()
main_menu()