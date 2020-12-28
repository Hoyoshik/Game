import pygame


a, b = 1600, 900
size = width, height = a, b
screen = pygame.display.set_mode(size)


class ACT1:
    if __name__ == '__main__':
        pygame.init()

        playerR = pygame.image.load('персонаж.png')
        playerL = pygame.image.load('персонаж2.png')
        background = pygame.image.load('фон3.png')
        background_x = 0
        dedx = 2000
        player = playerR

        playerDED = pygame.image.load('Гробовщик.png')

        x = 20
        y = 0
        speed = 100

        pygame.display.flip()
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill((0, 0, 0))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            move = pygame.key.get_pressed()
            y = 0
            if move[pygame.K_LEFT] and x > 20:
                x -= speed
                player = playerL
            elif move[pygame.K_RIGHT] and x <= 1250:
                x += speed
                player = playerR
            elif move[pygame.K_RIGHT] and x >= 1250 and background_x != -1300:
                background_x -= speed
                dedx -= speed
            elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                background_x += speed
                dedx += speed

            screen.blit(background, (background_x, y))
            screen.blit(player, (x, y))
            screen.blit(playerDED, (dedx, y))
            pygame.display.update()
        pygame.quit()