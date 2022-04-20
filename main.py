# Minefield v1.0
import random
import pygame
import sys

# pygame start
pygame.init()


# main loop
def main():
    # fps variable
    clock = pygame.time.Clock()

    # window specification
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Minefield')
    icon = pygame.image.load('gfiles/favicon.png')
    pygame.display.set_icon(icon)

    # Gif class
    class Gif(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.animation = False
            self.sprites = []
            self.sprites.append(pygame.image.load('gfiles/clap1.gif'))
            self.sprites.append(pygame.image.load('gfiles/clap2.gif'))
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]

            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]

        def switch(self):
            self.animation = True

        def update(self, speed):
            if self.animation:
                self.current_sprite += speed
                if int(self.current_sprite) >= len(self.sprites):
                    self.current_sprite = 0
                    self.animation = False

            self.image = self.sprites[int(self.current_sprite)]

    # class for interactive number grid
    class Option:
        hovered = False

        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)

        def set_rend(self):
            self.rend = game_font.render(self.text, True, self.get_color())

        def get_color(self):
            if self.hovered:
                return 71, 251, 148
            else:
                return 39, 111, 69

        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos

    game_font = pygame.font.SysFont('Courier', 24)

    options = [Option('00', (150, 75)), Option('01', (200, 75)),
               Option('02', (250, 75)), Option('03', (300, 75)), Option('04', (350, 75)),
               Option('05', (400, 75)), Option('06', (450, 75)), Option('07', (500, 75)),
               Option('08', (550, 75)), Option('09', (600, 75)), Option('10', (150, 125)), Option('11', (200, 125)),
               Option('12', (250, 125)), Option('13', (300, 125)), Option('14', (350, 125)),
               Option('15', (400, 125)), Option('16', (450, 125)), Option('17', (500, 125)),
               Option('18', (550, 125)), Option('19', (600, 125)), Option('20', (150, 175)), Option('21', (200, 175)),
               Option('22', (250, 175)), Option('23', (300, 175)), Option('24', (350, 175)),
               Option('25', (400, 175)), Option('26', (450, 175)), Option('27', (500, 175)),
               Option('28', (550, 175)), Option('29', (600, 175)), Option('30', (150, 225)), Option('31', (200, 225)),
               Option('32', (250, 225)), Option('33', (300, 225)), Option('34', (350, 225)),
               Option('35', (400, 225)), Option('36', (450, 225)), Option('37', (500, 225)),
               Option('38', (550, 225)), Option('39', (600, 225)), Option('40', (150, 275)), Option('41', (200, 275)),
               Option('42', (250, 275)), Option('43', (300, 275)), Option('44', (350, 275)),
               Option('45', (400, 275)), Option('46', (450, 275)), Option('47', (500, 275)),
               Option('48', (550, 275)), Option('49', (600, 275)), Option('50', (150, 325)), Option('51', (200, 325)),
               Option('52', (250, 325)), Option('53', (300, 325)), Option('54', (350, 325)),
               Option('55', (400, 325)), Option('56', (450, 325)), Option('57', (500, 325)),
               Option('58', (550, 325)), Option('59', (600, 325)), Option('60', (150, 375)), Option('61', (200, 375)),
               Option('62', (250, 375)), Option('63', (300, 375)), Option('64', (350, 375)),
               Option('65', (400, 375)), Option('66', (450, 375)), Option('67', (500, 375)),
               Option('68', (550, 375)), Option('69', (600, 375)), Option('70', (150, 425)), Option('71', (200, 425)),
               Option('72', (250, 425)), Option('73', (300, 425)), Option('74', (350, 425)),
               Option('75', (400, 425)), Option('76', (450, 425)), Option('77', (500, 425)),
               Option('78', (550, 425)), Option('79', (600, 425)), Option('80', (150, 475)), Option('81', (200, 475)),
               Option('82', (250, 475)), Option('83', (300, 475)), Option('84', (350, 475)),
               Option('85', (400, 475)), Option('86', (450, 475)), Option('87', (500, 475)),
               Option('88', (550, 475)), Option('89', (600, 475)), Option('90', (150, 525)), Option('91', (200, 525)),
               Option('92', (250, 525)), Option('93', (300, 525)), Option('94', (350, 525)),
               Option('95', (400, 525)), Option('96', (450, 525)), Option('97', (500, 525)),
               Option('98', (550, 525)), Option('99', (600, 525))]

    # random number from 0 to 99
    x = random.choice(options)
    print('random number = ' + str(options.index(x)))

    # menu loop
    def menu():
        # volume level
        pygame.mixer.music.unpause()
        volume = 0.3
        pygame.mixer.music.set_volume(volume)

        # starts starts playing soundtrack
        pygame.mixer.music.load('gfiles/Doom.wav')
        pygame.mixer.music.play(loops=999)

        # closing program using X or ESC and running loop
        running = True
        while running:
            screen.fill((0, 0, 0))

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.KEYDOWN:  # volume up using arrow up
                    if event.key == pygame.K_UP:
                        volume += 0.1
                        if volume >= 1:
                            volume = 1.0
                        pygame.mixer.music.set_volume(volume)
                if event.type == pygame.KEYDOWN:  # volume down using arrow down
                    if event.key == pygame.K_DOWN:
                        volume -= 0.1
                        if volume <= 0:
                            volume = 0.0
                        pygame.mixer.music.set_volume(volume)

            mx, my = pygame.mouse.get_pos()

            # invisible buttons
            button_1 = pygame.Rect(285, 285, 200, 45)  # (placement, size)
            button_2 = pygame.Rect(296, 340, 175, 45)
            button_3 = pygame.Rect(248, 395, 275, 45)
            pygame.draw.rect(screen, (0, 0, 0), button_1, 2)
            pygame.draw.rect(screen, (0, 0, 0), button_2, 2)
            pygame.draw.rect(screen, (0, 0, 0), button_3, 2)
            if button_1.collidepoint((mx, my)):
                if click:
                    normal_game()
            if button_2.collidepoint((mx, my)):
                if click:
                    hard_game()
            if button_3.collidepoint((mx, my)):
                if click:
                    nightmare_game()

            # background image
            bgimage_image = pygame.image.load('gfiles/stalker.jpg')
            screen.blit(bgimage_image, (0, 0))

            font2 = pygame.font.SysFont('Courier', 88, bold=False, italic=False)
            font3 = pygame.font.SysFont('Courier', 14)

            # text
            show_title = font2.render('MINEFIELD', True, (252, 238, 10))
            show_title2 = font2.render('MINEFIELD', True, (2, 215, 242))
            screen.blit(show_title2, (157, 111))
            screen.blit(show_title, (155, 110))
            show_volume = font3.render('volume: ' + str(round(volume, 1)), True, (255, 0, 60))  # volume level
            screen.blit(show_volume, (702, 580))

            # show_fps = font3.render('FPS ' + str(round(clock.get_fps())), True, (0, 0, 0))  # fps counter
            # screen.blit(show_fps, (735, 8))   # requires clock.tick(x)

            # reactive subtitles function
            def subtitles():
                button_x = 313
                button_y = 295
                button_x2 = 335
                button_y2 = 350
                button_x3 = 274
                button_y3 = 405
                normal_image = pygame.image.load('gfiles/normal.png')
                screen.blit(normal_image, (button_x, button_y))
                hard_image = pygame.image.load('gfiles/hard.png')
                screen.blit(hard_image, (button_x2, button_y2))
                nightmare_image = pygame.image.load('gfiles/nightmare.png')
                screen.blit(nightmare_image, (button_x3, button_y3))

                normal2_image = pygame.image.load('gfiles/normal2.png').convert_alpha()
                x_len = normal_image.get_width()
                y_len = normal_image.get_height()
                if mx > button_x and (mx < button_x + x_len):
                    x_inside = True
                else:
                    x_inside = False
                if my > button_y and (my < button_y + y_len):
                    y_inside = True
                else:
                    y_inside = False
                if x_inside and y_inside:
                    screen.blit(normal2_image, (button_x, button_y))

                hard2_image = pygame.image.load('gfiles/hard2.png').convert_alpha()
                x2_len = hard_image.get_width()
                y2_len = hard_image.get_height()
                if mx > button_x2 and (mx < button_x2 + x2_len):
                    x2_inside = True
                else:
                    x2_inside = False
                if my > button_y2 and (my < button_y2 + y2_len):
                    y2_inside = True
                else:
                    y2_inside = False
                if x2_inside and y2_inside:
                    screen.blit(hard2_image, (button_x2, button_y2))

                nightmare2_image = pygame.image.load('gfiles/nightmare2.png').convert_alpha()
                x3_len = nightmare_image.get_width()
                y3_len = nightmare_image.get_height()
                if mx > button_x3 and (mx < button_x3 + x3_len):
                    x3_inside = True
                else:
                    x3_inside = False
                if my > button_y3 and (my < button_y3 + y3_len):
                    y3_inside = True
                else:
                    y3_inside = False
                if x3_inside and y3_inside:
                    screen.blit(nightmare2_image, (button_x3, button_y3))

            subtitles()

            pygame.display.update()

    # one of game loops
    def normal_game():
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            pygame.mixer.music.pause()  # stops the soundtrack
            ten_hearts = pygame.image.load('gfiles/10_normal.png')
            screen.blit(ten_hearts, (8, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.mixer.music.unpause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        nine_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        nine_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def hard_game():
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            three_hearts = pygame.image.load('gfiles/3_hard.png')
            screen.blit(three_hearts, (8, 8))
            pygame.mixer.music.pause()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.mixer.music.unpause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        two_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        two_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()
            pygame.display.update()

    def nightmare_game():
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            one_heart = pygame.image.load('gfiles/1_nightmare.png')
            screen.blit(one_heart, (8, 8))
            pygame.mixer.music.pause()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.mixer.music.unpause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) != x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        loss()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()
            pygame.display.update()

    def victory():
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load('gfiles/fortnitesound.wav')
        pygame.mixer.music.play(loops=0)

        moving_sprites = pygame.sprite.Group()
        gif = Gif(297, 297)
        moving_sprites.add(gif)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()

            gif.switch()
            screen.fill((255, 255, 255))
            moving_sprites.draw(screen)
            moving_sprites.update(0.25)

            fortnite_image = pygame.image.load('gfiles/fortnite.png')
            screen.blit(fortnite_image, (100, 32))
            ez_image = pygame.image.load('gfiles/EZ.png')
            screen.blit(ez_image, (170, 300))

            font4 = pygame.font.SysFont('Courier', 32)
            show_esc = font4.render('Press ESC', True, (0, 0, 0))
            screen.blit(show_esc, (315, 500))

            pygame.display.flip()
            clock.tick(12)

    def loss():
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.load('gfiles/bum.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            screen.fill((0, 0, 0))  # bgcolor
            DarkSouls_image = pygame.image.load('gfiles/you_died.jpg')
            screen.blit(DarkSouls_image, (0, 32))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()

            font4 = pygame.font.SysFont('Courier', 32)
            show_esc = font4.render('Press ESC', True, (255, 255, 255))
            screen.blit(show_esc, (315, 500))
            pygame.display.update()

    def nine_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            nine_hearts = pygame.image.load('gfiles/9_hearts.png')
            screen.blit(nine_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        eight_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        eight_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def eight_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            eight_hearts = pygame.image.load('gfiles/8_hearts.png')
            screen.blit(eight_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        seven_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        seven_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def seven_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            seven_hearts = pygame.image.load('gfiles/7_hearts.png')
            screen.blit(seven_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        six_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        six_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def six_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            six_hearts = pygame.image.load('gfiles/6_hearts.png')
            screen.blit(six_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        five_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        five_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def five_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            five_hearts = pygame.image.load('gfiles/5_hearts.png')
            screen.blit(five_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        four_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        four_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def four_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            four_hearts = pygame.image.load('gfiles/4_hearts.png')
            screen.blit(four_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        three_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        three_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def three_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            three_hearts = pygame.image.load('gfiles/3_hard.png')
            screen.blit(three_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        two_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        two_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def two_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            two_hearts = pygame.image.load('gfiles/2_hearts.png')
            screen.blit(two_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        one_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        one_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def one_up():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            one_heart = pygame.image.load('gfiles/1_nightmare.png')
            screen.blit(one_heart, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowup.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) != x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        loss()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def nine_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            nine_hearts = pygame.image.load('gfiles/9_hearts.png')
            screen.blit(nine_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        eight_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        eight_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def eight_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            eight_hearts = pygame.image.load('gfiles/8_hearts.png')
            screen.blit(eight_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        seven_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        seven_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def seven_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            seven_hearts = pygame.image.load('gfiles/7_hearts.png')
            screen.blit(seven_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        six_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        six_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def six_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            six_hearts = pygame.image.load('gfiles/6_hearts.png')
            screen.blit(six_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        five_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        five_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def five_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            five_hearts = pygame.image.load('gfiles/5_hearts.png')
            screen.blit(five_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        four_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        four_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def four_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            four_hearts = pygame.image.load('gfiles/4_hearts.png')
            screen.blit(four_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        three_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        three_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def three_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            three_hearts = pygame.image.load('gfiles/3_hard.png')
            screen.blit(three_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        two_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        two_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def two_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            two_hearts = pygame.image.load('gfiles/2_hearts.png')
            screen.blit(two_hearts, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) < options.index(option):
                    if click:
                        one_down()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and options.index(x) > options.index(option):
                    if click:
                        one_up()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    def one_down():
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load('gfiles/Hit Marker.wav')
        pygame.mixer.music.play(loops=0)
        running = True
        while running:
            pygame.event.pump()
            screen.fill((0, 0, 0))  # bgcolor
            one_heart = pygame.image.load('gfiles/1_nightmare.png')
            screen.blit(one_heart, (8, 8))
            arrow_up = pygame.image.load('gfiles/arrowdown.png')
            screen.blit(arrow_up, (762, 8))
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit when pressed X
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # undo when pressed ESC
                    if event.key == pygame.K_ESCAPE:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) == x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        victory()
                elif option.rect.collidepoint(pygame.mouse.get_pos()) and option.rect.collidepoint(
                        pygame.mouse.get_pos()) != x.rect.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        loss()
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()

    menu()


main()
