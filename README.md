# Final Project Report
## CMPSC 441 and GAME 450

Abstract
The semester-long project of creating an AI adventure game has been a tough challenge. I had experience with AI models in the past, but nothing as in-depth as this. Python is one of the most widely chosen in the emerging field of AI utilization due to its ease of use and wide array of libraries. While my knowledge of python was nearly as limited as my knowledge of AI, this project has helped me become better acquainted with the language. There were several components that were necessary for this project that we had developed gradually throughout the semester. While they each presented their own unique challenges, they were each implemented in time.

Component List:
1. Cities and routes between cities
2. Player movement and money accounting
3. Landscape
4. Turn based fight simulator
5. An AI Agent able to play this game
6. An additional AI technique (Journalling mechanism, visual enhancements to the game etc.)


Problems solved:
The component of the game which generates cities and routes was one of the first created. There needs to be locations the player can travel to on the map. By using random generation, a list of city location are able to be generated for the world. The function takes in a size of the map and the number of cities to generate, and then outputs a list of coordinate pairs for each city. The routes are used to define which cities allow travel for the player. The function which generates the routes takes in the list of city names, and then generates a list of routes for what city goes to what. This component allows for there to be a system of travel in the game the player can utilize.
The component for the game which tracks player movement and money accounting allows for checking if a travel move is legal in the game, and manages the cost of travel so the player must prioritize funds when moving between cities. The function which gets the cost of the route takes in a route returns the change in elevation which is used to calculate the cost of travel. Since the elevation is being used to calculate cost, it made sense to use the relative change in elevation to act as the metric. Within the players action is a check to see if a move can be made by checking if the proposed start city and destination city is an existing route. If it is the player may travel along it, if not the player may not.
The component for landscape generation uses the perlin noise library to generate the map. The function to get the elevation takes in the size of the map and the number of octaves to generate an array of elevation values. Then a function takes in the elevation values and a cmap to create and RGBA representation as a map with difference in color to represent the difference in relative elevation
The turn based combat component allows for there to be interaction between the player and an ai agent. When the game runs combat, the game runs combat so long as and end condition is not met. The game creates new round, then has each player take their turn. Within each turn, there is a decision array where the players choose a weapon type, then the game calculates damage based on the types chosen. Then outputs the health values for each player. It then checks a win condition, if it is met by one player losing all their health, then the combat concludes, if not combat continues.

The component of the game which has an AI agent play allows for the computer to provide an opponent for the user in combat. The AI agent may choose their weapon selecting strategy in combat of one of the three weapon types. The component was similar to the rock, paper, scissors lab, where the AI agent for the game was either a random choice, single choice, or a mimic choice. I had the AI agent mimic the players last combat choice.

For the component of the game we were allowed to choose ourselves to add, I included a module where the game can create contextual text generation. So there player feeds in a question or phrase. And the game will generate addition content relating to it. So if they wanted to know more about city or object in the game, the game can generate additional lore/dialogue or flavor about the world that the player can read. 

Appendix:
Input Given: Example used in testing: context = "Deep Learning is a sub-field of Artificial Intelligence."
Output received: "Deep Learning is a sub-field of Artificial Intelligence. It was an early and widely recognized topic in learning theory, and has received quite a lot of attention over the years. The term artificial intellgence is quite often used to desribe a system or machine that can be."



