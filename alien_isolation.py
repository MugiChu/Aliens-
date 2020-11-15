import sys
import pygame as pg
from settings import Settings
from ship import Ship
import game_func as gf


def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pg.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pg.display.flip()


run_game()