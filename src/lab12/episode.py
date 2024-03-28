''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''

import pygame
from pathlib import Path

from lab11.sprite import Sprite
from lab11.turn_combat import CombatPlayer, Combat
from lab11.pygame_ai_player import PyGameAICombatPlayer
from lab11.pygame_human_player import PyGameHumanCombatPlayer

def run_episode(playerOne, playerTwo):
    p1HP = playerOne.health
    p2HP = playerTwo.health

    p1WEAP = playerOne.weapon

    #Create list for tuples
    episode = []

    while p1HP > 0 or p2HP > 0:

        #Setup observation
        observation = (p1HP, p2HP)

        #Setup player weapon
        action = p1WEAP

        #Setup player reward
        reward = playerOne.reward

        #Setup turn
        turn = (observation, action, reward)

        #Add turn to episode
        episode.append(turn)

    return episode