import pygame
import sys
import os
pygame.font.init() #--> imports the timer font

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
player_image = pygame.image.load("emoji1.png")

emoji1_visible = True
emoji2_visible = True

# Load and scale background image & reload the background
background = pygame.image.load("testbg.webp") #--> loads an image instead of a rectangle
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) #--> Refreshes the background

# player image
player_image = pygame.image.load("Steve.png")

# emoji images
emoji1_image = pygame.image.load("emoji1.png")
emoji2_image = pygame.image.load("emoji2.png")

# player location and speed
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 4

#Creating object rects
emoji_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 30, 30)

# Incrementing the score counter
score = 0
score_increment = 1

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

    p_rec = pygame.Rect(player_x, player_y, player_image.get_width(),player_image.get_height())
    e1_rec = pygame.Rect(180,40, emoji1_image.get_width(),emoji1_image.get_height())
    e2_rec = pygame.Rect(425,147, emoji2_image.get_width(),emoji2_image.get_height())
    #Score updating - emoji 1
    if p_rec.colliderect(e1_rec) and emoji1_visible==True:
        emoji1_visible = False
        score += score_increment
    

#make a rectangle for our images w/ same width and height and X ,Y


    if p_rec.colliderect(e2_rec) and emoji2_visible==True:
        emoji2_visible = False
        score += score_increment


    screen.blit(background, (0, 0))  # draw background Image ("Block Image Transfer" = blit)
    # B. draw player
    screen.blit(player_image, (player_x, player_y))  # draw player
    if emoji1_visible == True:
        screen.blit(emoji1_image, (180,40))
    if emoji2_visible == True:
        screen.blit(emoji2_image, (425, 147))

    #Score font to be visible
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()