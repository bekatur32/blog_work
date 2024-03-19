from pygame import font
from enum import Enum

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

FPS = 60
font.init()
FONT = font.SysFont(name='Arial', size=16, bold=True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class ButtonsType(Enum):
    START = 'Старт'
    SCORE = 'Счёт'
    QUIT = 'Выход'
    RESTART = 'Перезапустить'


class StateOfGame(Enum):
    MENU = 1
    GAME = 2
    SCORE = 3


BUTTON_UNPRESSED_COL = (133, 253, 193)
BUTTON_PRESSED_COL = (133, 253, 249)
BUTTON_SIZE = (160, 40)
properties_of_button = {'size': BUTTON_SIZE,
                        'color': BUTTON_UNPRESSED_COL}
