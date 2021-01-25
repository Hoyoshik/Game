import pygame
import sys
import os
from pygame.locals import *

import PREVIEW
import бумажечки

class Person:
    def __init__(self, x, minX, maxX, speed, playerR, playerL, img_names2, img_names3):
        self.x = x
        self.minX = minX
        self.maxX = maxX
        self.speed = speed
        self.rotation = False  # False - right; True - left

        self.rightMoveSprites = list()
        self.currentRightSprite = 0
        self.leftMoveSprites = list()
        self.currentLeftSprite = 0

        self.defaultRSprite = pygame.image.load(playerR).convert_alpha()
        self.defaultLSprite = pygame.image.load(playerL).convert_alpha()

        self.PlayerSprite = self.defaultRSprite

        for img2 in img_names2:
            self.rightMoveSprites.append(pygame.image.load(img2).convert_alpha())
        for img3 in img_names3:
            self.leftMoveSprites.append(pygame.image.load(img3).convert_alpha())

    def stepRight(self):
        self.rotation = False
        self.x = min(self.x + self.speed, self.maxX)
        self.PlayerSprite = self.rightMoveSprites[self.currentRightSprite]
        self.currentRightSprite = (self.currentRightSprite + 1) % len(self.rightMoveSprites)
        self.currentLeftSprite = 0

    def stepLeft(self):
        self.rotation = True
        self.x = max(self.x - self.speed, self.minX)
        self.PlayerSprite = self.leftMoveSprites[self.currentLeftSprite]
        self.currentLeftSprite = (self.currentLeftSprite + 1) % len(self.leftMoveSprites)
        self.currentRightSprite = 0

    def setDefaultSprite(self):
        if self.rotation:
            self.PlayerSprite = self.defaultLSprite
        else:
            self.PlayerSprite = self.defaultRSprite

    def getPlayerSprite(self):
        return self.PlayerSprite

    def getX(self):
        return self.x

    def isPlayMusic(self):
        return ((self.currentRightSprite == 1 or self.currentRightSprite == 6) or (
                self.currentLeftSprite == 1 or self.currentLeftSprite == 6)) and \
               (self.PlayerSprite != self.defaultRSprite and self.PlayerSprite != self.defaultLSprite)


