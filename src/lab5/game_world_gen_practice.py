'''
Lab 5: PCG and Project Lab

This a combined procedural content generation and project lab. 
You will be creating the static components of the game that will be used in the project.
Use the landscape.py file to generate a landscape for the game using perlin noise.
Use the lab 2 cities_n_routes.py file to generate cities and routes for the game.
Draw the landscape, cities and routes on the screen using pygame.draw functions.
Look for triple quotes for instructions on what to do where.
The intention of this lab is to get you familiar with the pygame.draw functions, 
use perlin noise to generate a landscape and more importantly,
build a mindset of writing modular code.
This is the first time you will be creating code that you may use later in the project.
So, please try to write good modular code that you can reuse later.
You can always write non-modular code for the first time and then refactor it later.
'''

import sys
import pygame
import random
import numpy as np
from landscape import get_landscape

from pathlib import Path
sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes


# TODO: Demo blittable surface helper function

''' Create helper functions here '''

#Blittable surface function
def createblittablesurface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    return pygame.surfarray.make_surface(landscape[:, :, :3]) 

#Cities function
def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of cities to be generated 
    and returns a list of cities with their x and y coordinates. The cities are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of cities to generate
    :return: A list of tuples, each representing a city, with random x and y coordinates.
    """
    # Consider the condition where x size and y size are different

    cities = []

    for i in range(n_cities):

        cities.append((random.randrange(0,size[0]), random.randrange(0, size[1])))

    return cities

# Routes function
def get_routes(city_names):
    """
    It takes a list of cities and returns a list of all possible routes between those cities. 
    Equivalently, all possible routes is just all the possible pairs of the cities. 
    
    :param cities: a list of city names
    :return: A list of tuples representing all possible links between cities/ pairs of cities, 
            each item in the list (a link) represents a route between two cities.
    """

    routes = []

    for i in city_names:

        for j in city_names:

            if i != j:
                routes.append((i,j))
    
    return routes

def getCoords(i):
    iRoute = routes[i]

    startName = iRoute[0]
    endName = iRoute[1]

    startCoords = city_locations_dict[startName]
    endCoords = city_locations_dict[endName]
    
    return [startCoords,endCoords]

if __name__ == "__main__":

    pygame.init()
    size = width, height = 640, 480
    black = 1, 1, 1

    screen = pygame.display.set_mode(size)

    pygame_surface = createblittablesurface(size)

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta',
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    city_locations = [] 
    routes = []

    ''' Setup cities and routes in here'''
    city_locations = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(city_names)

    city_locations_dict = {name: location for name, location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10] 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))

        ''' draw cities '''
        for i in city_locations:
            pygame.draw.circle(screen, (220,250,230), i, 1)
        ''' draw first 10 routes '''
        
        iter = 0

        for i in routes:
            
            coords = getCoords(iter)
            start = coords[0]
            end = coords[1]
            iter += 1

            pygame.draw.line(pygame_surface,(220,250,230),start,end)

        pygame.display.flip()
