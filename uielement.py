import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

""" An user interface element that can be added to a surface

        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            is_text = used to remove mouseover effect for text elements
            action - the gamestate change associated with this button
            
"""
class UIElement(Sprite):
    def __init__(self, center_position, text="", font_size=0, bg_rgb=(0, 0, 0), text_rgb=(0, 0, 0), remove_highlight=False, image_path="", action=None):
        
        self.mouse_over = False
        self.remove_highlight = remove_highlight

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action
            

        super().__init__()    

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    """ Updates the mouse_over variable and returns the button's
            action value when clicked.
    """
    def update(self, mouse_pos, mouse_up):
        if self.remove_highlight == False:
            if self.rect.collidepoint(mouse_pos):
                self.mouse_over = True
                if mouse_up:
                    return self.action
            else:
                self.mouse_over = False
            
    """ Draws element onto a surface """
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    # def show_imported_image(image_name, x, y):
    #     new_img = pygame.image.load(image_name)
    #     surface.blit(image_name, x, y)