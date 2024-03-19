import config
from tools import ButtonObject


def create_menu(button):
    buttons = []


    _y_of_first_button = config.SCREEN_HEIGHT / 2 - len(button) * config.BUTTON_SIZE[1] / 2
    for i, _button in enumerate(button):
        _tb = ButtonObject(config.BUTTON_SIZE, config.BUTTON_COL, _button)
        _tb.set_x(config.SCREEN_WIDTH / 2 - config.BUTTON_SIZE[0] / 2)

        _tb.set_y(_y_of_first_button + i * (config.BUTTON_SIZE[1] + 5))
        buttons.append(_tb)
    return buttons
