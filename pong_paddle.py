from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,postion):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(postion)
        self.shapesize(5,1)
    def go_up(self):
        new_y = self.ycor()+20
        
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
    
    
    
