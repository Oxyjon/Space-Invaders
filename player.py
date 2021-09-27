from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.up()
        self.color('white')
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

