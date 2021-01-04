# Pygame-Roguelite-Cardgame
## Intro
Attempt at a roguelite deckbuilding game similar to others in its genre.

## Additions to genre / Future ideas
* Attempt at adding additional game elements that extend outside of the game loop (i.e. more saved progress, gear, cards, ...)
* Outside game loop shop
* Additonal support benefits (/negatives): items, artificats, one-use items, allies,...)

## Scripts
* main.py: Runs main game loop and holds buttons, texts, and images for the different screens
* uielement.py: "factory-ish" class to make UI element creations easy and nicer looking in main.py
* images/: holds imported images
* Player.py: stores player data (health, gold, class, etc.)
* Gamestate.py: list of gamestate options that buttons use to change scenes

## 1/3/2021 - Initial Commit
* Added base code pulled from web for menu creation
* Added unimplemented shop, attack, use item buttons and basic flow 
* Added basic image adder and onclick

## Future Work
* Combat
* Items and Cards
* Allies (pets?)
* One Use Items
* Store purchasing
* In game Experience/Leveling and Game Payout design
* Saved Progress and out-of-game exp/leveling design

# Game Screenshots
![Alt text](/Screenshots/Intro_Screen.jpg?raw=true "Rough Intro Screen")
![Alt text](/Screenshots/Choose_Class_Screen.jpg?raw=true "Rough Choose Class Screen")
![Alt text](/Screenshots/Main_Game_Loop.jpg?raw=true "Rough Screen for the main game loop")
