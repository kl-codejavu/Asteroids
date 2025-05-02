# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

import sys

import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x= SCREEN_WIDTH /2
    y= SCREEN_HEIGHT /2

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y, shots)
    asteroid_field = AsteroidField()
       
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # Inside the game loop, right after screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()
        
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
           


if __name__ == "__main__":
    main()