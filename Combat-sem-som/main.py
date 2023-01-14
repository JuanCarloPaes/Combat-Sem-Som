import pygame

from game import Game

pygame.mixer.pre_init(44100, 16, 2, 4096)  # frequency, size, channels, bduffer-size
pygame.init()  # turn all of pygame on.

game = Game()
game.loop()

pygame.quit()
