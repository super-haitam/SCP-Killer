import pygame
import platform
import player

pygame.init()

screen = pygame.display.set_mode((600,400))

running = True

player_imgl = pygame.image.load("assets/Playerright.png")
player_imgr = pygame.image.load("assets/Playerleft.png")

player = player.Player(player_imgr,player_imgl)
platform = platform.Platform()
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)    
    
    screen.fill((0,150,150))
    platform.draw_platform(screen)
    player.movement()
    player.draw_player(screen)

    pygame.display.flip()