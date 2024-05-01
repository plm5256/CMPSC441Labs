""" Create PyGameAIPlayer class here"""
import pygame
from lab11.turn_combat import CombatPlayer


class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if ord("0") <= event.key <= ord("9"):
                    return event.key
        return ord(str(state.current_city))  # Not a safe operation for >10 cities


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer:
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        while True:
            """
            > The agent will mimic the opponent's last choice
            :return: The last choice of the opponent.
            """
            if len(self.my_choices) == 0:
                return self.weapon

            return self.my_choices[-1]
