import sys
import pygame
from ship import Ship
import game_functions as gf
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_evens(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
