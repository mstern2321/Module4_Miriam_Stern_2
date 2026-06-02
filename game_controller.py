from snake import Snake
from food import  Food
from scoreboard import Scoreboard
from turtle import Screen

class GameController:
    """
    Controls the Snake game
    """
    def __init__(self, screen, snake: Snake, food: Food, is_game_on: bool, scoreboard: Scoreboard) -> None:
        """
        Gives the objects their starting values
        """
        self.screen = screen


        self.snake = snake
        self.food = food
        self.is_game_on = is_game_on
        self.scoreboard = scoreboard


    def setup_bindings(self):
        """
        Makes the screen listen for different keys and calls the corresponding method
        """
        self.screen.listen()

        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")


    def run_game_loop(self):
        """
        Runs the game loop as long as is_game_on is True
        """

        if not self.is_game_on:
            return
        self.screen.update()
        self.snake.move()
        self.check_food_collision()

        if self.check_wall_collision() or self.check_self_collision(): # If there is a collision the game ends
            self.game_over()
            return

        self.screen.ontimer(self.run_game_loop, 120) # Slows down the movement so you can see it






    def check_food_collision(self):
        """
        Checks if snake collides with the food and then grows the snake and increases the player's score.
        """
        if self.snake.head.distance(self.food) < 15: # If the distance between the snake and the food is less than 15
            self.food.refresh() # another food is placed on the screem
            self.snake.grow() # the snake grows
            self.scoreboard.increase_score() # the player gets a point



    def check_wall_collision(self):
        """
        Checks if the player collides with any of the walls and returns True otherwise it returns False
        """
        if self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290 or self.snake.head.xcor() > 340 or self.snake.head.xcor() < -340:
                return True
        return False



    def check_self_collision(self):
        """
        Checks if snake collides with itself and returns True
        """
        for segment in self.snake.segments[1:]: # Loops through all segments of snake except first which is the head
            if self.snake.head.distance(segment) < 15: # if the distance between the head and the segment is less than 15
                return True
        return False


    def game_over(self):
        """
        calls the game_over method uf there is a collision  
        """
        self.is_game_on = False
        self.scoreboard.game_over()



