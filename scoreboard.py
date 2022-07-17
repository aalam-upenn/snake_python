from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.player_score = 0
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.player_score} ", False, align="center", font=('Arial', 24, 'normal'))

    def update_score(self):
        self.player_score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", False, align=ALIGNMENT, font=FONT)

