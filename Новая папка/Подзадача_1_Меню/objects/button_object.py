from .standart_object import GameObject
from .text_object import TextObject
from pygame import mouse
import config


class ButtonObject(GameObject):

    def __init__(self, size, color, button):
        super().__init__(size, color)
        self.type = button
        self.text_obj = TextObject(button.value)
        self.text_obj.rect.x = self.rect.width / 2 - self.text_obj.rect.width / 2
        self.text_obj.rect.y = self.rect.height / 2 - self.text_obj.rect.height / 2
        self.image.blit(self.text_obj.image, self.text_obj.rect)

    def is_touched(self):
        if self.rect.collidepoint(mouse.get_pos()):
            self.set_color(config.BUTTON_PRESSED_COL)
            return True
        else:
            self.set_color(config.BUTTON_UNPRESSED_COL)
            return False

    def set_color(self, color):
        self.image.fill(color)
        self.image.blit(self.text_obj.image, self.text_obj.rect)
