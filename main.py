import pygame as pg
from game.game import Game

def main():
    running = True
    playing = True
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((1800, 980), flags=pg.RESIZABLE)
    clock = pg.time.Clock()

    # implement menus

    # implement game
    game = Game(screen, clock)

    while running:
        # start menu

        while playing:
            # game loop
            game.run()


if __name__ == '__main__':
    main()