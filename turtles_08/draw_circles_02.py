import random
from turtle import Turtle, Screen

turtle1 = Turtle()
colors_list = ['red', 'green', 'blue', 'yellow', 'black', 'grey', 'brown']
turtle1.penup()
for i in range(10):
    choosen_color = random.choice(colors_list)
    turtle1.color(choosen_color)
    turtle1.circle(100)
    turtle1.left(15)


my_screen = Screen()
my_screen.exitonclick()