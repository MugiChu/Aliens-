import sys
import pygame as pg
import game_func as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pg.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pg.display.flip()


run_game()