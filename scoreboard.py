from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier',24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.goto(-200,265)
        self.color("black")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.write(f"P1Score: {self.score_1}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(200,265)
        self.write(f"P2Score: {self.score_2}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()



    def update_score(self):
        self.clear()
        self.goto(-200, 265)
        self.write(f"P1Score: {self.score_1}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(200, 265)
        self.write(f"P2Score: {self.score_2}", move=False, align=ALIGNMENT, font=FONT)

    def p1_score(self):
        self.score_1 +=1
        self.update_score()

    def p2_score(self):
        self.score_2 +=1
        self.update_score()


    def game_over(self, winner):
        self.goto(0,0)
        self.write(f"{winner} Wins!!", move=False, align=ALIGNMENT, font=FONT)