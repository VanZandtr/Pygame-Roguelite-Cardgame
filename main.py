import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates

from uielement import UIElement
from Player import Player
from GameState import GameState

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
player = Player()

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    print(player._class)
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = select_class(screen, player)
            
        if game_state == GameState.WIZARD:
            player._class = "Wizard"
            game_state = play_game(screen,player)
            
        if game_state == GameState.SHOP:
            game_state = open_shop(screen, player)

        if game_state == GameState.QUIT:
            pygame.quit()
            return
            


def title_screen(screen):
    btn_array = []
    
    start_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    btn_array.append(start_btn)
    
    shop_btn = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Shop",
        action=GameState.SHOP,
    )
    btn_array.append(shop_btn)
    
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    btn_array.append(quit_btn)
    
    buttons = RenderUpdates(btn_array)

    return game_loop(screen, buttons)

def select_class(screen, player):
    
    wizard_button = UIElement(
        center_position=(400, 300),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Wizard",
        action=GameState.WIZARD,
    )
    
    return_btn = UIElement(
        center_position=(130, 550),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    buttons = RenderUpdates(return_btn, wizard_button)

    return game_loop(screen, buttons)

def play_game(screen, player):
    img_array= []
    ele_array = []
    
    #images
    wizard_img = pygame.image.load("./images/wizard.jpg")
    wizard_img.convert()
    wizard_img_rect = wizard_img.get_rect()
    wizard_img_rect.centerx = 300
    wizard_img_rect.centery = 300
    print(wizard_img_rect.center)
    image_1 = [wizard_img, wizard_img_rect]
    img_array.append(image_1)
    
    #text
    health_text = UIElement(
        center_position=(400, 550),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f"Health: ({player.health})",
        remove_highlight=True,
        action=None,
    )
    ele_array.append(health_text)
    
    #buttons
    attack_btn = UIElement(
        center_position=(750, 525),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f" Attack ",
    )
    ele_array.append(attack_btn)
    
    use_skill_btn = UIElement(
        center_position=(750, 550),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f" Use Skill ",
    )
    ele_array.append(use_skill_btn)
    
    show_inventory_btn = UIElement(
        center_position=(70, 525),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f" Inventory ",
    )
    ele_array.append(show_inventory_btn
                     )
    return_btn = UIElement(
        center_position=(130, 550),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    ele_array.append(return_btn)

    buttons = RenderUpdates(ele_array)

    return game_loop(screen, buttons, img_array)

def open_shop(screen, player):
    show_inventory = UIElement(
        center_position=(70, 525),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f" Inventory ",
    )
    
    return_btn = UIElement(
        center_position=(130, 550),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    
    buttons = RenderUpdates(return_btn, show_inventory)
    
    return game_loop(screen, buttons)
    
""" Handles game loop until an action is return by a button in the
        buttons sprite renderer.
"""
def game_loop(screen, elements, images=[]):
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                x, y = event.pos
                mouse_up = True
                for i in images:
                    if i[1].collidepoint(x, y):
                        print("image click")

        screen.fill(BLUE)

        for ele in elements:
            ui_action = ele.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
        elements.draw(screen)
        
        for image in images:
            screen.blit(image[0], image[1])
        
        pygame.display.flip()





if __name__ == "__main__":
    main()