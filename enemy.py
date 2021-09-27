from turtle import Turtle

Xs = [240, 210, 180, 150, 120, 90, 60, 30, 0, -30, -60, -90, -120, -150, -180, -210, -240]
Ys = [240, 210, 180, 150, 120, 90, 60, 30]

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.enemies = []
        for x in Xs:
            for y in Ys:
                self.create_enemy(x, y)


    def create_enemy(self, xpos, ypos):
        new_enemy = Turtle('square')
        new_enemy.setheading(180)
        new_enemy.shapesize(1)
        new_enemy.color('white')
        new_enemy.up()
        new_enemy.goto(xpos, ypos)
        self.enemies.append(new_enemy)

