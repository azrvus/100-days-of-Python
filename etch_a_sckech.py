from turtle import Turtle, Screen
import turtle
tim = Turtle()
screen = Screen()
def move_forwards():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def recl():
    tim.reset()
def rot():
    tim.right(25)
def rotle():
    tim.left(25)
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='c', fun=recl)
screen.onkey(key='a', fun=rot)
screen.onkey(key='d', fun=rotle)
screen.exitonclick()