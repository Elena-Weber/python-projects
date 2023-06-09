# turtle module is built-in in Python, same as random
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nEnter a color from this list:\nred, orange, yellow, green, blue, indigo, violet")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congrats, {winning_color} turtle is the winner!")
                print(f"Click anywhere on the turtle race screen to exit.")
            elif user_bet in colors:
                print(f"You've lost, {winning_color} turtle is the winner.")
                print(f"Click anywhere on the turtle race screen to exit.")
            else:
                print(f"You haven't chosen any color from the list but {winning_color} turtle is the winner.")
                print(f"Click anywhere on the turtle race screen to exit.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
