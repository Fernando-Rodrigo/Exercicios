import pygame

pygame.mixer.init()
pygame.mixer.music.load('02 Wonderwall.mp3')
pygame.mixer.music.play()

x = input('Aperte enter para encerrar a música.')
