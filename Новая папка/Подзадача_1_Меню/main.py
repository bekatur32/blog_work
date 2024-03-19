import pygame
import config
import utils


class Window:

    def __init__(self):
        pygame.init()
        self._running = True
        self._display_surf_color = config.BLACK
        self._display_surf = pygame.display.set_mode(config.SCREEN_SIZE)
        self._clock = pygame.time.Clock()

        self.main_menu_buttons = utils.create_menu(config.button)

    @staticmethod

    def on_cleanup():
        pygame.quit()


    def on_init(self):
        self._display_surf.fill(self._display_surf_color)



    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for i, _btn in enumerate(self.main_menu_buttons):
                if _btn.rect.collidepoint(pygame.mouse.get_pos()):
                    print(f"Нажата кнопка {_btn.type}")

    def on_render(self):
        self._display_surf.fill(self._display_surf_color)
        for btn in self.main_menu_buttons:
            btn.is_touched()
            self._display_surf.blit(btn.image, btn.rect)
        pygame.display.flip()

    def on_start(self):
        self.on_init()
        while self._running:
            self._clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)

            self.on_render()
        self.on_cleanup()


window = Window()
window.on_start()