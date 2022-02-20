from __future__ import annotations

import math

import pygame

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
        self.orbit: list[set[float, float]] = []

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

        # Draw the Planet orbit
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + WIDTH / 2
                updated_points.append((x, y))
            # Draw the updated points as a line
            pygame.draw.lines(WIN, self.color, False, updated_points, 2)

        # Draw the Planet
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other: Planet) -> tuple[float, float]:
        """Force of attraction from a Planet to a Planet

        Args:
            other (Planet): the other Planet
        """
        other_x, other_y = other.x, other.y
        # Distance between the two Planets
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # Update the distance to the sun if the sun
        if other.sun:
            self.distance_to_sun = distance

        force_of_attraction = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force_of_attraction
        force_y = math.sin(theta) * force_of_attraction
        return force_x, force_y

    def update_position(self, planets: list[Planet]):
        """Update the Planets positions depending on this Planet's place

        Args:
            planets (list[Planet])
        """
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            # Calculate the total force on x and y axis
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # Increase velocity (F = m / a) over a period of time
        self.x_velocity += total_fx / self.mass * self.TIMESTEP
        self.y_velocity += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP
        self.orbit.append((self.x, self.y))

# assert Planet.__annotations__ == {'other': 'Planet'}


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
    earth.y_velocity = 29.783 * 1000

    # Mars
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_velocity = 24.077 * 1000

    # Mercury
    mercury = Planet(0.387*Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_velocity = -47.4 * 1000

    # Venus
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_velocity = -35.02 * 1000

    # Planet List
    planets = [sun, earth, mars, mercury, venus]

    while run:
        # Framerate refresh
        clock.tick(60)

        # # Draw background on screen
        WIN.fill((0, 0, 0))

        # Manage events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Draw Planets
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        # Update display
        pygame.display.update()

    pygame.quit()


# Start game
main()
