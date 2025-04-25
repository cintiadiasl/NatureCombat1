#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.timeout = 20000  # equivale a 20 segundos

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')  # música importada para o jogo
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # clock vai fazer com que a função rode sempre em um tempo específico
        while True:
            clock.tick(60)  # apresenta quanto de fps será utilizado, no caso, 60 fps (quanto maior o fps, mais rápido irá executar)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():  # Gerenciado de eventos que irá permitir fechar a janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}', COLOR_WHITE,
                            (10, 5))  # tempo de duração das fases
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE,
                            (10, WIN_HEIGHT - 35))  # vai fazer a impressão do fps em tempo real
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE,
                            (10, WIN_HEIGHT - 20))  # apresenta as entidades criadas
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
