import math
import turtle

turtle.delay(0)

def polupen(uhol,strana,velkost):          # Uhol a Strana spolu suvisia
    for i in range(strana):
        turtle.fd(velkost)
        turtle.left(uhol)

def lupen(uhol, strana, velkost):
    for i in range(2):
        polupen(uhol, strana, velkost)
        turtle.left(180-uhol*strana)

def kvet(uhol,strana,velkost,pocet_lup):
    for i in range(pocet_lup):
        lupen(uhol, strana, velkost)
        turtle.left(360/pocet_lup)

def arc(polomer, uhol):                      # Arc = oblúk
    arc_length = 2 * math.pi * polomer
    n = int(arc_length / 4)
    step_length = arc_length / n
    step_angle = float(uhol) / n

    turtle.left(step_angle/2)
    turtle.seth(50)
    polupen(step_angle,n,step_length)
    turtle.right(step_length/2)


arc(40,80)                              # prvý argumet je POLOMER, druhý je ako velmi zaoblená bude
#kvet(4,10,20,12)

turtle.exitonclick()
