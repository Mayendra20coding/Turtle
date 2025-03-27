import turtle
turtle.Screen().setup(300,400)
turtle.Screen().bgcolor('blue')
polygon=turtle.Turtle()
side=6
length=200
angle=360/side
for i in range(side):
 polygon.forward(length)
 polygon.right(angle)
turtle.done()