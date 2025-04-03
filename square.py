import turtle
turtle.Screen().setup(300,400)
turtle.Screen().bgcolor('light blue')
square=turtle.Turtle()
side=4
length=200
angle=360/side
for i in range(side):
 square.forward(length)
 square.right(angle)
turtle.done()