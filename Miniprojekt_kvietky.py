import math
import turtle

turtle.delay(0)
turtle.hideturtle()

def premiestni():
    turtle.pu()
    turtle.setpos(-100,-150)
    turtle.pd()

def polupen(uhol, pocet, velkost):                          # Spraví pol-lupeň
    for i in range(pocet):
        turtle.fd(velkost)
        turtle.left(uhol)


def lupen(uhol, pocet, velkost):                            # Spraví lupeň
    for i in range(2):
        polupen(uhol, pocet, velkost)
        turtle.left(180 - uhol * pocet)


def list_p(uhol, pocet, velkost, uhol_listu):                 # PRAVY LIST
    turtle.seth(uhol_listu)                              # Uhol prvého listu od zeme
    for i in range(2):
        polupen(uhol, pocet, velkost)
        turtle.left(180 - uhol * pocet)


def list_l(uhol, pocet, velkost, uhol_listu):                # LAVY LIST
    turtle.seth(180 - uhol_listu)                        # Uhol druheho listu od zeme, musí byť rovnaký ako prvý
    for i in range(2):
        for j in range(pocet):
            turtle.fd(velkost)
            turtle.right(uhol)
        turtle.right(180 - uhol * pocet)


def polupen_lavotocivy(uhol, pocet, dlzka):                     # LAVOTOCIVÁ STONKA
    for i in range(pocet):
        turtle.forward(dlzka)
        turtle.right(uhol)


def stonka(polomer, uhol):
    if uhol < 0:                                            # Ak sa zadá záporný uhol
        uhol = uhol * (-1)
    arc_length = 2 * math.pi * polomer                      # s týmto "uhol/360" to len zmenší dlzku stonky
    n = int(arc_length / 4)
    step_length = arc_length / n
    step_angle = float(uhol) / n

    turtle.seth(180 - (180 - uhol) / 2)
    polupen_lavotocivy(step_angle, n, step_length)


def kvet(uhol_lupen, uhol_list, pocet_lupen, pocet_list, velkost, pocet_lup, uhol_listu):
    premiestni()
    list_p(uhol_list, pocet_list, velkost, uhol_listu)
    list_l(uhol_list, pocet_list, velkost, uhol_listu)
    stonka(60, -90)
    for i in range(pocet_lup):
        lupen(uhol_lupen, pocet_lupen, velkost)
        turtle.left(360 / pocet_lup)


kvet(6, 6, 9, 9, 19, 8, 30)

turtle.exitonclick()



'''
VYSVETLIVKY KVET :
    uhol_lupen - tučnosť/chudosť lupeňa
    uhol_list - tučnosť/chudosť listu
    pocet_lupen - for-cyklus ide dlhšie - POMER, kde budú aj dlhšie aj tučnejšie
    pocet_list - for-cyklus ide dlhšie - POMER, kde budú aj dlhšie aj tučnejšie
    velkost - dĺžka listov/kvetov 
    pocet_lup - počet lupeňov na kvete
    uhol_listu - uhol oboch listov od zeme
'''
'''
VYSVETLIVKY STONKA :
    prvé_číslo - dĺžka stonky
    druhé_číslo - uhol (ohnutosť) stonky
'''
