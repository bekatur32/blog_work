from pygame import Surface
import config
from pygame import mouse


class Block:

    def __init__(self, size, color):
        self.image = Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def get_x(self):
        return self.rect.x

    def set_x(self, x):
        self.rect.x = x

    def get_y(self):
        return self.rect.y

    def set_y(self, y):
        self.rect.y = y

    def set_color(self, color):
        self.image.fill(color)


class TextObject:

    def __init__(self, text, x, y):
        self.font = config.FONT
        self.image = self.font.render(text, True, config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ButtonObject(Block):

    def __init__(self, size, color, button):

        super().__init__(size, color)
        self.type = button
        self.text_obj = TextObject(button, 0, 0)

        self.text_obj.rect.x = self.rect.width / 2 - self.text_obj.rect.width / 2
        self.text_obj.rect.y = self.rect.height / 2 - self.text_obj.rect.height / 2
        self.image.blit(self.text_obj.image, self.text_obj.rect)

    def is_touched(self):
        if self.rect.collidepoint(mouse.get_pos()):
            self.set_color(config.BUTTON_PRESSED_COL)
        else:
            self.set_color(config.BUTTON_COL)

    def set_color(self, color):
        self.image.fill(color)
        self.image.blit(self.text_obj.image, self.text_obj.rect)