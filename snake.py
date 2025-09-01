from turtle import Turtle
import random

SHAPE = "circle"
COLOR = ["red","blue","green","yellow","white","purple","brown"]
STARTING_COR = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
RIGHT = 0
UP = 90
LEFT = 180

class Snake:
    def __init__(self):
        self.new_boxes = []
        self.create_snake()
        self.head = self.new_boxes[0]

    def create_snake(self):

        for position in STARTING_COR:
            new_box = Turtle(shape=SHAPE)
            new_box.penup()
            new_box.goto(position)
            new_box.color(random.choice(COLOR))
            new_box.speed(0)
            self.new_boxes.append(new_box)

    def increase_length(self):
        next_box = Turtle(shape=SHAPE)
        next_box.speed("fastest")
        next_box.penup()
        next_box.goto(500,500)          # This stop the dot to create an animation before it go to last position

        next_box.color(random.choice(COLOR))
        self.new_boxes.append(next_box)




    def move(self):
        
        for number in range(len(self.new_boxes) - 1, 0, -1):
            new_x = self.new_boxes[number - 1].xcor()
            new_y = self.new_boxes[number - 1].ycor()
            self.new_boxes[number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)



    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)