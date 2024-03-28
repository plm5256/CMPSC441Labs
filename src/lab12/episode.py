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

from lab11.turn_combat import Combat
from lab11.pygame_human_player import PyGameHumanCombatPlayer
from lab11.pygame_combat import PyGameComputerCombatPlayer, run_turn

def run_episode(playerOne, playerTwo):

    #Create list for tuples
    episode = []

    currentGame = Combat()

    #Setup Players
    player = PyGameHumanCombatPlayer(playerOne)
    opponent = PyGameComputerCombatPlayer(playerTwo)

    # Main Game Loop
    while not currentGame.gameOver:
        
        #Setup player weapon before turn begins
        action = player.weapon_selecting_strategy(player)

        #Run Combat turn
        run_turn(currentGame, player, opponent)

        #Setup observation: Get health values after turn concludes
        observation = (player.health, opponent.health)

        #Setup player reward
        reward = currentGame.checkWin(player, opponent)

        #Record the turn as a tuple
        turn = (observation, action, reward)

        #Add turn to list for the episode
        episode.append(turn)

    #Return the entire episode once combat concludes
    return episode