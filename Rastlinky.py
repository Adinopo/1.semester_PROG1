import turtle

turtle.hideturtle()
#turtle.speed(10)
turtle.delay(0)

def premiestni(suradnice):
    turtle.pu()
    turtle.goto(suradnice)
    turtle.pd()


def premiestnihome():
    turtle.pu()
    turtle.home()
    turtle.pd()


def kvet():
    sum = 0
    for lupen in range(7):
        for i in range(50):
            turtle.left(1)
            turtle.forward(3)

        premiestnihome()

        sum+=50
        turtle.left(sum)

        for i in range(50):
            turtle.right(1)
            turtle.forward(3)

        premiestnihome()

        turtle.left(sum)


def stonka():
    turtle.home()
    turtle.left(240)
    for i in range(60):             # Stonka kolmo na dol
        turtle.left(1)
        turtle.forward(6)           # Dlzka stonky


def listky():
    turtle.setheading(0)
    var = turtle.position()

    for leaves in range(2):         # Cyklus na vykreslenie oboch lístkov
        for i in range(30):         # 1 listok
            turtle.forward(4)
            turtle.left(3)

        premiestni(var)

        for i in range(30):         # 2 listok
            turtle.right(3)
            turtle.forward(4)

        turtle.pu()
        turtle.goto(var)
        turtle.pd()
        turtle.left(90)


kvet()
stonka()
listky()

turtle.exitonclick()                # Nezavrie canvas hneď, ale čaká na mouse-click
