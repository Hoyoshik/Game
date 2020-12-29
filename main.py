import sys

import pygame
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

import PREVIEW

pygame.mouse.set_visible(False)
PREVIEW.p()

a, b = 1600, 900
size = width, height = a, b
screen = pygame.display.set_mode(size)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.startt)

    def startt(self):
        self.close()

        class ACT1:
            if __name__ == '__main__':
                pygame.init()
                screen = pygame.display.set_mode(size)
                pygame.display.flip()
                running = True
                pygame.mouse.set_visible(False)
                IMAGE = pygame.image.load('курсор2.png')
                playerR = pygame.image.load('персонаж.png')
                playerL = pygame.image.load('персонаж2.png')
                d = pygame.image.load('0.png')
                background = pygame.image.load('фон3.png')
                background_x = 0
                dedx = 2000
                player = playerR
                playerDED = pygame.image.load('Гробовщик.png')
                x = 20
                y = 0
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

                while running:
                    player = playerR
                    clock.tick(120)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                        elif pygame.mouse.get_focused():
                            if event.type == pygame.MOUSEMOTION:
                                mouse_pos = pygame.mouse.get_pos()
                                screen.blit(IMAGE, mouse_pos)
                                pygame.display.flip()
                                mouse_pos1 = mouse_pos
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
                    elif move[pygame.K_RIGHT] and x >= 1250 and background_x != -1300:
                        background_x -= speed
                        dedx -= speed
                        player = all_imgs2[c1]
                        c1 += 1
                    elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                        background_x += speed
                        dedx += speed
                    c += 1
                    if c == 8:
                        c = 0
                    if c1 == 13:
                        c1 = 0
                    screen.blit(background, (background_x, y))
                    screen.blit(player, (x, y))
                    screen.blit(playerDED, (dedx, y))
                    screen.blit(all_imgs[c], (background_x, y))
                    pygame.display.update()
                pygame.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
