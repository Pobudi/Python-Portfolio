import turtle
import random
from math import sqrt, floor, ceil
import time

screen = turtle.Screen()
screen.screensize(500, 500)
diego = turtle.Turtle()
a=300

main_vertexes = [(0, a), (-sqrt(1/3)*2*a, -a), (sqrt(1/3)*2*a, -a)]

diego.penup()
diego.speed("fastest")
diego.goto(main_vertexes[0])
diego.dot(10)
diego.goto(main_vertexes[1])
diego.dot(10)
diego.goto(main_vertexes[2])
diego.dot(10)

# y1 = -sqrt(3)*x + 300
# y2 = sqrt(3)*x + 300
# y3 = -300
x = random.randint(ceil(-sqrt(1/3)*2*a), floor(sqrt(1/3)*2*a))
y = random.randint(-300, ceil(-abs(x)*sqrt(3)+300))
first_point = (0, -50)
diego.color("red")
diego.goto(first_point)
diego.dot(10)
diego.color("black")

# vertex = random.choice(main_vertexes)
# diego.setheading(diego.towards(vertex))
# distance = floor(0.5*diego.distance(vertex))
# diego.forward(distance)
# diego.dot(8) 

for _ in range(10000):
    vertex = random.choice(main_vertexes)
    diego.setheading(diego.towards(vertex))
    distance = floor(0.5*diego.distance(vertex))
    diego.forward(distance)
    diego.dot(8)  
    



screen.exitonclick()
