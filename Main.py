import pygame

pygame.init()

#Estalish screen WIDTH & HEIGHT
WIDTH, HEIGHT = (500, 400)
FPS = 60 #--> Smoother movement
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Emoji Game Jam")
clock = pygame.time.Clock()