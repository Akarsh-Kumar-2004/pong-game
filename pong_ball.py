from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(1,1)
        self.goto(0,0)
        self.distance_change_x = 10
        self.distance_change_y = 10
        
    def move(self):
        time.sleep(0.1)
        new_x = self.xcor()+self.distance_change_x
        new_y = self.ycor()+self.distance_change_y
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.distance_change_y *=-1
    def bounce_x(self):
        self.distance_change_x *= -1
    def reset_position_right(self):
        self.goto(0,0)
        self.bounce_x()
    def reset_position_left(self):
        self.goto(0,0)
        self.bounce_x()
        
        