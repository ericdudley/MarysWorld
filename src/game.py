import pygame
import os
from player import Player, PlayerState
from block import Block
from threading import Timer


def main():

    pygame.init()

    logo = pygame.image.load(os.path.join('img', 'logo.png'))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Mary's World")

    width = 800
    height = 600

    screen = pygame.display.set_mode((width, height))

    game_is_running = True

    player = Player()
    blocks = []

    for i in range(16):
        blk = Block()
        blk.pos.x = i * 50
        blk.pos.y = height
        blocks.append(blk)

    while game_is_running:
        player.Update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.vel.x = -0.2
                    player.SetState(PlayerState.MOVE)
                elif event.key == pygame.K_RIGHT:
                    player.vel.x = 0.2
                    player.SetState(PlayerState.MOVE)
                elif event.key == pygame.K_UP:
                    player.Jump()
                elif event.key == pygame.K_DOWN:
                    player.SetState(PlayerState.FALL)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.vel.x = 0
                    player.SetState(PlayerState.IDLE)
                elif event.key == pygame.K_RIGHT:
                    player.vel.x = 0
                    player.SetState(PlayerState.IDLE)
            if event.type == pygame.QUIT:
                game_is_running = False
        screen.fill((0, 0, 0))
        player_sprite = pygame.transform.scale(player.GetSurface(), (100, 100))
        screen.blit(player_sprite, (player.pos.x, player.pos.y))
        fall = True
        for blk in blocks:
            screen.blit(blk.GetSurface(), (blk.pos.x, blk.pos.y))
            if blk.GetRect().colliderect(player.GetRect()):
                fall = False

        if fall:
            player.SetState(PlayerState.FALL)
        elif player.state == PlayerState.FALL:
            player.vel.y = 0
            player.SetState(PlayerState.IDLE)

        pygame.display.update()


if __name__ == "__main__":
    main()
