import pygame
import math

# Game window dimensions
WIDTH, HEIGHT = 750, 750

# Set pygame defaults
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Colors
WHITE = (255, 255, 255,)


def main():
    """Runs the game"""
    # Is the game running?
    run = True
    # For screen refresh
    clock = pygame.time.Clock()

    while run:
        # Framerate refresh
        clock.tick(60)

        # # Draw on screen
        # WIN.fill(WHITE)

        # # Update display
        # pygame.display.update()

        # Manage events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


# Start game
main()