def ACT1_REFORGE():
    pygame.init()
    pygame.mixer.music.load('Звуки и музыка\дождь.mp3')
    s = pygame.mixer.Sound('Звуки и музыка\шаг.ogg')
    s.set_volume(0.1)
    pressspace = pygame.image.load('Спрайты\Элементы интерфейса\НАЖМИТЕ ПРОБЕЛ.png').convert_alpha()
    background = pygame.image.load('фон3.png').convert_alpha()
    key = pygame.transform.smoothscale(pygame.image.load('Ключ.png').convert_alpha(), (50, 50))
    img_names = ('0.png', '1.png', '2.png',
                 '3.png', '4.png', '5.png', '6.png', '7.png')

    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        background_x = 0

        keyx = 600
        keyshow = False

        inventarkey = False

        textstart = True

        speed = 20
        c = 0

        mainPerson = Person(20,  # начальная координата x
                            20,  # минимальное значение x
                            1250,  # максимальное значение x
                            speed,  # скорость изменения x
                            'Спрайты\Персонаж\персонаж.png',
                            # путь к изображению стоящего персонажа вмторящего в правую сторону
                            'Спрайты\Персонаж\персонаж2.png',
                            # путь к изображению стоящего персонажа вмторящего в левую сторону
                            ('Спрайты\Персонаж\\right\пр1.png', 'Спрайты\Персонаж\\right\пр2.png',
                             'Спрайты\Персонаж\\right\пр3.png', 'Спрайты\Персонаж\\right\пр4.png',
                             'Спрайты\Персонаж\\right\пр5.png', 'Спрайты\Персонаж\\right\пр6.png',
                             'Спрайты\Персонаж\\right\пр7.png', 'Спрайты\Персонаж\\right\пр8.png',
                             'Спрайты\Персонаж\\right\пр9.png', 'Спрайты\Персонаж\\right\пр10.png',
                             'Спрайты\Персонаж\\right\пр11.png', 'Спрайты\Персонаж\\right\пр12.png'),
                            # изображения для анимации ходьбы в правую сторону
                            ("Спрайты\Персонаж\\left\ле1.png", "Спрайты\Персонаж\\left\ле2.png",
                             "Спрайты\Персонаж\\left\ле3.png", "Спрайты\Персонаж\\left\ле4.png",
                             "Спрайты\Персонаж\\left\ле5.png", "Спрайты\Персонаж\\left\ле6.png",
                             "Спрайты\Персонаж\\left\ле7.png", "Спрайты\Персонаж\\left\ле8.png",
                             "Спрайты\Персонаж\\left\ле9.png", "Спрайты\Персонаж\\left\ле10.png",
                             "Спрайты\Персонаж\\left\ле11.png", "Спрайты\Персонаж\\left\ле12.png")
                            # изображения для анимации ходьбы в левую сторону
                            )  # главный герой

        dedPerson = Person(2000,  # начальная координата x
                           -10000,  # минимальное значение x
                           10000,  # максимальное значение x
                           speed,  # скорость изменения x
                           'Спрайты\Гробовщик\Гробовщик.png',
                           # путь к изображению стоящего персонажа вмторящего в правую сторону
                           'Спрайты\Гробовщик\ГробовщикЛ.png',
                           # путь к изображению стоящего персонажа вмторящего в левую сторону
                           ('Спрайты\Гробовщик\Гробовщик.png',),  # изображения для анимации ходьбы в правую сторону
                           ("Спрайты\гробовщик\гр1.png", "Спрайты\гробовщик\гр2.png", "Спрайты\гробовщик\гр3.png",
                            "Спрайты\гробовщик\гр4.png",
                            "Спрайты\гробовщик\гр5.png", "Спрайты\гробовщик\гр6.png", "Спрайты\гробовщик\гр7.png",
                            "Спрайты\гробовщик\гр8.png",
                            "Спрайты\гробовщик\гр9.png", "Спрайты\гробовщик\гр10.png", "Спрайты\гробовщик\гр11.png",
                            "Спрайты\гробовщик\гр12.png")
                           # изображения для анимации ходьбы в левую сторону
                           )  # дед

        all_imgs = list()
        all_imgsGr = list()

        for img in img_names:
            fullname = os.path.join('Спрайты\Дождь', img)
            all_imgs.append(pygame.image.load(fullname).convert_alpha())
        clock = pygame.time.Clock()
        running = True
        grDead = False
        H = 0
        schetpi = 0
        pygame.mixer.music.play(-1)
        g = True
        image = pygame.image.load('черрный фон.jpg')
        x1 = 0
        x2 = 0
        PREVIEW.act1preview()
        while running:
            mainPerson.setDefaultSprite()
            clock.tick(12)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_menu()
                else:
                    pygame.display.flip()
            move = pygame.key.get_pressed()
            y = 0
            x = mainPerson.getX()
            if x != 640 or H == 1:
                if move[pygame.K_LEFT] and x > 20:
                    mainPerson.stepLeft()
                elif move[pygame.K_RIGHT] and x < 1250:
                    mainPerson.stepRight()
                elif move[pygame.K_RIGHT] and x >= 1250 and background_x != -1300:
                    background_x -= speed
                    keyx -= speed
                    mainPerson.stepRight()
                elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                    background_x += speed
                    keyx += speed
                    mainPerson.stepLeft()
            elif schetpi > 0:
                grDead = True
                keyshow = True

            dedx = dedPerson.getX()

            if grDead:
                dedPerson.stepLeft()
                if dedx < -1000:
                    H = 1
                    grDead = False

            if move[pygame.K_SPACE] and x - background_x > 2150 and inventarkey:
                ACT1_5()
                pygame.quit()

            elif x == 640 and H != 1 and schetpi == 0:
                if dedx != 700:
                    dedPerson.stepLeft()
                else:
                    dedPerson.setDefaultSprite()
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    schetpi += 1
                    while restart:
                        BATTLE_DED()


            c += 1
            if c == 8:
                c = 0
            if mainPerson.isPlayMusic():
                s.play()

            player = mainPerson.getPlayerSprite()
            playerDED = dedPerson.getPlayerSprite()

            screen.blit(background, (background_x, y))
            if keyshow:
                screen.blit(key, (keyx, 800))
            screen.blit(player, (x, 300))

            screen.blit(playerDED, (dedx, y))

            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            screen.blit(all_imgs[c], (background_x, y))

            # маски
            mask = player.get_rect()
            mask.x = x
            mask.y = 300

            maskkey = key.get_rect()
            maskkey.x = keyx
            maskkey.y = 800

            if move[pygame.K_SPACE] and keyshow and mask.colliderect(maskkey):
                inventarkey = True
                keyshow = False

            if textstart:
                draw_text('попадите в дом', pygame.font.Font('20031 (1).otf', 20), (255, 255, 255), screen, 20, 20)
            if mask.colliderect(maskkey) and H == 1 and keyshow:
                screen.blit(pressspace, (0, 0))
            if x - background_x > 2150 and inventarkey:
                screen.blit(pressspace, (0, 0))

            if x1 != 920:
                x1 += 30
                x2 -= 30
                screen.blit(image, (x1, 0))
                screen.blit(image, (x2, 0))
            pygame.display.update()
        pygame.quit()

