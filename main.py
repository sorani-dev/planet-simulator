import pygame
import math

# Game window dimensions
WIDTH, HEIGHT = 750, 750

# Set pygame defaults
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Colors
WHITE = (255, 255, 255,)


class Planet(object):

    # Approximal Unit (Distance from a planet to the sun) in meters
    AU = 149.6e6 * 1000
    # Gravity
    G = 6.674258e-11
    # Scale down (1 meter to x pixels)
    SCALE = 250 / AU  # 1 AU = 100 pixels
    # Time to represent in the simulation (how much time has passed since last update)
    TIMESTEP = 3600 * 24  # One day

    def __init__(self, x: float, y: float, radius: float, color: set[int, int, int], mass: float) -> None:
        """Initialize

        Args:
            x (float): X Coordinate
            y (float): Y Coordinate
            radius (float): Planet radius
            color (set[int, int, int]): Planet color
            mass (float): Planet mass
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        # The sun does not go on an orbit
        self.sun = False
        # Planet's distance
        self.distance_to_sun = 0

        # Keep track of all the points this planet has travelled along
        self.orbit: list[float] = []

        # Velocity
        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, win: pygame.Surface) -> None:
        """Draw Planet on screen

        Args:
            win (pygame.Surface): the window to draw on
        """
        # Get the center of the screen
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + WIDTH / 2
        # Draw the Planet
        pygame.draw.circle(win, self.color, (x, y), self.radius)


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
