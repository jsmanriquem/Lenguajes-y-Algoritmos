import pygame
import os
from gameboard import GameBoard
from constants import *

class GameManager(object):
    def __init__(self, easy_mode, aoutowin):
        self.my_path = "%s/.." % os.path.dirname(os.path.realpath(__file__))
        pygame.init()
        pygame.display.set_caption("Solitaire")
        logo_path = os.path.join(self.my_path, "img", "solitaire_logo.png")
        logo = pygame.image.load(logo_path)
        pygame.display.set_icon(logo)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.background_tex = None
        self.restart_tex = None
        self.restart_highlight_tex = None
        self.textures = {}
        self.loadTextures()

        self.gameBoard = GameBoard(self.textures, easy_mode, aoutowin)

        self.mouse_held = False
        self.mouse_pos = (0, 0)

        self.restart_button = pygame.Rect((20, TOPROW_Y), RESTART_BUTTON_SIZE)

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            else:
                self.handleMouseInput(event)

    def handleMouseInput(self, event):
        self.mouse_pos = pygame.mouse.get_pos()
        self.gameBoard.mouse_pos = self.mouse_pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.mouse_held:
                self.mouse_held = True
                self.gameBoard.mouseClicked()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.mouse_held:
                self.mouse_held = False
                if self.restart_button.collidepoint(self.mouse_pos):
                    self.gameBoard.restartGame()
                else:
                    self.gameBoard.mouseReleased()

    def playGame(self):
        running = True
        while running:
            if self.handleInput() == 1:
                running = False
            self.drawGame()

    def drawGame(self):
        if not self.gameBoard.player_won or not self.gameBoard.drawn_once:
            self.screen.blit(self.background_tex, (0, 0))
        if self.restart_button.collidepoint(self.mouse_pos):
            self.screen.blit(self.restart_highlight_tex, self.restart_button.topleft)
        else:
            self.screen.blit(self.restart_tex, self.restart_button.topleft)
        self.gameBoard.drawBoard(self.screen)
        pygame.display.flip()

    def loadTextures(self):
        self.background_tex = pygame.image.load(os.path.join(self.my_path, "img/background.png"))
        self.restart_tex = pygame.transform.scale(pygame.image.load(os.path.join(self.my_path, "img/restart.png")), RESTART_BUTTON_SIZE)

        self.textures["card_tex"] = pygame.image.load(os.path.join(self.my_path, "img/card_textures/card.png"))
        self.textures["card_back_tex"] = pygame.image.load(os.path.join(self.my_path, "img/card_textures/card_back.png"))
        self.textures["empty_tex"] = pygame.image.load(os.path.join(self.my_path, "img/card_textures/empty_holder.png"))

        self.textures["suit_textures"] = {
            "HEARTS": pygame.transform.scale(pygame.image.load(os.path.join(self.my_path, "img/card_textures/suits/big_hearts.png")), CARD_SMALL_ITEM_SIZE),
            "DIAMONDS": pygame.transform.scale(pygame.image.load(os.path.join(self.my_path, "img/card_textures/suits/big_diamonds.png")), CARD_SMALL_ITEM_SIZE),
            "CLUBS": pygame.transform.scale(pygame.image.load(os.path.join(self.my_path, "img/card_textures/suits/big_clubs.png")), CARD_SMALL_ITEM_SIZE),
            "SPADES": pygame.transform.scale(pygame.image.load(os.path.join(self.my_path, "img/card_textures/suits/big_spades.png")), CARD_SMALL_ITEM_SIZE)
        }

        black_value_textures = {}
        red_value_textures = {}
        numbers_dir = os.path.join(self.my_path, "img/card_textures/numbers")
        try:
            for image_file in os.listdir(numbers_dir):
                new_tex = pygame.transform.scale(pygame.image.load(os.path.join(numbers_dir, image_file)), CARD_SMALL_ITEM_SIZE)
                filepath_split = image_file.split('_')
                val = int(filepath_split[0])
                color = filepath_split[1]
                if color == 'b':
                    black_value_textures[val] = new_tex
                elif color == 'r':
                    red_value_textures[val] = new_tex
                else:
                    raise ValueError
        except ValueError as err:
            print("Error loading number textures. %s" % err)
        self.textures["black_value_textures"] = black_value_textures
        self.textures["red_value_textures"] = red_value_textures

        self.textures["deck_tex"] = self.textures["card_back_tex"]
