from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        
        self.color('white')
        self.penup()
        self.hideturtle()

        self.goto(0,265)
        with open('high_score.txt') as f:
            self.high_score=int(f.read())
        
        self.update_scoreboard()


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
        
        
    def reset(self):
        if self.high_score<self.score:
            self.high_score=self.score
            with open('snake game\high_score.txt','w') as f:
                f.write(f'{self.high_score}')
        self.score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score={self.score}   High Score={self.high_score}",align='center',font=('Arial', 20, 'normal'))
  

    
        