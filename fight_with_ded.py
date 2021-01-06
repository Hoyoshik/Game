import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1600, 900), 0, 32)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def fight_with_ded():
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
    g1 = 0
    c = False
    c1 = False
    schetpi1 = 0
    schetpi = 0
    while True:
        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        screen.blit(pygame.transform.scale(grob1[g], (400, 50)), (300, 250))
        screen.blit(pygame.transform.scale(grob2[g1], (400, 50)), (840, 250))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and c != True:
                    c = True
                    if g1 == 4:
                        pass
                    else:
                         g1 += 1

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
fight_with_ded()