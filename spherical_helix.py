


# Python program to draw
# Spiral Helix Pattern
# using Turtle Programming

import turtle
loadWindow = turtle.squares()
turtle.speed(2)

for i in range(100):
  turtle.circle(5*i)
  turtle.circle(-5*i)
  turtle.left(i)

turtle.exitonclick()