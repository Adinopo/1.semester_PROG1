'''
Ulohy cvicenia 4
'''

import turtle

from pip._vendor.distlib.compat import raw_input

#turtle.hideturtle()
#turtle.delay(0)

#2
def test_parita(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False

#3
def min_dvoch(a, b):
    print("Smaller number is: ", end="")
    if a < b:
        print(a)
    else:
        print(b)

#4
def min_troch(a, b, c):
    print("Smaller number is: ", end="")
    if a < b:
        if c < a:
            print(c)
        else:
            print(a)
    elif c < b:
        print(c)
    else:
        print(b)

#5
def menu(znak):
    if znak == "s":
        print() # vykresli stvorec
    elif znak == "t":
        print() # vykresli 3-uholnik


def video(feet = 0, inches = 0):            # keyword arguments
    inputt = input("Enter code:")
    if len(inputt) < 6:                     # funkcia "len()"
        print("Your string is less than 6 letters.")
    else:
        print("Your string is more than 6 letters.")






#znak = input("Enter a char: ")
#menu(znak)

#cislo = int(input("Enter an integer value: "))
#print(test_parita(cislo))

#min_dvoch(20,12)
#min_troch(60,50,90)
