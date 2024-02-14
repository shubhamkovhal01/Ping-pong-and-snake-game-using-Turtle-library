import turtle
from turtle import Screen,Turtle
position=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

screen=Screen()
class Snake:

    def __init__(self):
        self.squ=[]
        self.create_snake()
        self.head=self.squ[0]

    def create_snake(self):
        for i in range(0,3):
            self.add_tail(position[i])

    def add_tail(self,position):
        new_square=Turtle(shape='square')
        screen.bgcolor('black')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.squ.append(new_square)

    def reset_s(self):
        for squares in self.squ:
            squares.goto(1000,1000)
        self.squ.clear()
        self.create_snake()
        self.head=self.squ[0]

    def extend(self):
        self.add_tail(self.squ[-1].position())

    def move(self):
        for squar in range(len(self.squ)-1,0,-1):
            new_x=self.squ[squar-1].xcor()
            new_y=self.squ[squar-1].ycor()
            self.squ[squar].goto(new_x,new_y )
        self.squ[0].forward(20)

    def move_r(self):
        if self.squ[0].heading()!=LEFT:
            self.squ[0].setheading(RIGHT)
    def move_l(self):
        if self.squ[0].heading()!=RIGHT:
            self.squ[0].setheading(LEFT)
    def move_u(self):
        if self.squ[0].heading()!=DOWN:
            self.squ[0].setheading(UP)
    def move_d(self):
        if self.squ[0].heading()!=UP:
            self.squ[0].setheading(DOWN)
            
        
        