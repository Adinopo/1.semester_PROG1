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
    else:
        print("You entered wrong char!")

#6
def pocet_rovnakych(a, b, c):
    if a == b == c:
        print("All 3 numbers are equal.")
    elif a == b or a == c or b == c:
        print("2 numbers are equal.")
    else:
        print("None of the numbers are equal.")

#7
def del_piatimi(n):
    sum = 0
    for i in range(n):
        num = int(input("Enter integer value: "))
        if num % 5 == 0:
            sum += 1
    print(str(sum) + " numbers are divisible by 5.")

#8
def sum_num(n):
    sum = 0
    for i in range(n):
        num = int(input("Enter integer value: "))
        sum += num
    print(sum)

#9-10
def int_max(n):
    max = int(input())
    max_2 = int(input())
    if max_2 > max:
        pom = max
        max = max_2
        max_2 = pom
    for i in range(n-2):
        num = int(input())
        if num > max:
            max_2 = max
            max = num
        elif num > max_2:
            max_2 = num
    print(max,"\n",max_2)

#11
def delitelnost(num):
    for i in range(num):
        if num % (1+i) == 0:
            print(i+1)

#12
def prvocisla(a):
    sum = True
    for i in range(a-2):
        if a % (i+2) > 0:
            pass
        else:
            print("Entered number is even.")
            return
    if sum:
        print("Entered number is odd.")

#12-1
def prvocial_1(a):
    if a == 2:
        print("2")
        return
    sum = True
    for i in range(a-2):
        for j in range(i+3):
            if ((i+3) % (j+2)) > 0 and j+2 != i+3:
                sum = True
            else:
                break
        if sum:
            print(i+3)



#14 ŠACHOVÉ
#Rook move
def rook_move(row1, column1, row2, column2):
    if row1 == row2 or column1 == column2:
        print("Rook can move there")
    else:
        print("Rook can not move there")


#15 Same color
def cheess_color(x1, y1, x2, y2):
    result_1 = False
    result_2 = False
    if (x1 + y1) % 2 == 0:
        print("First coordination is Black")
        result_1 = True
    elif (x2 + y2) % 2 == 0:
        print("Second coordination is Black")
        result_2 = True

    if result_1 and result_2:
        print("Both are the same color")
    elif not(result_1):
        print("First coordination is White")
    elif not(result_2):
        print("Second coordination is White")


#16 King move
def king_move(x1, y1, x2, y2):
    if ((x1 + 1) >= x2 >= (x1 - 1)) and ((y1 + 1) >= y2 >= (y1 - 1)):
        print("King can move there")
    else:
        print("King can not move there")


#17 Bishop move
def bishop_move(x1, y1, x2, y2):
    if abs(x2 - x1) == abs(y2 - y1):
        print("Bishop can move there")
    else:
        print("Bishop can not move there")


#18 Queen move
def queen_move(x1, y1, x2, y2):
    if abs(x2 - x1) == abs(y2 - y1) or x1 == x2 or y1 == y2:
        print("Queen can move there")
    else:
        print("Queen can not move there")


#19 Knight move
def knight_move(x1, y1, x2, y2):
    if (x1 + 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2)) or (x1 + 1 == x2 and (y1 + 2 == y2 or y1 - 2 == y2)) or (x1 - 1 == x2 and (y1 + 2 == y2 or y1 - 2 == y2)) or (x1 - 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2)):
        print("Knight can move there")
    else:
        print("Knight can not move there")


#knight_move(3,5,4,8)

#queen_move(4,1,1,4)

#bishop_move(4,4,1,7)

#king_move(3,3,6,4)

#cheess_color(3,5,2,7)

#(rook_move(1,2,1,8))

#-----------------------------------------------------

#prvocial_1(15)

#prvocisla(2)

#delitelnost(12)

#int_max(5)

#sum_num(5)

#del_piatimi(5)

#pocet_rovnakych(2,0,8)

#znak = input("Enter a char: ")
#menu(znak)

#cislo = int(input("Enter an integer value: "))
#print(test_parita(cislo))

#min_dvoch(20,12)
#min_troch(60,50,90)
