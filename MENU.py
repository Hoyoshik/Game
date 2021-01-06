import pygame, sys
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('МЕЛОДИЯ.mp3')
pygame.mixer.music.play(-1)

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1600, 900), 0, 32)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
background = pygame.image.load('фон3.png')


but = pygame.transform.scale(pygame.image.load('кнопка.png').convert_alpha(), (400, 100))
but1 = pygame.transform.scale(pygame.image.load('кнопка1.png').convert_alpha(), (400, 100))

def main_menu():
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_text('главное меню', pygame.font.Font('20031 (1).otf', 50) , (255, 255, 255), screen, 20, 20)
        button_1 = pygame.Rect(94, 200, 395, 90)
        button_2 = pygame.Rect(94, 350, 395, 90)
        button_3 = pygame.Rect(94, 500, 395, 90)

        mx, my = pygame.mouse.get_pos()

        screen.blit(but, (90, 195))
        screen.blit(but, (90, 345))
        screen.blit(but, (90, 495))


        if button_1.collidepoint((mx, my)):
            screen.blit(but1, (90, 195))
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            screen.blit(but1, (90, 345))
            if click:
                options()
        draw_text('начать игру', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 120, 224)
        draw_text('продолжить игру', pygame.font.Font('20031 (1).otf', 38), (255, 255, 255), screen, 105, 376)
        draw_text('настройки', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 130, 520)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()