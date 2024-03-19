import config


class TextObject:
    font = config.FONT

    def __init__(self, text=str, one_on_display_surf=False):
        self.image = self.font.render(text, True, config.BLACK)
        self.rect = self.image.get_rect()
        if one_on_display_surf:
            self.rect.x = config.SCREEN_WIDTH / 2 - self.rect.width / 2
            self.rect.y = config.SCREEN_HEIGHT /2 - self.rect.height / 2 + 50