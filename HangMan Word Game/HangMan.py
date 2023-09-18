import sys
import subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
import pygame
from pygame.locals import *
import random
import time
pygame.init()

def main():
    # Assets:
        ## Music
            ### Menu Music:
    def background_menu_music():
        pygame.mixer.init()
        path = 'HangMan/assets/music/menu_music.mp3'
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.65)
        pygame.mixer.music.play(-1)

            ### In-game Music:
    def game_music():
        path = 'HangMan/assets/music/game_music.mp3'
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.45)
        pygame.mixer.music.play(-1)

        ## Screen
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hangman')
    fps = 60
    screen.fill((255, 255, 255))

        ## Text:
    def add_text():
            ### Title
        font = pygame.font.SysFont('Calibri', 70)
        text = font.render('Hang Man', True, (255, 0, 0))
        screen.blit(text, (250, 30))

            ### Credit
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('Made by Nhat Nam Khanh Nguyen & Tewodros Asrat', True, (255, 0, 0))
        screen.blit(text, (20, 560))

            ### Start
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Start', True, (255, 0, 0))
        screen.blit(text, (370, 350))

            ### Quit
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Quit', True, (255, 0, 0))
        screen.blit(text, (375, 430))

    def restartexit_button():
            ### Restart
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Restart', True, (255, 0, 0))
        screen.blit(text, (300, 320))
            ### Exit
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Exit', True, (255, 0, 0))
        screen.blit(text, (450, 320))
        
        ## Images:
            ### Button Image
    button_image = pygame.image.load('HangMan/assets/img/MainMenu/Click Button/button.png').convert_alpha()

            ### Game Logo
    def logo():
        logo_image = pygame.image.load('HangMan/assets/img/MainMenu/Logo/logo.png').convert_alpha()
        logo = pygame.transform.scale(logo_image, (100, 100))
        screen.blit(logo, (350, 195))
        pygame.display.set_icon(logo_image)
        
        ## Click Button:
    class Button():
                ### Button
            def __init__(self, x, y, image, scaleW, scaleH):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scaleW), int(height * scaleH)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

                ### Click mechanic (1 click at a time)
            def button(self):
                click = False
                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        click = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
                screen.blit(self.image, (self.rect.x, self.rect.y))
                return click

            ### Functional Buttons
    start_button = Button(370, 350, button_image, 55/640, 35/360)
    quit_button = Button(375, 430, button_image, 45/640, 35/360)
    restart_button = Button(300, 320, button_image, 0.125, 0.08)
    exit_button = Button(450, 320, button_image, 0.125, 0.08)

        ## English word module:
    def get_word():
        sys.path.insert(1, 'HangMan/assets/modules/english words')
        from words import word_list
        word = random.choice(word_list)
        return word.upper()
    word = get_word()
    display_lines = len(word)
    

        ## Underscores:
    def underscores():
        if display_lines == 1:
            i_0 = (370, 248)
            i_1 = (0, 0)
            i_2 = (0, 0)
            i_3 = (0, 0)
            i_4 = (0, 0)
            i_5 = (0, 0)
            i_6 = (0, 0)
            i_7 = (0, 0)
            i_8 = (0, 0)
            i_9 = (0, 0)
            pygame.draw.line(screen, (0, 0, 0), (360, 280), (400, 280), 2)
        if display_lines == 2:
            i_0 = (350, 248)
            pygame.draw.line(screen, (0, 0, 0), (340, 280), (380, 280), 2)
            i_1 = (410, 248)
            pygame.draw.line(screen, (0, 0, 0), (400, 280), (440, 280), 2)
            i_2 = (0, 0)
            i_3 = (0, 0)
            i_4 = (0, 0)
            i_5 = (0, 0)
            i_6 = (0, 0)
            i_7 = (0, 0)
            i_8 = (0, 0)
            i_9 = (0, 0)
        if display_lines == 3:
            i_0 = (330, 248)
            pygame.draw.line(screen, (0, 0, 0), (320, 280), (360, 280), 2)
            i_1 = (390, 248)
            pygame.draw.line(screen, (0, 0, 0), (380, 280), (420, 280), 2)
            i_2 = (450, 248)
            pygame.draw.line(screen, (0, 0, 0), (440, 280), (480, 280), 2)
            i_3 = (0, 0)
            i_4 = (0, 0)
            i_5 = (0, 0)
            i_6 = (0, 0)
            i_7 = (0, 0)
            i_8 = (0, 0)
            i_9 = (0, 0)
        if display_lines == 4:
            i_0 = (310, 248)
            pygame.draw.line(screen, (0, 0, 0), (300, 280), (340, 280), 2)
            i_1 = (370, 248)
            pygame.draw.line(screen, (0, 0, 0), (360, 280), (400, 280), 2)
            i_2 = (430, 248)
            pygame.draw.line(screen, (0, 0, 0), (420, 280), (460, 280), 2)
            i_3 = (490, 248)
            pygame.draw.line(screen, (0, 0, 0), (480, 280), (520, 280), 2)
            i_4 = (0, 0)
            i_5 = (0, 0)
            i_6 = (0, 0)
            i_7 = (0, 0)
            i_8 = (0, 0)
            i_9 = (0, 0)
        if display_lines == 5:
            i_0 = (270, 248)
            pygame.draw.line(screen, (0, 0, 0), (260, 280), (300, 280), 2)
            i_1 = (330, 248)
            pygame.draw.line(screen, (0, 0, 0), (320, 280), (360, 280), 2)
            i_2 = (390, 248)
            pygame.draw.line(screen, (0, 0, 0), (380, 280), (420, 280), 2)
            i_3 = (450, 248)
            pygame.draw.line(screen, (0, 0, 0), (440, 280), (480, 280), 2)
            i_4 = (510, 248)
            pygame.draw.line(screen, (0, 0, 0), (500, 280), (540, 280), 2)
            i_5 = (0, 0)
            i_6 = (0, 0)
            i_7 = (0, 0)
            i_8 = (0, 0)
            i_9 = (0, 0)
        if display_lines == 6:
            i_0 = (250, 248)
            pygame.draw.line(screen, (0, 0, 0), (240, 280), (280, 280), 2)
            i_1 = (310, 248)
            pygame.draw.line(screen, (0, 0, 0), (300, 280), (340, 280), 2)
            i_2 = (370, 248)
            pygame.draw.line(screen, (0, 0, 0), (360, 280), (400, 280), 2)
            i_3 = (430, 248)
            pygame.draw.line(screen, (0, 0, 0), (420, 280), (460, 280), 2)
            i_4 = (490, 248)
            pygame.draw.line(screen, (0, 0, 0), (480, 280), (520, 280), 2)
            i_5 = (550, 248)
            pygame.draw.line(screen, (0, 0, 0), (540, 280), (580, 280), 2)
            i_6 = (0, 0)
            i_7 = (0, 0)
            i_8 = (0, 0)
            i_9 = (0, 0)
        if display_lines == 7:
            i_0 = (210, 248)
            pygame.draw.line(screen, (0, 0, 0), (200, 280), (240, 280), 2)
            i_1 = (270, 248)
            pygame.draw.line(screen, (0, 0, 0), (260, 280), (300, 280), 2)
            i_2 = (330, 248)
            pygame.draw.line(screen, (0, 0, 0), (320, 280), (360, 280), 2)
            i_3 = (390, 248)
            pygame.draw.line(screen, (0, 0, 0), (380, 280), (420, 280), 2)
            i_4 = (450, 248)
            pygame.draw.line(screen, (0, 0, 0), (440, 280), (480, 280), 2)
            i_5 = (510, 248)
            pygame.draw.line(screen, (0, 0, 0), (500, 280), (540, 280), 2)
            i_6 = (570, 248)
            pygame.draw.line(screen, (0, 0, 0), (560, 280), (600, 280), 2)
            i_7 = (0, 0)
            i_8 = (0, 0)
            i_9 = (0, 0)
        if display_lines == 8:
            i_0 = (170, 248)
            pygame.draw.line(screen, (0, 0, 0), (160, 280), (200, 280), 2)
            i_1 = (230, 248)
            pygame.draw.line(screen, (0, 0, 0), (220, 280), (260, 280), 2)
            i_2 = (290, 248)
            pygame.draw.line(screen, (0, 0, 0), (280, 280), (320, 280), 2)
            i_3 = (350, 248)
            pygame.draw.line(screen, (0, 0, 0), (340, 280), (380, 280), 2)
            i_4 = (410, 248)
            pygame.draw.line(screen, (0, 0, 0), (400, 280), (440, 280), 2)
            i_5 = (470, 248)
            pygame.draw.line(screen, (0, 0, 0), (460, 280), (500, 280), 2)
            i_6 = (530, 248)
            pygame.draw.line(screen, (0, 0, 0), (520, 280), (560, 280), 2)
            i_7 = (590, 248)
            pygame.draw.line(screen, (0, 0, 0), (580, 280), (620, 280), 2)
            i_8 = (0, 0)
            i_9 = (0, 0)
        if display_lines == 9:
            i_0 = (150, 248)
            pygame.draw.line(screen, (0, 0, 0), (140, 280), (180, 280), 2)
            i_1 = (210, 248)
            pygame.draw.line(screen, (0, 0, 0), (200, 280), (240, 280), 2)
            i_2 = (270, 248)
            pygame.draw.line(screen, (0, 0, 0), (260, 280), (300, 280), 2)
            i_3 = (330, 248)
            pygame.draw.line(screen, (0, 0, 0), (320, 280), (360, 280), 2)
            i_4 = (390, 248)
            pygame.draw.line(screen, (0, 0, 0), (380, 280), (420, 280), 2)
            i_5 = (450, 248)
            pygame.draw.line(screen, (0, 0, 0), (440, 280), (480, 280), 2)
            i_6 = (510, 248)
            pygame.draw.line(screen, (0, 0, 0), (500, 280), (540, 280), 2)
            i_7 = (570, 248)
            pygame.draw.line(screen, (0, 0, 0), (560, 280), (600, 280), 2)
            i_8 = (630, 248)
            pygame.draw.line(screen, (0, 0, 0), (620, 280), (660, 280), 2)
            i_9 = (0, 0)
        if display_lines == 10:
            i_0 = (110, 248)
            pygame.draw.line(screen, (0, 0, 0), (100, 280), (140, 280), 2)
            i_1 = (170, 248)
            pygame.draw.line(screen, (0, 0, 0), (160, 280), (200, 280), 2)
            i_2 = (230, 248)
            pygame.draw.line(screen, (0, 0, 0), (220, 280), (260, 280), 2)
            i_3 = (290, 248)
            pygame.draw.line(screen, (0, 0, 0), (280, 280), (320, 280), 2)
            i_4 = (350, 248)
            pygame.draw.line(screen, (0, 0, 0), (340, 280), (380, 280), 2)
            i_5 = (410, 248)
            pygame.draw.line(screen, (0, 0, 0), (400, 280), (440, 280), 2)
            i_6 = (470, 248)
            pygame.draw.line(screen, (0, 0, 0), (460, 280), (500, 280), 2)
            i_7 = (530, 248)
            pygame.draw.line(screen, (0, 0, 0), (520, 280), (560, 280), 2)
            i_8 = (590, 248)
            pygame.draw.line(screen, (0, 0, 0), (580, 280), (620, 280), 2)
            i_9 = (650, 248)
            pygame.draw.line(screen, (0, 0, 0), (640, 280), (680, 280), 2)
        return i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9

        ## Hanging Pole:
    def draw_hanging_pole():
        img = pygame.image.load('HangMan/assets/img/Hanging Pole/pole.png').convert_alpha()
        hanging_pole = pygame.transform.scale(img, (100,100))
        screen.blit(hanging_pole, (275, 55))
        hanging_bar = pygame.transform.rotate(pygame.transform.scale(img, (80, 80)), 270)
        screen.blit(hanging_bar, (325, 21))
        
        ## Head:
    def draw_head():
        pygame.draw.circle(screen, (0, 0, 0), (400, 73), 10, 3)
        
        ## Torso:
    def draw_torso():
        pygame.draw.line(screen, (0, 0, 0), (399, 83), (399, 113), 3)
        
        ## Left arm:
    def draw_left_arm():
        pygame.draw.line(screen, (0, 0, 0), (399, 83), (379, 93), 3)
        
        ## Right arm:
    def draw_right_arm():
        pygame.draw.line(screen, (0, 0, 0), (399, 83), (419, 93), 3)
        
        ## Left leg:
    def draw_left_leg():
        pygame.draw.line(screen, (0, 0, 0), (399, 113), (379, 123), 3)
        
        ## Right leg:
    def draw_right_leg():
        pygame.draw.line(screen, (0, 0, 0), (399, 113), (419, 123), 3)
        
        ## Interactive letters:
            ### A:
    A_button = Button(50, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha(), 1, 1)

            ### B:
    B_button = Button(110, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha(), 1, 1)

            ### C:
    C_button = Button(170, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha(), 1, 1)

            ### D:
    D_button = Button(230, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha(), 1, 1)

            ### E:
    E_button = Button(290, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha(), 1, 1)

            ### F:
    F_button = Button(350, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha(), 1, 1)

            ### G:
    G_button = Button(400, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha(), 1, 1)

            ### H:
    H_button = Button(460, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha(), 1, 1)

            ### I:
    I_button = Button(525, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha(), 1, 1)

            ### J:
    J_button = Button(570, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha(), 1, 1)

            ### K:
    K_button = Button(630, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha(), 1, 1)

            ### L:
    L_button = Button(690, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha(), 1, 1)

            ### M:
    M_button = Button(740, 400, pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha(), 1, 1)

            ### N:
    N_button = Button(50, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha(), 1, 1)

            ### O:
    O_button = Button(105, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha(), 1, 1)

            ### P:
    P_button = Button(175, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha(), 1, 1)

            ### Q:
    Q_button = Button(225, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha(), 1, 1)

            ### R:
    R_button = Button(290, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha(), 1, 1)

            ### S:
    S_button = Button(350, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha(), 1, 1)

            ### T:
    T_button = Button(405, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha(), 1, 1)

            ### U:
    U_button = Button(460, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha(), 1, 1)

            ### V:
    V_button = Button(520, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha(), 1, 1)

            ### W:
    W_button = Button(568, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha(), 1, 1)

            ### X:
    X_button = Button(630, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha(), 1, 1)

            ### Y:
    Y_button = Button(690, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha(), 1, 1)

            ### Z:
    Z_button = Button(745, 500, pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha(), 1, 1)

    # Main Game:
    def game():
        game_music()
        screen.fill((255, 255, 255))
        clock = pygame.time.Clock()
        gameLoop = True
        draw_hanging_pole()
        tries = 6
        win = display_lines
        ## Logic System
        while gameLoop:
            while tries > 0:
                i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9 = underscores()
                if A_button.button():
                    A = "A"
                    if A in word:
                        for i in range(0, len(word)):
                            if word[i] == A:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/A.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                                
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (46, 415))
                if B_button.button():
                    B = "B"
                    if B in word:
                        for i in range(0, len(word)):
                            if word[i] == B:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/B.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (106, 415))
                if C_button.button():
                    C = "C"
                    if C in word:
                        for i in range(0, len(word)):
                            if word[i] == C:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/C.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (166, 415))
                if D_button.button():
                    D = "D"
                    if D in word:
                        for i in range(0, len(word)):
                            if word[i] == D:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/D.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (226, 415))
                if E_button.button():
                    E = "E"
                    if E in word:
                        for i in range(0, len(word)):
                            if word[i] == E:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/E.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (286, 415))
                if F_button.button():
                    F = "F"
                    if F in word:
                        for i in range(0, len(word)):
                            if word[i] == F:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/F.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (346, 415))
                if G_button.button():
                    G = "G"
                    if G in word:
                        for i in range(0, len(word)):
                            if word[i] == G:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/G.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (396, 415))
                if H_button.button():
                    H = "H"
                    if H in word:
                        for i in range(0, len(word)):
                            if word[i] == H:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/H.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (456, 415))
                if I_button.button():
                    I = "I"
                    if I in word:
                        for i in range(0, len(word)):
                            if word[i] == I:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/I.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (20, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (515, 415))
                if J_button.button():
                    J = "J"
                    if J in word:
                        for i in range(0, len(word)):
                            if word[i] == J:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/J.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (566, 415))
                if K_button.button():
                    K = "K"
                    if K in word:
                        for i in range(0, len(word)):
                            if word[i] == K:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/K.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (626, 415))
                if L_button.button():
                    L = "L"
                    if L in word:
                        for i in range(0, len(word)):
                            if word[i] == L:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/L.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (686, 415))
                if M_button.button():
                    M = "M"
                    if M in word:
                        for i in range(0, len(word)):
                            if word[i] == M:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/M.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (736, 415))
                if N_button.button():
                    N = "N"
                    if N in word:
                        for i in range(0, len(word)):
                            if word[i] == N:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/N.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (46, 515))
                if O_button.button():
                    O = "O"
                    if O in word:
                        for i in range(0, len(word)):
                            if word[i] == O:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/O.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (101, 515))
                if P_button.button():
                    P = "P"
                    if P in word:
                        for i in range(0, len(word)):
                            if word[i] == P:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/P.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (171, 515))
                if Q_button.button():
                    Q = "Q"
                    if Q in word:
                        for i in range(0, len(word)):
                            if word[i] == Q:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Q.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (221, 515))
                if R_button.button():
                    R = "R"
                    if R in word:
                        for i in range(0, len(word)):
                            if word[i] == R:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/R.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (286, 515))
                if S_button.button():
                    S = "S"
                    if S in word:
                        for i in range(0, len(word)):
                            if word[i] == S:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/S.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (346, 515))
                if T_button.button():
                    T = "T"
                    if T in word:
                        for i in range(0, len(word)):
                            if word[i] == T:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/T.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (401, 515))
                if U_button.button():
                    U = "U"
                    if U in word:
                        for i in range(0, len(word)):
                            if word[i] == U:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/U.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (456, 515))
                if V_button.button():
                    V = "V"
                    if V in word:
                        for i in range(0, len(word)):
                            if word[i] == V:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/V.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (516, 515))
                if W_button.button():
                    W = "W"
                    if W in word:
                        for i in range(0, len(word)):
                            if word[i] == W:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/W.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (564, 515))
                if X_button.button():
                    X = "X"
                    if X in word:
                        for i in range(0, len(word)):
                            if word[i] == X:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/X.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (626, 515))
                if Y_button.button():
                    Y = "Y"
                    if Y in word:
                        for i in range(0, len(word)):
                            if word[i] == Y:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Y.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (686, 515))
                if Z_button.button():
                    Z = "Z"
                    if Z in word:
                        for i in range(0, len(word)):
                            if word[i] == Z:
                                win -= 1
                                if i == 0:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_0)
                                if i == 1:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_1)
                                if i == 2:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_2)
                                if i == 3:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_3)
                                if i == 4:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_4)
                                if i == 5:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_5)
                                if i == 6:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_6)
                                if i == 7:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_7)
                                if i == 8:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_8)
                                if i == 9:
                                    img = pygame.image.load('HangMan/assets/img/Interactive Letters/Z.png').convert_alpha()
                                    screen.blit(pygame.transform.scale(img, (30, 50)), i_9)
                    else:
                        tries -= 1
                        img = pygame.image.load('HangMan/assets/img/Interactive Letters/x_symbol.png').convert_alpha()
                        screen.blit(pygame.transform.scale(img, (30, 30)), (741, 515))
        
        ## Win condition:
                if win == 0:
                    tries = -1
                    font = pygame.font.SysFont('Arial',30)
                    game_over = font.render('Victory!', True, (0, 150, 100))
                    screen.blit(game_over, (365, 190))
                    print("Game Over!")
                    restartexit_button()
                    pygame.display.update()

        ## Lose condition:
                if tries == 5:
                    draw_head()
                elif tries == 4:
                    draw_torso()
                elif tries == 3:
                    draw_left_arm()
                elif tries == 2:
                    draw_right_arm()
                elif tries == 1:
                    draw_left_leg()
                elif tries == 0:
                    draw_right_leg()
                    font = pygame.font.SysFont('Arial',30)
                    game_over = font.render('Game Over!', True, (255, 0, 0))
                    screen.blit(game_over, (330, 170))
                    result = font.render('The answer is: ' + word, True, (255, 0, 0))
                    screen.blit(result, (260, 210))
                    print("Game Over!")
                    restartexit_button()
                    pygame.display.update()
                break
            
        ## Restart and Exit game after win/lose:
            if tries == 0:
                if restart_button.button():
                    main()
                if exit_button.button():
                    gameLoop = False
            if win == 0:
                if restart_button.button():
                    main()
                if exit_button.button():
                    gameLoop = False
            
            ## Configuration:
            clock.tick(fps)
            for event in pygame.event.get():            # Terminate game when click EXIT
                if event.type == pygame.QUIT:
                    gameLoop = False
            pygame.display.update()
        pygame.quit()

    # Main Menu:
    def menu():
        background_menu_music()
        add_text()
        logo()
        pygame.display.update()
        clock = pygame.time.Clock()
        menuLoop = True
        while menuLoop:
            clock.tick(fps)
        ## Start game:
            if start_button.button() == True:
                print('Start! Please Wait!')
                font = pygame.font.SysFont('Arial', 25)
                text = font.render('Please wait!', True, (255, 0, 0))
                screen.blit(text, (345, 315))
                pygame.display.update()
                time.sleep(1)
                pygame.mixer.music.pause()
                game()

        ## Quit game
            if quit_button.button():
                menuLoop = False
                
        ## Terminate game when click EXIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menuLoop = False
            pygame.display.update()
        pygame.quit()
    menu()
main()
