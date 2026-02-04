import pygame

pygame.init()

#Estalish screen WIDTH & HEIGHT
WIDTH, HEIGHT = (500, 400)
FPS = 60 #--> Smoother movement
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Emoji Game Jam")
clock = pygame.time.Clock()

#Defining colours 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Defining Objects
bg_image = pygame.image.load("testbg.webp")
player_image = pygame.image.load("Steve.png")

# Load and scale background image
background = pygame.image.load("testbg.webp") #--> loads an image instead of a rectangle
# player image
player_image = pygame.image.load("Steve.png")