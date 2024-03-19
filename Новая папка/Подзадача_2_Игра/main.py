from pygame import display
from pygame import time
from pygame import event
from pygame import constants
from pygame import mouse
import config
import utils
import random
from objects.text_object import TextObject
from objects.standart_object import GameObject


class Window:

    def __init__(self):
        display.init()
        self._display_surf = display.set_mode(config.SCREEN_SIZE)
        self._clock = time.Clock()

        self._buttons = []
        self._objects = []

        self.main_menu_buttons = utils.create_menu(
            (config.ButtonsType.START, config.ButtonsType.SCORE, config.ButtonsType.QUIT))
        self._buttons += self.main_menu_buttons
        self.after_game_menu_buttons = utils.create_menu((config.ButtonsType.RESTART, config.ButtonsType.QUIT))
        self._buttons += self.after_game_menu_buttons

        self._state_of_game = config.StateOfGame.MENU

        self._objects += self.main_menu_buttons

        self._running = True

        self._start_of_game = False
        self._playing_game = False
        self._space_is_pressed = False
        self._time_to_play = 0
        self._score = 0
        self._scores = []

    def _on_init(self):
        self._display_surf.fill(config.WHITE)

    def _on_loop(self):
        if self._state_of_game == config.StateOfGame.GAME:
            # self.example_of_game_1()
            self.example_of_game_2()

    def example_of_game_1(self):
        if self._start_of_game:
            self._init_time = time.get_ticks()
            self._time_to_press = self._init_time + random.randint(100, 3000)
            self._start_of_game = False
            self._objects.append(TextObject('Приготовься нажаться кнопку', True))

        if time.get_ticks() >= self._time_to_press and not self._playing_game:
            self._objects = []
            self._objects.append(TextObject('Нажимай кнопку', True))
            self._playing_game = True

        if self._playing_game and self._space_is_pressed:
            self._scores.append(time.get_ticks() - self._time_to_press)
            self._playing_game = False
            self._state_of_game = config.StateOfGame.SCORE
            self._objects = []
            self._objects += self.after_game_menu_buttons
            print(self._scores)

    def example_of_game_2(self):
        if self._start_of_game:
            self._score = 0
            self._init_time = time.get_ticks()
            self._time_to_press = self._init_time + random.randint(100, 500)
            self._start_of_game = False
            self._objects.append(TextObject('Приготовься ловить блоки', True))
            self._time_to_play = time.get_ticks() + 3010

        if time.get_ticks() >= self._time_to_press and not self._playing_game:
            self._objects = []
            self._playing_game = True
            self._time_to_play = time.get_ticks() + random.randint(10000, 30000)

        if self._playing_game:
            if time.get_ticks() % 100 == 0:
                _b = GameObject((40, 40), config.BLACK)
                _b.set_x(random.randint(0, config.SCREEN_WIDTH))
                _b.set_y(random.randint(0, config.SCREEN_HEIGHT))
                self._objects.append(_b)
            if self._objects:
                for _obj in self._objects:
                    if _obj.rect.collidepoint(mouse.get_pos()):
                        self._objects.remove(_obj)
                        self._score += 1

        if time.get_ticks() > self._time_to_play:
            self._playing_game = False
            self._scores.append(self._score)
            self._state_of_game = config.StateOfGame.SCORE
            self._objects = []
            self._objects += self.after_game_menu_buttons
            print(self._scores)

    def _on_event(self, _event):
        if _event.type == constants.QUIT:
            self._running = False

        if _event.type == constants.KEYUP:
            if _event.key == constants.K_SPACE:
                self._space_is_pressed = True
        else:
            self._space_is_pressed = False

        for _but in self._buttons:
            if _but.is_touched() and (_but in self._objects) and _event.type == constants.MOUSEBUTTONUP:
                if _but.type == config.ButtonsType.START:
                    self._state_of_game = config.StateOfGame.GAME
                    self._objects = []
                    self._start_of_game = True
                    break
                elif _but.type == config.ButtonsType.SCORE:
                    self._state_of_game = config.StateOfGame.SCORE
                    self._objects = []
                    self._objects += self.after_game_menu_buttons
                    break
                elif _but.type == config.ButtonsType.QUIT:
                    self._running = False
                    break
                elif _but.type == config.ButtonsType.RESTART:
                    self._state_of_game = config.StateOfGame.MENU
                    self._objects = []
                    self._objects += self.main_menu_buttons
                    break

    def _on_cleanup(self):
        display.quit()

    def _on_render(self):
        self._display_surf.fill(config.WHITE)
        for _obj in self._objects:
            self._display_surf.blit(_obj.image, _obj.rect)
        display.flip()

    def start(self):
        self._on_init()
        while self._running:
            self._clock.tick(config.FPS)
            for _event in event.get():
                self._on_event(_event)
            self._on_loop()
            self._on_render()
        self._on_cleanup()


window = Window()
window.start()
