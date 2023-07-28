'''This code is a simple implementation of the classic Snake game using the Pygame library, which provides functionalities for game development. Let's go through the code step by step:

Importing Libraries: The code starts by importing the necessary libraries - pygame, random, Enum, and namedtuple.

Pygame Initialization: pygame.init() initializes all the modules required for Pygame.

Setting up Constants and Data Structures:

font: The font used for displaying the score on the screen.
Direction: An enumeration class representing the possible directions (RIGHT, LEFT, UP, DOWN) the snake can move.
Point: A named tuple representing a point on the game grid with x and y coordinates.
Color Constants: Several color constants are defined using RGB values.
BLOCK_SIZE: The size of each block or segment of the snake.
SPEED: The speed of the game, represented by the number of frames per second.
SnakeGame Class:

__init__: The constructor of the SnakeGame class initializes the game window, sets the initial state of the game (snake position, direction, score, etc.), and places the food on the game grid.

_place_food: This private method is used to place the food randomly on the game grid. The food position is chosen randomly within the game window and repositioned if it coincides with the snake's body.

play_step: This method represents a single step in the game. It handles user input, moves the snake, checks for collisions, updates the game UI, and returns the game status (game over or not) along with the current score.

_is_collision: This private method checks for collision conditions, such as hitting the game window's boundaries or colliding with the snake's body.

_update_ui: This private method updates the game display by drawing the snake, food, and the current score.

_move: This private method handles the movement of the snake based on the provided direction.

Game Loop:

The SnakeGame class is instantiated, creating the game window and setting up the initial game state.
The game runs in an infinite loop, where each iteration represents a single game step.
The game loop repeatedly calls the play_step method to advance the game.
If the game is over (the snake collides with something), the loop starts a new game by reinitializing the SnakeGame class with game = SnakeGame().
The loop keeps running until the user manually closes the game window.
Final Score:

Once the game loop exits (usually when the user closes the game window), the final score is printed.
Note: It seems there is a commented-out break statement in the code that could terminate the game loop if the user chooses to uncomment it. However, as it stands, the game loop will continue indefinitely, starting a new game each time the previous one ends.

To play the game, run the script, and a Pygame window will open with the Snake game. Use the arrow keys (left, right, up, down) to control the direction of the snake. Try to eat the food (red block) and grow the snake while avoiding collisions with the game window boundaries and the snake's body. The game will keep track of the score, and each time the snake collides, a new game will start, and the final score will be displayed once the game window is closed.





'''
import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.SysFont('calibri', 20)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

WHITE = (255, 255, 255)
RED = (248,143,147)
GREEN = (186,217,181)
FONT = (66,12,20)
BACK = (239,247,207)

BLOCK_SIZE = 20
SPEED = 15

class SnakeGame:
    
    def __init__(self, w=640, h=480):
        pygame.display.set_caption('Snake')
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        self._move(self.direction) 
        self.snake.insert(0, self.head)
        
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
            
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        
        self._update_ui()
        self.clock.tick(SPEED)
        return game_over, self.score
    
    def _is_collision(self):
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self):
        self.display.fill(BACK)
        
        for pt in self.snake:
            pygame.draw.rect(self.display, GREEN, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))

            
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))        
        text = font.render( str(self.score), True, GREEN)
        self.display.blit(text, [320, 5])
        pygame.display.flip()
        
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)
            

if __name__ == '__main__':
    game = SnakeGame()

    while True:

        game_over, score = game.play_step()
        
        if game_over == True:
            game = SnakeGame()
            print('Final Score', score)
#             break
        
    print('Final Score', score)
        
        
    pygame.quit()