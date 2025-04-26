# C - Constantes começadas pela letra C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E Velocidade
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    #'Level2Bg0': 999,
    #'Level2Bg1': 999,
    #'Level2Bg2': 999,
    #'Level2Bg3': 999,
    #'Level2Bg4': 999,
    'Player1': 300,
    #'Player1Shot': 1,
    'Player2': 300,
    #'Player2Shot': 1,
    'Enemy1': 50,
    #'Enemy1Shot': 1,
    'Enemy2': 60,
    #'Enemy2Shot': 1,
}

# M - Constantes começadas pela letra M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

PLAYER_KEY_UP = {'Player1': pygame.K_UP, # Movimento o Player1 para cima
                 'Player2': pygame.K_w} # Movimento o Player2 para cima
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, # Movimento o Player1 para baixo
                   'Player2': pygame.K_s} # Movimento o Player2 para baixo
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, # Movimento o Player1 para a esquerda
                   'Player2': pygame.K_a} # Movimento o Player1 para a esquerda
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, # Movimento o Player1 para a direita
                    'Player2': pygame.K_d} # Movimento o Player2 para a direita
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, # Comando para os tiros do Player1
                    'Player2': pygame.K_LCTRL} # Comando para os tiros do Player2

# S
SPAWN_TIME = 4000


# W - Constantes começadas pela letra W
WIN_WIDTH = 576
WIN_HEIGHT = 324
