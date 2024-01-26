# from turtle module import Turtle, Screen classes
from turtle import Turtle, Screen

# take object from Turtle class : named   turtle1
turtle1 = Turtle()
turtle1.shape('turtle')
turtle1.speed('slowest')

turtle1.fillcolor('green')
turtle1.begin_fill()
for i in range(4):
    turtle1.forward(250)
    turtle1.left(90)

turtle1.end_fill()

turtle1.penup()
turtle1.goto(x= -200, y= 100)

# to draw square stamps
turtle1.shape('square')
turtle1.stamp()
turtle1.forward(100)
turtle1.stamp()
turtle1.forward(100)
turtle1.stamp()

turtle1.goto(-100, -100)
turtle1.pendown()
turtle1.shape('turtle')
turtle1.circle(50)


# take object from Screen class : named  my_screen
my_screen = Screen()
my_screen.exitonclick()