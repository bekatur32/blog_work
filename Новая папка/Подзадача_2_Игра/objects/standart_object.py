from pygame import Surface
from pygame import transform


class GameObject:

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

