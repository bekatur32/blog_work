import config
from objects.button_object import ButtonObject


def create_menu(types_of_buttons):
    button_data = dict()
    buttons = []

    for _button in types_of_buttons:
        button_data[_button] = config.properties_of_button

    _x_of_first_button = config.SCREEN_HEIGHT / 2 - len(button_data) * config.BUTTON_SIZE[1] / 2

    for i, _button in enumerate(button_data):
        _tb = ButtonObject(**button_data[_button], button=_button)
        _tb.set_x(config.SCREEN_WIDTH / 2 - config.BUTTON_SIZE[0] / 2)
        _tb.set_y(_x_of_first_button + i * (config.BUTTON_SIZE[1] + 1))
        buttons.append(_tb)
    return buttons
