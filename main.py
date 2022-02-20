import pygame
import math

# Game window dimensions
WIDTH, HEIGHT = 800, 800

# Set pygame defaults
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Colors
WHITE = (255, 255, 255,)
YELLOW = (255, 255, 0,)
BLUE = (100, 149, 237,)
RED = (188, 39, 50,)
DARK_GREY = (80, 78, 81,)


class Planet(object):

    # Approximal Unit (Distance from a planet to the sun) in meters
    AU = 149.6e6 * 1000
    # Gravity
    G = 6.674258e-11
    # Scale down (1 meter to x pixels)
    SCALE = 250 / AU  # 1 AU = 100 pixels
    # Time to represent in the simulation (how much time has passed since last update)
    TIMESTEP = 3600 * 24  # One day

    def __init__(self, x: float, y: float, radius: int, color: set[int, int, int], mass: float) -> None:
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

    # The Sun
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    # The Earth
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)

    # Mars
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)

    # Mercury
    mercury = Planet(0.387*Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)

    # Venus
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    # Planet List
    planets = [sun, earth, mars, mercury, venus]

    while run:
        # Framerate refresh
        clock.tick(60)

        # # Draw on screen
        # WIN.fill(WHITE)

        # Manage events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Draw Planets
        for planet in planets:
            planet.draw(WIN)

        # Update display
        pygame.display.update()

    pygame.quit()


# Start game
main()
