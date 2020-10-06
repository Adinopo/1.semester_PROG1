import turtle

turtle.hideturtle()
turtle.speed(10)
turtle.pu()
turtle.goto(-250,250)
turtle.pd()

sum = 0

'''for lupen in range(7):
    for i in range(50):
        turtle.left(1)
        turtle.forward(5)

    turtle.pu()
    turtle.home()
    turtle.pd()

    sum+=50
    turtle.left(sum)

    for i in range(50):
        turtle.right(1)
        turtle.forward(5)

    turtle.pu()
    turtle.home()
    turtle.pd()


    turtle.left(sum)
'''

turtle.left(240)            # Stonka
for i in range(40):
    turtle.left(1.5)
    turtle.forward(7)

turtle.setheading(0)
var = turtle.position()

for i in range(30):         # Prvy listok
    turtle.forward(4)
    turtle.left(3)


turtle.pu()
turtle.goto(var)
turtle.pd()

for i in range(30):
    turtle.right(3)
    turtle.forward(4)

turtle.pu()
turtle.goto(var)
turtle.pd()
turtle.left(90)

for i in range(30):             # Druhy listok
    turtle.forward(4)
    turtle.left(3)


turtle.pu()
turtle.goto(var)
turtle.pd()

#turtle.left(10)
for i in range(30):
    turtle.right(3)
    turtle.forward(4)


turtle.exitonclick()
