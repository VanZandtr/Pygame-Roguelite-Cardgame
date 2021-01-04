import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates

""" Stores information about a player """
class Player:
    def __init__(self, gold=0, health=100, level=1, _class=None):
        self.gold = gold
        self.health = health
        self.level = level
        self._class = _class