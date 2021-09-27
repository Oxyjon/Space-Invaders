import time
from turtle import Turtle

class Bullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.bullets = []
        self.hideturtle()
        self.shapesize(0.5)
        self.penup()
        self.goto(position)
        self.fired = False

    def fire(self):
        self.showturtle()
        self.fired = True

    def ready(self, position):
        self.hideturtle()
        self.goto(position)
        self.fired = False





