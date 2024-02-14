import turtle
from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()          
screen.setup(width=600,height=600)

screen.title("Welcome to BH")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.move_u,'Up')
screen.onkey(snake.move_d,'Down')
screen.onkey(snake.move_l,'Left')
screen.onkey(snake.move_r,'Right')


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.squ[0].distance(food)<15:
        food.refresh()
        snake.extend( )
        scoreboard.increase_score()
         
    if snake.squ[0].xcor() >285 or snake.squ[0].xcor() < -285 or snake.squ[0].ycor() >285 or snake.squ[0].ycor() < -285:
        
        scoreboard.reset()
        snake.reset_s()
        

    for squares in snake.squ:
        if squares==snake.squ[0]:
            pass
        elif snake.squ[0].distance(squares)<10:
            
            scoreboard.reset()
            snake.reset_s()


        


screen.exitonclick()        