spavn = 0
coat = 0
document = 0

def ACT1_5():
    global coat, uslovie, document
    if document == 1:
        print(101)
    pygame.init()
    pygame.mixer.music.load('Звуки и музыка\дождьдом.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    s = pygame.mixer.Sound('Звуки и музыка\шаг.ogg')
    s.set_volume(0.1)
    pressspace = pygame.image.load('Спрайты\Элементы интерфейса\НАЖМИТЕ ПРОБЕЛ.png').convert_alpha()
    background = pygame.image.load('фон2.png').convert_alpha()
    backgroundwithout = pygame.image.load('фон22.png').convert_alpha()
    table = pygame.Rect(750, 500, 300, 250)
    seif = pygame.Rect(1280, 400, 150, 200)
    paltishko = pygame.Rect(265, 200, 150, 600)
    door = pygame.Rect(60, 300, 220, 400)
    pal = True
    uslovie = 0
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        background_x = 0
        speed = 20
        if spavn == 0:
            mainPerson = Person(20,  # начальная координата x
                                20,  # минимальное значение x
                                1250,  # максимальное значение x
                                speed,  # скорость изменения x
                                'Спрайты\Персонаж\персонаж.png',
                                # путь к изображению стоящего персонажа вмторящего в правую сторону
                                'Спрайты\Персонаж\персонаж2.png',
                                # путь к изображению стоящего персонажа вмторящего в левую сторону
                                ('Спрайты\Персонаж\\right\пр1.png', 'Спрайты\Персонаж\\right\пр2.png',
                                 'Спрайты\Персонаж\\right\пр3.png', 'Спрайты\Персонаж\\right\пр4.png',
                                 'Спрайты\Персонаж\\right\пр5.png', 'Спрайты\Персонаж\\right\пр6.png',
                                 'Спрайты\Персонаж\\right\пр7.png', 'Спрайты\Персонаж\\right\пр8.png',
                                 'Спрайты\Персонаж\\right\пр9.png', 'Спрайты\Персонаж\\right\пр10.png',
                                 'Спрайты\Персонаж\\right\пр11.png', 'Спрайты\Персонаж\\right\пр12.png'),
                                # изображения для анимации ходьбы в правую сторону
                                ("Спрайты\Персонаж\\left\ле1.png", "Спрайты\Персонаж\\left\ле2.png",
                                 "Спрайты\Персонаж\\left\ле3.png", "Спрайты\Персонаж\\left\ле4.png",
                                 "Спрайты\Персонаж\\left\ле5.png", "Спрайты\Персонаж\\left\ле6.png",
                                 "Спрайты\Персонаж\\left\ле7.png", "Спрайты\Персонаж\\left\ле8.png",
                                 "Спрайты\Персонаж\\left\ле9.png", "Спрайты\Персонаж\\left\ле10.png",
                                 "Спрайты\Персонаж\\left\ле11.png", "Спрайты\Персонаж\\left\ле12.png")
                                # изображения для анимации ходьбы в левую сторону
                                )  # главный герой
        if spavn > 0:
            print(1)
            mainPerson = Person(1200,  # начальная координата x
                                20,  # минимальное значение x
                                1250,  # максимальное значение x
                                speed,  # скорость изменения x
                                'Спрайты\Персонаж\персонаж.png',
                                # путь к изображению стоящего персонажа вмторящего в правую сторону
                                'Спрайты\Персонаж\персонаж2.png',
                                # путь к изображению стоящего персонажа вмторящего в левую сторону
                                ('Спрайты\Персонаж\\right\пр1.png', 'Спрайты\Персонаж\\right\пр2.png',
                                 'Спрайты\Персонаж\\right\пр3.png', 'Спрайты\Персонаж\\right\пр4.png',
                                 'Спрайты\Персонаж\\right\пр5.png', 'Спрайты\Персонаж\\right\пр6.png',
                                 'Спрайты\Персонаж\\right\пр7.png', 'Спрайты\Персонаж\\right\пр8.png',
                                 'Спрайты\Персонаж\\right\пр9.png', 'Спрайты\Персонаж\\right\пр10.png',
                                 'Спрайты\Персонаж\\right\пр11.png', 'Спрайты\Персонаж\\right\пр12.png'),
                                # изображения для анимации ходьбы в правую сторону
                                ("Спрайты\Персонаж\\left\ле1.png", "Спрайты\Персонаж\\left\ле2.png",
                                 "Спрайты\Персонаж\\left\ле3.png", "Спрайты\Персонаж\\left\ле4.png",
                                 "Спрайты\Персонаж\\left\ле5.png", "Спрайты\Персонаж\\left\ле6.png",
                                 "Спрайты\Персонаж\\left\ле7.png", "Спрайты\Персонаж\\left\ле8.png",
                                 "Спрайты\Персонаж\\left\ле9.png", "Спрайты\Персонаж\\left\ле10.png",
                                 "Спрайты\Персонаж\\left\ле11.png", "Спрайты\Персонаж\\left\ле12.png")
                                # изображения для анимации ходьбы в левую сторону
                                )  # главный герой
        clock = pygame.time.Clock()
        running = True
        pygame.mixer.music.play(-1)
        while running:
            mainPerson.setDefaultSprite()
            clock.tick(12)
            move = pygame.key.get_pressed()
            y = 0
            x = mainPerson.getX()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                    main_menu()
                else:
                    pygame.display.flip()
            if move[pygame.K_LEFT] and x > 20:
                mainPerson.stepLeft()
            elif move[pygame.K_RIGHT] and x < 1250:
                mainPerson.stepRight()
            player = mainPerson.getPlayerSprite()
            if mainPerson.isPlayMusic():
                s.play()
            if move[pygame.K_SPACE] and mask.colliderect(paltishko):
                coat = 1
            if coat == 1:
                pal = False
            if pal == False:
                screen.blit(backgroundwithout, (background_x, y))
            if pal == True:
                screen.blit(background, (background_x, y))
            screen.blit(player, (x, 300))
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            # маски
            mask = player.get_rect()
            mask.x = x
            mask.y = 300
            if move[pygame.K_SPACE] and mask.colliderect(table):
                бумажечки.paper()
            if move[pygame.K_SPACE] and mask.colliderect(seif):
                saif()
            if move[pygame.K_SPACE] and mask.colliderect(door) and uslovie == 2:
                ACT1_5_2()
                pygame.quit()
            if coat == 1:
                uslovie = 1
            if document == 1:
                uslovie = 2
            #pygame.draw.rect(screen, pygame.Color('red'), seif)
            #pygame.draw.rect(screen, pygame.Color('red'), paltishko)
            #pygame.draw.rect(screen, pygame.Color('red'), door)
            #pygame.draw.rect(screen, pygame.Color('red'), table)
            #pygame.draw.rect(screen, pygame.Color('blue'), mask)
            pygame.display.update()
        pygame.quit()


def ACT1_5_2():
    pygame.init()
    pygame.mixer.music.load('Звуки и музыка\дождьдом.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    s = pygame.mixer.Sound('Звуки и музыка\шаг.ogg')
    s.set_volume(0.1)
    background = pygame.image.load('фон4.png').convert_alpha()
    bl = False
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        background_x = 0
        textstart = True
        speed = 20
        mainPerson = Person(20,
                             20,
                             1250,
                             speed,
                             'Спрайты\Персонаж\пальтопр.png',
                             'Спрайты\Персонаж\пальтоле.png',
                             # путь к изображению стоящего персонажа вмторящего в левую сторону
                             ('Спрайты\Персонаж\\coatright\пальто1пр.png', 'Спрайты\Персонаж\\coatright\пальто2пр.png',
                              'Спрайты\Персонаж\\coatright\пальто3пр.png', 'Спрайты\Персонаж\\coatright\пальто4пр.png',
                              'Спрайты\Персонаж\\coatright\пальто5пр.png', 'Спрайты\Персонаж\\coatright\пальто6пр.png',
                              'Спрайты\Персонаж\\coatright\пальто7пр.png', 'Спрайты\Персонаж\\coatright\пальто8пр.png',
                              'Спрайты\Персонаж\\coatright\пальто9пр.png', 'Спрайты\Персонаж\\coatright\пальто10пр.png',
                              'Спрайты\Персонаж\\coatright\пальто11пр.png'),
                             # изображения для анимации ходьбы в правую сторону
                             ('Спрайты\Персонаж\\coatleft\пальто1ле.png', 'Спрайты\Персонаж\\coatleft\пальто2ле.png',
                              'Спрайты\Персонаж\\coatleft\пальто3ле.png', 'Спрайты\Персонаж\\coatleft\пальто4ле.png',
                              'Спрайты\Персонаж\\coatleft\пальто5ле.png', 'Спрайты\Персонаж\\coatleft\пальто6ле.png',
                              'Спрайты\Персонаж\\coatleft\пальто7ле.png', 'Спрайты\Персонаж\\coatleft\пальто8ле.png',
                              'Спрайты\Персонаж\\coatleft\пальто9ле.png', 'Спрайты\Персонаж\\coatleft\пальто10ле.png',
                              'Спрайты\Персонаж\\coatleft\пальто11ле.png')
                             # изображения для анимации ходьбы в левую сторону
                             )  # главный герой
        clock = pygame.time.Clock()
        running = True
        pygame.mixer.music.play(-1)
        g = True
        while running:
            mainPerson.setDefaultSprite()
            clock.tick(12)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_menu()
                else:
                    pygame.display.flip()

            move = pygame.key.get_pressed()
            y = 0
            x = mainPerson.getX()
            if move[pygame.K_LEFT] and x > 20:
                mainPerson.stepLeft()
            elif move[pygame.K_RIGHT] and x < 1250:
                mainPerson.stepRight()
            elif move[pygame.K_RIGHT] and x >= 1250 and background_x != -1300:
                background_x -= speed
                mainPerson.stepRight()
            elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                background_x += speed
                mainPerson.stepLeft()
            player = mainPerson.getPlayerSprite()
            if mainPerson.isPlayMusic():
                s.play()
            if x == 1250:
                main_menu()
            screen.blit(background, (background_x, y))
            screen.blit(player, (x, 300))
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            # маски
            mask = player.get_rect()
            mask.x = x
            mask.y = 300

            pygame.display.update()
        pygame.quit()

IMAGE = pygame.image.load('курсор2.png')


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_textConsolka(text, font, color, surface, x, y):
    color = pygame.Color(140, 0, 15)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    pygame.mixer.music.load('МЕЛОДИЯ.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    # s = pygame.mixer.Sound('звук щелчка.ogg')

    m = 0
    ty = pygame.image.load('1туман.png').convert_alpha()
    tyx = 2000
    menusp = (
        'меню.png', 'меню2.png', 'меню4.png', 'меню5.png', 'меню6.png', 'меню7.png', 'меню8.png')
    menu = list()
    for i in menusp:
        menu.append(pygame.image.load(i).convert_alpha())
    image = pygame.image.load('черрный фон.jpg')

    while True:
        if tyx == -6400:
            tyx = 2000
        screen.fill((pygame.Color('Black')))
        screen.blit(background, (0, 0))
        draw_text('главное меню', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 20, 20)
        button_1 = pygame.Rect(94, 200, 395, 90)
        button_2 = pygame.Rect(94, 350, 395, 90)
        button_3 = pygame.Rect(94, 500, 395, 90)

        mx, my = pygame.mouse.get_pos()
        screen.blit(menu[m], (0, 0))
        screen.blit(ty, (tyx, 0))

        tyx -= 100

        screen.blit(but, (90, 195))
        screen.blit(but, (90, 345))
        screen.blit(but, (90, 495))

        draw_text('начать игру', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 120, 224)
        draw_text('продолжить игру', pygame.font.Font('20031 (1).otf', 38), (255, 255, 255), screen, 105, 376)
        draw_text('настройки', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 130, 520)

        x = -1600
        x1 = 1600
        if button_1.collidepoint((mx, my)):
            screen.blit(but1, (90, 195))
            draw_text('начать игру', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 120, 224)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # s.play()
                    g = True

                    while g:
                        if x != 920:
                            x += 30
                            x1 -= 30
                            screen.blit(image, (x, 0))
                            screen.blit(image, (x1, 0))
                            pygame.display.flip()
                            pygame.display.update()
                            mainClock.tick(24)
                        else:
                            g = False
                    pygame.mixer.music.stop()
                    ACT1_REFORGE()
                    pygame.quit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        m += 1
        if m == 7:
            m = 0
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(IMAGE, mouse_pos)
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(24)


def BATTLE_DED():
    global chis, restart
    back = pygame.image.load('фонбитва.png').convert_alpha()
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
                        restart = False
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
                screen.fill((0, 0, 0))
                PREVIEW.death()
                br = False
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
        mainClock.tick(24)
        schetpi += 1
    chis = 1

def saif():
    global spavn
    spavn += 1
    backgroung = pygame.image.load('сейф.png').convert_alpha()
    if __name__ == '__main__':
        pygame.display.flip()
        clock = pygame.time.Clock()
        running = True
        maskConsolka = pygame.Rect(630, 396, 130, 130)
        while running:
            clock.tick(30)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ACT1_5()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if maskConsolka.collidepoint(mx, my):
                        consolka()
                else:
                    pygame.display.flip()
            screen.blit(backgroung, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            pygame.display.flip()
            pygame.display.update()
            # pygame.draw.rect(screen, pygame.Color('blue'), maskConsolka)
        pygame.quit()


def consolka():
    global spavn
    spavn += 1
    background = pygame.image.load('черрный фон.jpg').convert_alpha()
    maskcon1 = pygame.Rect(550, 250, 140, 140)
    maskcon2 = pygame.Rect(692, 250, 140, 140)
    maskcon3 = pygame.Rect(834, 250, 140, 140)
    maskcon4 = pygame.Rect(550, 392, 140, 140)
    maskcon5 = pygame.Rect(692, 392, 140, 140)
    maskcon6 = pygame.Rect(834, 392, 140, 140)
    maskcon7 = pygame.Rect(550, 534, 140, 140)
    maskcon8 = pygame.Rect(692, 534, 140, 140)
    maskcon9 = pygame.Rect(834, 534, 140, 140)
    maskconC = pygame.Rect(550, 676, 140, 140)
    maskcon0 = pygame.Rect(692, 676, 140, 140)
    maskconEN = pygame.Rect(834, 676, 140, 140)
    consol1 = '1'
    consol2 = '2'
    consol3 = '3'
    consol4 = '4'
    consol5 = '5'
    consol6 = '6'
    consol7 = '7'
    consol8 = '8'
    consol9 = '9'
    consolC = 'C'
    consol0 = '0'
    consolEN = 'ENTER'
    simvol = 0
    consolError = 'ERROR!'
    uslovie = False
    if __name__ == '__main__':
        pygame.display.flip()
        clock = pygame.time.Clock()
        running = True
        consol = '000000'
        kod = '231426'
        while running:
            clock.tick(30)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ACT1_5()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if maskcon1.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol1
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon2.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol2
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon3.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol3
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon4.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol4
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon5.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol5
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon6.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol6
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon7.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol7
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon8.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol8
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon9.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol9
                        consol = ''.join(edit)
                        simvol += 1
                    if maskcon0.collidepoint(mx, my) and simvol < 6:
                        edit = list(consol)
                        edit[simvol] = consol0
                        consol = ''.join(edit)
                        simvol += 1
                    if maskconC.collidepoint(mx, my) and simvol < 6 and consol != consolError:
                        consol = '000000'
                        simvol = 0
                    if maskconC.collidepoint(mx, my) and consol == consolError:
                        consol = '000000'
                        simvol = 0
                    if maskconEN.collidepoint(mx, my):
                        if consol == kod:
                            edit = 'OPEN!'
                            consol = ''.join(edit)
                            uslovie == True
                            seifopen()
                        else:
                            consol = consolError
                            simvol = 6
                else:
                    pygame.display.flip()
            screen.blit(background, (0, 0))
            draw_textConsolka(consol1, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 550,
                              220)
            draw_textConsolka(consol2, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 700,
                              220)
            draw_textConsolka(consol3, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 850,
                              220)
            draw_textConsolka(consol4, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 550,
                              360)
            draw_textConsolka(consol5, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 700,
                              360)
            draw_textConsolka(consol6, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 850,
                              360)
            draw_textConsolka(consol7, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 550,
                              500)
            draw_textConsolka(consol8, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 700,
                              500)
            draw_textConsolka(consol9, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 200), (255, 405, 255), screen, 850,
                              500)
            draw_textConsolka(consolC, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 135), (255, 405, 255), screen, 570,
                              650)
            draw_textConsolka(consol0, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 135), (255, 405, 255), screen, 715,
                              650)
            draw_textConsolka(consolEN, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 40), (255, 405, 255), screen, 840,
                              700)
            draw_textConsolka(consol, pygame.font.Font('7fonts.ru_DS-DIGI.TTF', 135), (255, 405, 255), screen, 568,
                              120)
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            pygame.display.flip()
            pygame.display.update()
        pygame.quit()

