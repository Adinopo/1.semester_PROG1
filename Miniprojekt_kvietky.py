import math
import turtle

turtle.delay(0)

def polupen(uhol, pocet, velkost):                        # Uhol a Strana spolu suvisia
    for i in range(pocet):
        turtle.fd(velkost)
        turtle.left(uhol)


def lupen(uhol, pocet, velkost):
    for i in range(2):
        polupen(uhol, pocet, velkost)
        turtle.left(180 - uhol * pocet)


def list_l(uhol, pocet, velkost, uhol_listu):
    turtle.seth(uhol_listu)                                # Uhol prvého listu od zeme
    for i in range(2):
        polupen(uhol, pocet, velkost)
        turtle.left(180 - uhol * pocet)


def list_p(uhol, pocet, velkost, uhol_listu):
    turtle.seth(180-uhol_listu)                            # Uhol druheho listu od zeme, musí byť rovnaký ako prvý
    for i in range(2):
        for j in range(pocet):
            turtle.fd(velkost)
            turtle.right(uhol)
        turtle.right(180 - uhol * pocet)


def polupen_lavotocivy(uhol, pocet, dlzka):
    for i in range(pocet):
        turtle.forward(dlzka)
        turtle.right(uhol)


def stonka(polomer, uhol):                                  # Arc = oblúk
    arc_length = 2 * math.pi * polomer                      # s týmto uhol/360 to len zmenší dlzku stonky
    n = int(arc_length / 4)
    print(n)
    step_length = arc_length / n
    print(step_length)
    step_angle = float(uhol) / n
    print(step_angle)

    turtle.seth(180-(180-uhol)/2)
    polupen_lavotocivy(step_angle,n,step_length)


def kvet(uhol_lupen, uhol_list, pocet_lupen, pocet_list, velkost, pocet_lup, uhol_listu):        # uhol_lupen/list = tučnota lista, velkost = dlzka listov, pocet_list/lupen = tučnota listu
    list_l(uhol_list, pocet_list, velkost, uhol_listu)
    list_p(uhol_list, pocet_list, velkost, uhol_listu)
    stonka(60,90)
    for i in range(pocet_lup):
        lupen(uhol_lupen, pocet_lupen, velkost)
        turtle.left(360/pocet_lup)



kvet(8,6,10,15,9,8,30)

turtle.exitonclick()
