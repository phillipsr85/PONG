from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("cyan")
screen.title("Pong")

##prevents us from seeing paddle moving to starting position, need a screen updat in a while loop
screen.tracer(0)


r_paddle =Paddle((350,0))
l_paddle =Paddle((-350,0))
ball= Ball()
scoreboard =Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
   #updates tracer
    screen.update()


    ball.move()

    ##bounce off wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    ##Bounce off paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()


    ##Ball out of bounds

    if ball.xcor() > 380:
        scoreboard.p1_score()
        ball.refresh()


    ##Ball out of bounds
    if ball.xcor() < -380:
        scoreboard.p2_score()
        ball.refresh()

    ##Game over

    if scoreboard.score_1 == 5:
        winner = "Player 1"
        scoreboard.game_over(winner)
        game_is_on = False
    elif scoreboard.score_2 ==5:
        winner = "Player 2"
        scoreboard.game_over(winner)
        game_is_on = False







screen.exitonclick()
