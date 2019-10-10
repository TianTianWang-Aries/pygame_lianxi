# -*- coding: utf-8 -*-
__author__ = 'Tami'
__date__ = '2019-09-26 12:48'
import sys
import pygame
from lianxi_pygame.ship import Ship
from lianxi_pygame.settings import Settings


def run_game():
    screen = pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("blue window")

    #创建一艘飞船
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都会重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
