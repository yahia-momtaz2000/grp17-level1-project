# from turtle module import Tutle, Screen class
import random
from turtle import Turtle, Screen


# my functions
# draw_turtle function
def draw_turtle(generic_name, turtle_color, y_pos):
    generic_name = Turtle()
    generic_name.color(turtle_color)
    generic_name.shape('turtle')
    generic_name.shapesize(1.5)
    generic_name.penup()
    generic_name.goto(-300, y_pos)
    generic_name.pendown()
    return generic_name


# move_turtle_func function to control the green turtle
game_end = False
def move_turtle_func():
    if game_end == False:
        g_turtle.forward(40)

# create object from Turtle class
my_turtle = Turtle()

# create object from Screen
my_screen = Screen()
# Screen Setup
my_screen.title('My Race Game')
my_screen.setup(800, 500)
my_screen.bgcolor('forestgreen')

# Write Text [ Heading ]
my_turtle.penup()
my_turtle.goto(-100, 205)
my_turtle.write('Yahia race', font=('Arial', 20, 'bold') )

# The Floor
my_turtle.goto(-350, 200)
my_turtle.fillcolor('chocolate')
my_turtle.pendown()
my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()

# draw the end line
my_turtle.goto(250, 200)
my_turtle.right(90)
my_turtle.forward(400)


# Drawing Turtles : Calling draw_function : 4 times
b_turtle = draw_turtle('blue_turtle', 'cyan', 150)
p_turtle = draw_turtle('pink_turtle', 'pink', 50)
y_turtle = draw_turtle('yellow_turtle', 'yellow', -50)
g_turtle = draw_turtle('green_turtle', 'green', -150)

# I need to Control the green turtle
my_screen.listen()
my_screen.onkey(move_turtle_func, 'Right')

while True:
    b_turtle.forward(random.randint(1, 10))
    p_turtle.forward(random.randint(1, 10))
    y_turtle.forward(random.randint(1, 10))
    # g_turtle.forward(random.randint(1, 10))

    # if any one is a winner [  x pos == 230 ]
    if b_turtle.xcor() >= 230:
        winner = b_turtle
        break
    elif p_turtle.xcor() >= 230:
        winner = p_turtle
        break
    elif y_turtle.xcor() >= 230:
        winner = y_turtle
        break
    elif g_turtle.xcor() >= 230:
        winner = g_turtle
        break

# Celebrate The Winner
game_end = True
winner.shapesize(2.5)
for i in range(1000):
    winner.left(5)



my_screen.exitonclick()