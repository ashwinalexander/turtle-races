from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
expected_winner = screen.textinput(title="Make a bet", prompt="Which turtle will win? Pick a color: ")
winner = "noone"
colors = ["red", "orange", "yellow", "green", "blue","purple"]
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-225, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if expected_winner:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if(turtle.xcor() > 220):
            is_race_on = False
            winner = turtle.fillcolor();


if winner == expected_winner:
    print(f"You win! {winner} is the winner")
else:
    print(f"You lose.{winner} is the winner")









screen.exitonclick()