from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.highscore =  int(file.read())
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High score : {self.highscore}",  align="center",font= ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode = "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.pendown()
        self.color("white")
        self.write("GAME OVER",align = "center",font = ("Arial", 24, "normal"))
