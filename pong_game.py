import turtle 
from pong_paddle import Paddle
from pong_ball import Ball
from pong_score import Scoreboard
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("THE PONG GAME")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard =Scoreboard()






screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")


game_is_on = True
while game_is_on:
    screen.update()
    screen.delay(1)
    ball.move()
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()
    if (ball.distance(r_paddle)<50 or ball.distance(l_paddle)<50) and (ball.xcor()>330 or ball.xcor()<-330):
        ball.bounce_x()

    if ball.xcor()> 380 :
        ball.reset_position_right()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_position_left()
        scoreboard.r_point()
        














screen.exitonclick()