def seifopen():
    global spavn, document
    spavn += 1
    seifopen.counter = 1
    backgroung = pygame.image.load('сейф внутри.png').convert_alpha()
    backgroungwithout = pygame.image.load('сейф внутри2.png').convert_alpha()
    if __name__ == '__main__':
        pygame.display.flip()
        clock = pygame.time.Clock()
        running = True
        maskDoc = pygame.Rect(470, 520, 555, 130)
        documents = False
        while running:
            clock.tick(30)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if maskDoc.collidepoint(mx, my):
                        documents = True
                else:
                    pygame.display.flip()
                if event.type == QUIT:
                    ACT1_5()
            if documents == False:
                screen.blit(backgroung, (0, 0))
            if documents == True:
                screen.blit(backgroungwithout, (0, 0))
                document = 1
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            #pygame.draw.rect(screen, pygame.Color('blue'), maskDoc)

pygame.mixer.init()
pygame.mouse.set_visible(False)
a, b = 1600, 900
size = width, height = a, b
screen = pygame.display.set_mode(size)
mainClock = pygame.time.Clock()

restart = True

font = pygame.font.SysFont(None, 20)

click = False
background = pygame.image.load('фон3.png').convert_alpha()

but = pygame.transform.scale(pygame.image.load('кнопка.png').convert_alpha(), (400, 100))
but1 = pygame.transform.scale(pygame.image.load('кнопка1.png').convert_alpha(), (400, 100))
#PREVIEW.p()
main_menu()
#ACT1_REFORGE()
#BATTLE_DED()