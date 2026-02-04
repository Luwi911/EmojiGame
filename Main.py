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
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) #--> Refreshes the background

# player image
player_image = pygame.image.load("Steve.png")

# emoji image
emoji1_image = pygame.image.load("emoji1.png")

# player location and speed
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 4

#movement variables (NEW)
player_dx = 0 #--> "difference in X" (starts @ 0 bc it's not moving at first)
player_dy = 0 #--> "difference in Y"


end = False
while not end:
    #---------------------------------------------------------------
    # UPDATE: 
    #---------------------------------------------------------------
    # A. Event handling: Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

        # start movement on key press (moves by 1 space)
        if event.type == pygame.KEYDOWN:
            # arrow keys
            if event.key == pygame.K_LEFT:
                player_dx = -player_speed #-->dx is CHANGING (-speed to go LEFT)
            if event.key == pygame.K_RIGHT: #-->dx is CHANGING (+speed to go RIGHT)
                player_dx = player_speed
            if event.key == pygame.K_UP:
                player_dy = -player_speed #--> (-y is GOING UP)
            if event.key == pygame.K_DOWN: #--> (+y is GOING DOWN)
                player_dy = player_speed
            # Escape key 
            if event.key == pygame.K_ESCAPE:
                end = True
        # end movement on key release
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_dx = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player_dy = 0

    # B. Game logic: Update player position based on input
    player_x += player_dx 
    player_y += player_dy


    screen.blit(background, (0, 0))  # draw background Image ("Block Image Transfer" = blit)
    # B. draw player
    screen.blit(player_image, (player_x, player_y))  # draw player
    screen.blit(emoji1_image, (0,0))

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()