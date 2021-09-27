import turtle
from turtle import Screen
from player import Player
from enemy import Enemy
from bullet import Bullet
from score import Score
import time

#init screen
screen = Screen()
#screen setup
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0, 0)

#Init player
player = Player((0, -265))
enemy = Enemy()
bullet = Bullet((player.xcor(), player.ycor()))
score = Score()

#Screen listen for clicks
screen.listen()
screen.onkey(player.go_left, 'a')
screen.onkey(player.go_right, 'd')


def game():
    game_running = True
    move_speed = 1
    bullet_speed = 20

    while game_running == True:
        screen.onkey(bullet.fire, 'space')
        time.sleep(0.05)
        screen.update()
        # Fired bullet
        if bullet.fired == True:
            y = bullet.ycor()
            y += bullet_speed
            bullet.sety(y)
        if bullet.ycor() > 280:
            bullet.ready((player.xcor(), player.ycor()))

        # Enemy movement
        # Move left
        for e in enemy.enemies:
            x = e.xcor()
            x += move_speed
            e.setx(x)
            # right side
            if e.xcor() >= 300:
                # Drop 1 row size
                for e in enemy.enemies:
                    y = e.ycor() - 30
                    e.sety(y)
                #Reverse the speed
                move_speed *= -1
            #Left side
            if e.xcor() <= -300:
                #Drop 1 row size
                for e in enemy.enemies:
                    y = e.ycor() - 30
                    e.sety(y)
                #Reverse speed again
                move_speed *= -1

    #Detect collision
        for e in enemy.enemies:
            if e.ycor() - 20 <= bullet.ycor() <= e.ycor() + 20 and (e.xcor() - 20 < bullet.xcor() < e.xcor() + 20):
                e.goto(500, 500)
                score.add_point()
                bullet.ready((player.xcor(), player.ycor()))
                enemy.enemies.remove(e)

        #Game Over
        for e in enemy.enemies:
            if e.ycor() <= -265:
                score.game_over()
                game_running = False

        # if there are no more enemy objects
        if len(enemy.enemies) == 0:
            score.win()
            turtle.done()
            game_running = False

game()
#close game
screen.exitonclick()