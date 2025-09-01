import random
from turtle import Turtle
from snake import COLOR

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.shapesize(1,1)
        self.color(random.choice(COLOR))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.setposition(new_x, new_y)
        new_color = random.choice(COLOR)
        self.color(new_color)