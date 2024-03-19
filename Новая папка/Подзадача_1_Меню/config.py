from pygame import font  # Для текста нам понадобится шрифт

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

font.init()  # Надо инициализировать работу шрифтов

FONT = font.SysFont(name='Arial', size=40, bold=True)  # После зададим шрифт

BLACK = (0, 0, 0)  # Зададим черный цвет

button = ["PLAY", "SCORE", "QUIT"]  # Список кнопок в config

BUTTON_COL = (133, 253, 249)
BUTTON_PRESSED_COL = (133, 253, 150)
BUTTON_SIZE = (160, 40)