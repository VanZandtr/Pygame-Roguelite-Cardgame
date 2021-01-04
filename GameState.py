import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    WIZARD = 2
    SHOP = 3