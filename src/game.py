import pygame
import os
from Player import Player


def main():

    pygame.init()

    logo = pygame.image.load(os.path.join('img', 'logo.png'))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Mary's World")

    screen = pygame.display.set_mode((800, 600))

    game_is_running = True

    player = Player()

    while game_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
        screen.fill((0, 0, 0))
        screen.blit(player.getSprite(), (50, 50))

        pygame.display.update()


if __name__ == "__main__":
    main()
