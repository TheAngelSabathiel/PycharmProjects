from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Xander's Snake")
screen.tracer(0)

xander = Snake("white","square")
# jomari = Snake("pink","circle")
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(xander.up,"Up")
screen.onkey(xander.down, "Down")
screen.onkey(xander.right, "Right")
screen.onkey(xander.left, "Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    xander.move()

    # Checking whether the turtle eats the food
    if xander.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.refresh_score()
        xander.add_segment()

    # Checking whether the turtle collides with the wall
    if abs(xander.segments[0].xcor()) >= 300 or abs(xander.segments[0].ycor()) >= 300:
        game_is_on = False

    # Checking whether the turtle collides with its tail
    for seg in xander.segments[1:]:
        if xander.segments[0].distance(seg) < 15:
            game_is_on = False


scoreboard.game_over()

screen.exitonclick()