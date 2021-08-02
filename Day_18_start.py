from turtle import Turtle, Screen
import random
import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
tim.color('red', 'green')
tim.pensize(15)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = (0, 90, 180, 270)
for _ in range(1000000000):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))













screen = Screen()
screen.exitonclick()